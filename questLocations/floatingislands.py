from questLocations.api import api_userData, api_call, api_changeTrap, api_userData_body
from util import eprint, debug
import time


class FloatingIslands():
    def __init__(self, request_acc, debug=False):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/environment/floating_islands.php"
        self.quest = "QuestFloatingIslands"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        # self.data = api_userData(self.request_cookies)
        self.data = api_userData_body(self.request_cookies, {"uh": request_acc['uh'], "page_class":"Camp"})  
        self.data2 = api_userData_body(self.request_cookies, {"uh": request_acc['uh'], "page_class":"Camp"})  
        self.debug = debug

    def leaveTheIsland(self):
        self.request_body['action'] = 'retreat'
        eprint('Floating Islands', 'Leaving the island')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def toggleBottledWind(self):
        self.request_body['action'] = 'toggle_fuel'
        return api_call(self.URL, self.request_cookies, self.request_body)

    def isIslandFullyExplored(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['island_progress'] == 40

    # def isPirateCheeseEmpty(self):
    def isAtLastPanel(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['island_progress'] > 29

    def distanceFromWarden(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['enemy_encounter_hunts_remaining']

    def has_defeated_enemy(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['has_defeated_enemy']

    def isBattlingWarden(self):
        return self.distanceFromWarden(
        ) == 0 and not self.has_defeated_enemy() and not self.isOnHighAltitudeIsland()

    def isBattlingParagon(self):
        return self.distanceFromWarden(
        ) == 0 and not self.has_defeated_enemy() and self.isOnHighAltitudeIsland()

    def getBottledWindStatus(self):  # None if false
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['is_fuel_enabled'] == True

    def isAtCurrentLocation(self):
        if self.data['user']['quests'].get(self.quest) != None:
            return True
        return False

    def getDistanceFromWarden(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['enemy_encounter_hunts_remaining']

    def hasDefeatedWarden(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['has_defeated_enemy']

    def getIslandType(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['island_type']

    def isAtLaunchPad(self):
        return self.getIslandType() == 'launch_pad_island'

    def getSkyMapGrid(self):
        self.request_body['action'] = 'get_adventure_board'
        response = api_call(self.URL, self.request_cookies,
                            self.request_body)['adventure_board']['grid']
        print([grid['type'] for grid in response])
        # response = api_call(self.URL, self.request_cookies, self.request_body)
        return [grid['type'] for grid in response]

    def useCyclone(self):
        self.request_body['action'] = 'randomize_adventure_board'
        eprint('Floating Islands', 'Randomize Adventure Board')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def launch(self, powertype):
        self.request_body['action'] = 'launch'
        self.request_body['power_type'] = powertype
        self.request_body['use_saved_trap_setup'] = 0
        eprint('Floating Islands', f'Launching to {powertype} island')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def sortSkyMapGrid(self):
        grid = self.getSkyMapGrid()
        weaponMap = {
            'arcn': grid[0:4],
            'frgttn': grid[4:8],
            'hdr': grid[8:12],
            'shdw': grid[12:16],
            'drcnc': grid[12::-4],
            'law': grid[13::-4],  # verified
            'phscl': grid[14::-4],  # verified
            'tctcl': grid[15::-4],
        }
        return weaponMap

    def determineIslandTarget(self, mode='normal'):
        weaponMap = self.sortSkyMapGrid()

        # Debugging
        for power in weaponMap:
            eprint("Floating islands", f'{power} : {weaponMap[power]}')

        def assignScore(map):
            if map == 'ore_bonus':
                return 2
            if map == 'gem_bonus':
                return 2
            if map == 'sky_cheese':
                return 1
            if map == 'loot_cache':
                return 3
            if map == "sky_pirates":
                return 4
            if map[0:13] == 'paragon_cache':
                return 5
            if map[-6:] == 'shrine':
                return 5

            return 0

        # key is to make everything 3,2,1,0
        scoring = []
        eprint('Floating Islands', f'{mode} mode grid search')

        for power in weaponMap:
            # if power == "drcnc":
            #     eprint("Floating Islands", "Skipping Draconic")
            #     continue

            # Pirate Mode
            if mode == 'pirate':
                if weaponMap[power][0] != 'sky_pirates':
                    continue

                skipping = True
                for slot in weaponMap[power]:
                    if slot[-6:] == 'shrine':
                        skipping = False
                if skipping:
                    continue
            
            # Pirate mode on high altitude island, prioritize pirate on high altitude
            elif mode == 'high_pirate':
                if not ('loot_cache' in weaponMap[power] and 'sky_pirates' in weaponMap[power]):
                    continue

            # Loot mode on high altitude island, prioritize pirate on loot
            elif mode == 'high_loot':
                if 'loot_cache' in weaponMap[power]:
                    print(f'{power}: {weaponMap[power]}')
                    print(f'gem bonus: {weaponMap[power].count("gem_bonus")}, ore bonus: {weaponMap[power].count("ore_bonus")}')

                    if not (weaponMap[power].count("gem_bonus") == 2 or weaponMap[power].count("ore_bonus") == 2):
                        print(f"{power}: not consideered")
                        continue

                elif not (weaponMap[power].count("gem_bonus") == 3 or weaponMap[power].count("ore_bonus") == 3):
                    print(f"{power}: not consideered")
                    continue

            # The first tile must be paragon or shrine
            else:
                if not (weaponMap[power][0][0:13] == 'paragon_cache'
                        or weaponMap[power][0][-6:] == 'shrine'):
                    continue

                # Count the number of empty skies
                noEmptySky = [
                    item for item in weaponMap[power] if item != 'empty_sky'
                ]
                if weaponMap[power][0][0:13] == 'paragon_cache':
                    if len(noEmptySky) < 4:
                        continue
                if weaponMap[power][0][-6:] == 'shrine':
                    if len(noEmptySky) < 2:
                        continue
            score = assignScore(weaponMap[power][0]) * 1000 + assignScore(
                weaponMap[power][1]) * 100 + assignScore(
                    weaponMap[power][2]) * 10 + assignScore(
                        weaponMap[power][3]) * 1
            scoring.append({"power": power, "score": score})

        newlist = sorted(scoring, key=lambda k: k['score'], reverse=True)

        # newWeaponMap = {}
        for item in newlist:
            eprint('Selected Type',
                   f'{item["power"]} : {weaponMap[item["power"]]}')
            return item['power']

    def setTrap(self, settings):
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})

    def armWardenSetup(self):
        status = False
        if self.getTrapSetup('weapon') != 'geyser_physical_weapon':
            self.setTrap({'weapon': 'geyser_physical_weapon'})
            eprint('Floating Islands', 'Arming Smoldering Stone sentinel')
            status = True

        if self.getTrapSetup('bait') != 'toxic_super_brie_cheese':
            self.setTrap({'bait': 'toxic_super_brie_cheese'})
            eprint('Floating Islands', 'Arming empowered SB+')
            status = True

        if self.getTrinket() != 'Rift Ultimate Power Charm':
            self.setTrap({'trinket': 'rift_ultimate_power_trinket'})
            eprint('Floating Islands', 'Arming Rift ultimate power charm')
            status = True

        if status:
            eprint('Floating Islands', 'Armed warden setup, ready to battle.')

    def armParagonSetup(self):
        status = False
        if self.getTrapSetup('bait') != 'toxic_super_brie_cheese':
            self.setTrap({'bait': 'toxic_super_brie_cheese'})
            eprint('Floating Islands', 'Arming empowered SB+')
            status = True

        if self.getTrinket() != 'Rift Ultimate Power Charm':
            self.setTrap({'trinket': 'rift_ultimate_power_trinket'})
            eprint('Floating Islands', 'Arming Rift ultimate power charm')
            status = True

        if status:
            eprint('Floating Islands', 'Armed paragon setup, ready to battle.')


    def getCorsairCheeseCount(self):
        return self.data['user']['enviroment_atts']['items']['sky_pirate_cheese']['quantity']

    def getTrapSetup(self, type):
        return self.data2['trap_image']['layers'][type]['type']

    def getTrinket(self):
        return self.data2['page']['trinket_name']

    def armPirateSetup(self):
        if self.getTrapSetup('weapon') != 'pirate_sleigh_weapon':
            self.setTrap({'weapon': 'pirate_sleigh_weapon'})
            eprint('Floating Islands', 'Arming Pirate Trap')

        if self.getTrapSetup('bait') != 'sky_pirate_cheese':
            self.setTrap({'bait': 'sky_pirate_cheese'})
            eprint('Floating Islands', 'Arming Pirate Cheese')

        if self.getTrinket() != 'Rift Extreme Power Charm':
            self.setTrap({'trinket': 'rift_extreme_power_trinket'})
            eprint('Floating Islands', 'Arming Rift extreme power charm')

    def isOnHighAltitudeIsland(self):
        return self.data2['user']['enviroment_atts']['hunting_site_atts']['is_high_tier_island'] == True

    def armSavedSetup(self):
        self.request_body['action'] = 'arm_saved_setup'
        return api_call(self.URL, self.request_cookies, self.request_body)

    def isArmingSavedSetup(self):
        # Added a bypass due to lack of charms
        if self.data['user']['trinket_name'] == None:
            return True

        return self.data['user']['quests'][
            self.quest]['saved_trap_setup']['is_active'] == True

    def isAtHAI(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['sky_wardens_caught'] == 4

    def enableBottledWind(self):
        if self.getBottledWindStatus() == False:
            eprint('Floating Islands', 'Enabled bottled wind.')
            self.toggleBottledWind()

    def disableBottledWind(self):
        if self.getBottledWindStatus() == True:
            eprint('Floating Islands', 'Disabled bottled wind.')
            self.toggleBottledWind()

    def getScoreBoardData(self):
        URL = 'https://www.mousehuntgame.com/managers/ajax/pages/scoreboards.php'
        self.request_body[
            'scoreboard'] = 'QuestFloatingIslands::total_islands_explored'
        self.request_body['action'] = 'get_page'
        self.request_body['category'] = 'main'
        self.request_body['weekly'] = 0
        self.request_body['friends_only'] = 0
        self.request_body['search'] = ''
        self.request_body['page'] = 1
        return api_call(URL, self.request_cookies, self.request_body)

    def displayScoreBoardData(self):
        data = self.getScoreBoardData()['scoreboard_page']['rows']
        for index, row in enumerate(data):
            if row['name'] == "Howard Low":
                row['name'] = 'Howard Low <========================= this is you!'
            print(f'#{row["rank"]}, {row["points"]} points, {row["name"]}')

    # Main Automation
    def automateHunt(self):
        if not self.isAtCurrentLocation():
            # eprint('Floating Islands', 'User not at current location')
            return

        self.getSkyMapGrid()
        return

        # Commence loop to scramble door until the preferred door is available
        while (True):
            pirate_threshold = 20

            if self.isAtLaunchPad():
                while True:
                    power = None
                    # if self.isAtHAI():
                    #     power = self.determineIslandTarget('high_pirate')
                    if self.isAtHAI():
                        power = self.determineIslandTarget('high_loot')
                    elif self.getCorsairCheeseCount() >= pirate_threshold:
                        print(self.getCorsairCheeseCount())
                        power = self.determineIslandTarget('pirate')
                    elif self.getCorsairCheeseCount() < pirate_threshold:
                        power = self.determineIslandTarget()

                    if power != None: break
                    if power == None:
                        eprint("Floating islands", "No suitable island found, triggering cyclone.")
                        self.useCyclone()  # Troubleshoot first
                        time.sleep(15)
                eprint("Floating islands", f'Launch code is {power}')
                # If launching to pirate, equip pirate setup
                if self.getCorsairCheeseCount() >= pirate_threshold:
                    self.launch(power)
                    self.armPirateSetup()
                else:
                    self.launch(power)
                    self.armSavedSetup()
                return


            else:
                # Leave the island if fully explored
                if self.isIslandFullyExplored() and not self.isOnHighAltitudeIsland():
                    eprint('Floating Islands', 'Low Altitude Island is fully explored.')
                    self.leaveTheIsland()
                    return

                # Trap setup determination
                if self.isBattlingWarden():
                    self.armWardenSetup()
                elif self.isBattlingParagon():
                    self.armParagonSetup()
                elif self.isOnHighAltitudeIsland():
                    if not self.isArmingSavedSetup():
                        eprint("Floating Islands", "On high altitude island, arm saved setup.")
                        self.armSavedSetup()
                elif self.getCorsairCheeseCount() >= pirate_threshold: 
                    self.armPirateSetup()
                elif self.getCorsairCheeseCount() < pirate_threshold:
                    if not self.isArmingSavedSetup():
                        eprint("Floating Islands", "Low on corsair cheese, arming saved setup.")
                        self.armSavedSetup()

                # Ensure the bottled wind is on
                if self.isAtLastPanel():
                    self.disableBottledWind()
                else:
                    self.enableBottledWind()

            return
