from questLocations.api import api_userData, api_call, api_changeTrap, api_userData_body
from util import eprint
import time


class GWH():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/events/winter_hunt.php"
        self.quest = "QuestWinterHunt2020"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        # self.data = api_userData(self.request_cookies)
        self.data = api_userData_body(self.request_cookies, {"uh": request_acc['uh'], "page_class":"Tournament"})    
        self.name = request_acc['name']

    def isAtCurrentLocation(self):
        if self.data['user']['quests'].get(self.quest) != None:
            return True
        return False

    def setTrap(self, settings):
        res = api_changeTrap(self.request_cookies, {
            **self.request_body,
            **settings
        })

    def getCurrentCheese(self):
        return self.data['user']['bait_name']

    def getCurrentCheeseQuantity(self):
        return self.data['user']['bait_quantity']

    def isArmingPecanCheese(self):
        current_bait = self.getCurrentCheese()
        if current_bait in ['Glazed Pecan Pecorino Cheese', 'Pecan Pecorino Cheese']:
            return True
        return False

    def setSuperBrie(self):
        if self.getCurrentCheese() != "SUPER|brie+":
            eprint("GWH", f"{self.name}: Arming SB+")
            self.setTrap({'bait': 'super_brie_cheese'})

    def buildGolem(self, slot, environment, hat):
        self.request_body['action'] = 'build_golem'
        self.request_body['slot'] = slot
        self.request_body['environment'] = environment
        self.request_body['has_hat'] = hat
        # self.request_body['head'] = 0
        # self.request_body['arms'] = 0
        # self.request_body['legs'] = 0
        # self.request_body['torso'] = 0
        return api_call(self.URL, self.request_cookies, self.request_body)

    def joinTournament(self, tournament_id):
        self.request_body['action'] = 'join'
        self.request_body['tournament_id'] = tournament_id
        self.request_body['hg_is_ajax'] = 1
        self.request_body['sn'] = 'Hitgrab'
        tournamen_url = "https://www.mousehuntgame.com/managers/ajax/users/tournament.php"
        return api_call(tournamen_url, self.request_cookies, self.request_body)

    def getCurrentCharm(self):
        return self.data['user']['enviroment_atts']['trinket_name']

    def getCurrentCharmQuantity(self):
        try:
            return int(self.data['user']['enviroment_atts']['trinket_quantity_formatted'].replace(",", ""))
        except:
            return 0

    def getGolemStats(self):
        return self.data['user']['quests'][self.quest]['golems']

    def isGolemReadyToClaim(self, slot):
        golems = self.getGolemStats()
        return golems[slot]['can_claim']

    def claimReward(self, slot):
        self.request_body['action'] = 'claim_reward'
        self.request_body['slot'] = slot
        return api_call(self.URL, self.request_cookies, self.request_body)

    def getHUDItemCount(self, item):
        return int(self.data['user']['quests'][self.quest]['items'][item]['quantity'])

    def getSpecialTournaments(self):
        return self.data['page']['tournaments'][1]['tournaments']

    def getNextAvailableTournmanetID(self):
        tournaments = self.getSpecialTournaments()
        for tournament in tournaments:
            if tournament['name'][-33:] == "Snow Golem Celebration Tournament" and tournament['can_join']:
                eprint("Tournament", f"{self.name}: Joining tournament {tournament['name']}")
                return tournament['tournament_id']

    def isMinimumGolemPartsMet(self):
        qty_head = self.getHUDItemCount('golem_part_head_stat_item')
        qty_limb = self.getHUDItemCount('golem_part_limb_stat_item')
        qty_torso = self.getHUDItemCount('golem_part_torso_stat_item')
        if qty_head >= 3 and qty_limb >= 12 and qty_torso >= 3:
            return True
        return False

    def checkAndJoinTournament(self):
        tournamentID = self.getNextAvailableTournmanetID()
        if tournamentID != None:
            res = self.joinTournament(int(tournamentID))
            eprint("Tournament", f"{self.name}: Joined tournament")

    def determineCharm(self):
        if self.getCurrentCharmQuantity() < 3:
            eprint("GWH", f"{self.name}: Running low on {self.getCurrentCharm()}")
            current_charm = self.getCurrentCharm()

            if current_charm == "Let It Snow Charm":
                eprint("GWH", f"{self.name}: Arming Winter Charm")
                self.setTrap({'trinket': "festive_trinket"})

            elif current_charm == "Winter Charm":
                eprint("GWH", f"{self.name}: Arming Gilded Charm")
                self.setTrap({'trinket': "gilded_trinket"})

            # elif current_charm == "Rift Super Snowball Charm":
            #     eprint("GWH", f"{self.name}: Arming Rift Snowball Charm")
            #     self.setTrap({'trinket': "rift_snowball_trinket"})

            else:
                eprint("GWH", f"{self.name}: Arming Gilded Charm")
                self.setTrap({'trinket': "gilded_trinket"})

        if self.isMinimumGolemPartsMet():
            if self.getHUDItemCount('let_it_snow_trinket') > 1:                
                if not self.getCurrentCharm() == "Let It Snow Charm":
                    self.setTrap({'bait': 'gouda_cheese'})
                    self.setTrap({'trinket': "let_it_snow_trinket"})
                    eprint("GWH", f"{self.name}: Arming gouda and extra LISC to keep the number to below 20")

            elif self.getHUDItemCount('glazed_pecan_pecorino_cheese') > 2:
                if self.getCurrentCheese() != "Glazed Pecan Pecorino Cheese":
                    self.setTrap({'bait': 'glazed_pecan_pecorino_cheese'})
                    self.setTrap({'trinket': "festive_trinket"})
                    eprint("GWH", f"{self.name}: Arming Glazed Pecan Pecorino and winter charm")

            elif self.getHUDItemCount('pecan_pecorino_cheese') > 2:
                if self.getCurrentCheese() != "Pecan Pecorino Cheese":
                    self.setTrap({'bait': 'pecan_pecorino_cheese'})
                    self.setTrap({'trinket': "festive_trinket"})
                    eprint("GWH", f"{self.name}: Arming Pecan Pecorino and winter charm")

            else:
                if not self.getCurrentCheese() == "Gouda Cheese":
                    self.setTrap({'bait': 'gouda_cheese'})
                    eprint("GWH", f"{self.name}: Insufficient Pecan cheeses, using Gouda Cheese")
            return

        # Condition when I have enough LISC
        if not self.isMinimumGolemPartsMet():
            if self.getHUDItemCount('let_it_snow_trinket') > 2:                
                if not self.getCurrentCheese() == "Gouda Cheese":
                    self.setTrap({'bait': 'gouda_cheese'})
                    eprint("GWH", f"{self.name}: Insufficient Golem parts and enough LISC, armed Gouda")
                if not self.getCurrentCharm() == "Let It Snow Charm":
                    self.setTrap({'trinket': "let_it_snow_trinket"})
                    eprint("GWH", f"{self.name}: Insufficient Golem parts and enough LISC, armed LISC")

            # Condition when I do not have enough LISC, hunt using glazed pecan pericano instead
            elif self.getHUDItemCount('glazed_pecan_pecorino_cheese') > 2:
                if not self.getCurrentCheese() == "Glazed Pecan Pecorino Cheese":
                    self.setTrap({'bait': 'glazed_pecan_pecorino_cheese'})
                    eprint("GWH", f"{self.name}: Insufficient Golem parts and not enough LISC, using GPP to hunt")

            # Condition when I do not have enough LISC and GPP, hunt using pecan pericano instead
            elif self.getHUDItemCount('pecan_pecorino_cheese') > 2:
                if not self.getCurrentCheese() == "Pecan Pecorino Cheese":
                    self.setTrap({'bait': 'pecan_pecorino_cheese'})
                    eprint("GWH", f"{self.name}: Insufficient Golem parts and not enough LISC/GPP, using PP to hunt")

            # When i'm poor, using SB+
            else:
                if not self.getCurrentCheese() == "Gouda Cheese":
                    self.setTrap({'bait': 'gouda_cheese'})

            return

    def automateHunt(self, envs):
        if not self.isAtCurrentLocation():
            return

        # if self.isArmingPecanCheese():
        #     if self.getCurrentCheeseQuantity() < 3:
        #         self.setSuperBrie() 

        # getting golem status
        for i in range(3):
            if self.isGolemReadyToClaim(i):
                self.claimReward(i)
                eprint("GWH", f"{self.name}: Claim Reward from golem {i+1}")
                self.buildGolem(i, envs[i]['env'], envs[i]['has_hat'])
                eprint("GWH", f"{self.name}: Build golem {i+1}")

        # self.determineCharm()
        # self.checkAndJoinTournament()

        return
