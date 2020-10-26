from questLocations.api import api_userData, api_call, api_changeTrap
from util import eprint, debug
import time


class FloatingIslands():
    def __init__(self, request_acc, debug=False):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/environment/floating_islands.php"
        self.quest = "QuestFloatingIslands"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData(self.request_cookies)
        self.debug = debug

    def leaveTheIsland(self):
        self.request_body['action'] = 'retreat'
        eprint('Floating Islands', 'Leaving the island')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def toggleBottledWind(self):
        self.request_body['action'] = 'toggle_fuel'
        eprint('Floating Islands', 'Toggled Bottled Wind')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def isIslandFullyExplored(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['island_progress'] == 40

    def distanceFromWarden(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['enemy_encounter_hunts_remaining']

    def has_defeated_enemy(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['has_defeated_enemy']

    def isBattlingWarden(self):
        return self.distanceFromWarden(
        ) == 0 and not self.has_defeated_enemy() and not self.isAtHAI()

    def isBattlingParagon(self):
        return self.distanceFromWarden(
        ) == 0 and not self.has_defeated_enemy() and self.isAtHAI()

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
        # response = api_call(self.URL, self.request_cookies, self.request_body)
        return [grid['type'] for grid in response]

    def useCyclone(self):
        self.request_body['action'] = 'randomize_adventure_board'
        eprint('Floating Islands', 'Randomize Adventure Board')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def launch(self, powertype):
        self.request_body['action'] = 'launch'
        self.request_body['power_type'] = powertype
        self.request_body['use_saved_trap_setup'] = 1
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

    def determineIslandTarget(self):
        weaponMap = self.sortSkyMapGrid()

        # Debugging
        for power in weaponMap:
            print(f'{power} : {weaponMap[power]}')

        def assignScore(map):
            if map == 'ore_bonus':
                return 2
            if map == 'gem_bonus':
                return 2
            if map == 'sky_cheese':
                return 1
            if map[0:13] == 'paragon_cache':
                return 3
            if map[-6:] == 'shrine':
                return 3

            return 0

        # key is to make everything 3,2,1,0
        scoring = []
        for power in weaponMap:
            if power == "drcnc":
                eprint("Floating Islands", "Skipping Draconic")
                continue

            # The first tile must be paragone or shrine
            if not (weaponMap[power][0][0:13] == 'paragon_cache'
                    or weaponMap[power][0][-6:] == 'shrine'):
                continue

            # Need the good loot
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
        self.setTrap({
            'weapon': 2844,
            'base': 3023,
            'bait': 1967,
            'trinket': 545
        })
        eprint('Floating Islands', 'Arming Warden Setup')

    def armParagonSetup(self):
        self.setTrap({'base': 3023, 'bait': 1967, 'trinket': 545})
        eprint('Floating Islands', 'Arming Paragon Setup')

    def armSavedSetup(self):
        self.request_body['action'] = 'arm_saved_setup'
        eprint('Floating Islands', 'Arming saved Setup')
        return api_call(self.URL, self.request_cookies, self.request_body)

    def isArmingSavedSetup(self):
        return self.data['user']['quests'][
            self.quest]['saved_trap_setup']['is_active'] == True

    def isAtHAI(self):
        return self.data['user']['quests'][
            self.quest]['hunting_site_atts']['sky_wardens_caught'] == 4

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

        # Commence loop to scramble door until the preferred door is available
        while (True):
            # Leave the island if fully explored
            if self.isIslandFullyExplored():
                eprint('Floating Islands', 'Island is fully explored.')
                self.leaveTheIsland()
                return

            # Battling Warden
            if self.isBattlingWarden() and self.isArmingSavedSetup():
                eprint("Floating Islands", "Battling Warden")
                self.armWardenSetup()
            elif self.isBattlingParagon() and self.isArmingSavedSetup():
                eprint("Floating Islands", "Battling Paragon")
                self.armParagonSetup()
            else:
                if not self.isArmingSavedSetup():
                    self.armSavedSetup()

            # Ensure the bottled wind is on
            if self.getBottledWindStatus() == False:
                self.toggleBottledWind()

            # Stop at HAI
            if self.isAtHAI():
                eprint("Floating islands",
                       f'At High Altitude island, do nothing')
                return

            if self.isAtLaunchPad():
                while True:
                    power = self.determineIslandTarget()
                    if power != None: break
                    if power == None:
                        eprint("FLoating island", "Triggering Cyclone")
                        self.useCyclone()  # Troubleshoot first
                        time.sleep(60)
                eprint("Floating islands", f'Launch code is {power}')
                self.launch(power)
                return

            return
