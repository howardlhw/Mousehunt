from questLocations.api import api_userData, api_call
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


    def setToggleChampionFire(self):
        floor = self.data['user']['quests']['QuestRiftValour']['floor']
        at_eclipse = self.data['user']['quests']['QuestRiftValour']['is_at_eclipse']
        fuel_enabled = self.data['user']['quests']['QuestRiftValour']['is_fuel_enabled']
        eprint('Valor Rift', "floor: %s, atEclipse: %s, fuelEnabled: %s"%(floor, at_eclipse, fuel_enabled))

        # CF Toggle determination
        if at_eclipse and not fuel_enabled:
            return True
        if not at_eclipse and fuel_enabled:
            return True

        return False

    def automateHunt(self):
        if not self.isAtCurrentLocation():
            eprint('Valor Rift', 'User not at current location')
            return

        if self.setToggleChampionFire():
            self.toggleChampionFire()
            eprint('Valor Rift', 'Toggled Champion Fire')
            return

        return
        