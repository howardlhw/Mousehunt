from questLocations.api import api_userData, api_call, api_changeTrap
from util import eprint
import time


class Vrift():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/environment/rift_valour.php"
        self.quest = "QuestRiftValour"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData(self.request_cookies)

    def isAtCurrentLocation(self):
        if self.data['user']['quests'].get(self.quest) != None:
            return True
        return False

    def toggleChampionFire(self):
        self.request_body['action'] = 'toggle_fuel'
        return api_call(self.URL, self.request_cookies, self.request_body)

    def getFloorLevel(self):
        return self.data['user']['quests']['QuestRiftValour']['floor']

    def setToggleChampionFire(self):
        floor = self.data['user']['quests']['QuestRiftValour']['floor']
        at_eclipse = self.data['user']['quests']['QuestRiftValour'][
            'is_at_eclipse']
        fuel_enabled = self.data['user']['quests']['QuestRiftValour'][
            'is_fuel_enabled']

        # CF Toggle determination
        if at_eclipse and not fuel_enabled:
            eprint(
                'Valour Rift', "floor: %s, atEclipse: %s, fuelEnabled: %s" %
                (floor, at_eclipse, fuel_enabled))
            self.setShadeOFEclipseTrap()
            return True
        if not at_eclipse and fuel_enabled:
            eprint(
                'Valour Rift', "floor: %s, atEclipse: %s, fuelEnabled: %s" %
                (floor, at_eclipse, fuel_enabled))
            self.setNormalSetup()
            return True

        return False

    def setShadeOFEclipseTrap(self):
        self.setTrap({'trinket': 'rift_2020_trinket'})
        eprint('Valour Rift', 'Arming Eclipse Setup')

    def setNormalSetup(self):
        self.setTrap({'trinket': 'rift_snowball_trinket'})
        eprint('Valour Rift', 'Arming Climbing Setup')

    # def isAtEclipse(self):
    #     self.data['user']['quests']['QuestRiftValour']['is_at_eclipse']

    def getFloor(self):
        return self.data['user']['quests']['QuestRiftValour']['floor']

    def isFuelEnabled(self):
        return self.data['user']['quests']['QuestRiftValour'][
            'is_fuel_enabled']

    def setTrap(self, settings):
        res = api_changeTrap(self.request_cookies, {
            **self.request_body,
            **settings
        })

    def automateHunt(self):
        if not self.isAtCurrentLocation():
            return

        if self.getFloorLevel() > 24:
            if not self.isFuelEnabled():
                eprint('Valor Rift', 'Toggled Champion Fire')
                self.toggleChampionFire()
            return

        if self.setToggleChampionFire():
            self.toggleChampionFire()
            eprint('Valor Rift', 'Toggled Champion Fire')
            return

        return
