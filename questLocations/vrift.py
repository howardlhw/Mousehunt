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

    def getCurrentStep(self):
        return self.data['user']['quests']['QuestRiftValour']['current_step']

    def getFloorPresige(self):
        return self.data['user']['quests']['QuestRiftValour']['prestige']

    def getSpeed(self):
        return self.data['user']['quests']['QuestRiftValour']['power_up_data'][
            'long_stride']['current_value']

    def getCFStatus(self):
        return self.data['user']['quests']['QuestRiftValour'][
            'is_fuel_enabled']

    def enableCF(self):
        if not self.getCFStatus():
            eprint("Valour Rift", "Enable Champion fire at floor %s"%(self.getFloorLevel()))
            self.toggleChampionFire()

    def disableCF(self):
        if self.getCFStatus():
            eprint("Valour Rift", "Disable Champion fire at floor %s"%(self.getFloorLevel()))
            self.toggleChampionFire()

    def getStepToEclipse(self):
        if self.getFloorPresige() == 1:
            return 140
        if self.getFloorPresige() == 2:
            return 351
        if self.getFloorPresige() == 3:
            return 632
        if self.getFloorPresige() == 4:
            return 983
        if self.getFloorPresige() == 5:
            return 1404
        if self.getFloorPresige() == 6:
            return 1895
        if self.getFloorPresige() == 7:
            return 2456
        if self.getFloorPresige() == 8:
            return 3087
        if self.getFloorPresige() == 9:
            return 3788
        if self.getFloorPresige() == 10:
            return 4559
        if self.getFloorPresige() == 11:
            return 5400
        if self.getFloorPresige() == 12:
            return 6311

    def getCountOfCFToUse(self):
        return (self.getStepToEclipse() -
                self.getCurrentStep()) % self.getSpeed()

    def getCurrentTrinket(self):
        return self.data['user']['trinket_name']

    def determineAndSetTrap(self):
        # floor = self.data['user']['quests']['QuestRiftValour']['floor']
        at_eclipse = self.data['user']['quests']['QuestRiftValour'][
            'is_at_eclipse']

        if at_eclipse:
            # eprint('Valour Rift', "floor: %s, atEclipse: %s" %(self.getFloor(), at_eclipse))
            self.setEclipseTrap()
        else:
            self.setNormalTrap()

    def setEclipseTrap(self):
        if self.getCurrentTrinket() != 'Rift 2020 Charm':
            eprint('Valour Rift', f'Changing trinket to Rift 2020 Charm')
            self.setTrap({'trinket': "rift_2020_trinket"})
            
    def setNormalTrap(self):
        if self.getCurrentTrinket() != 'Rift Spooky Charm':
            eprint('Valour Rift', f'Changing trinket to Rift Spooky Charm')
            self.setTrap({'trinket': "rift_spooky_trinket"})

    def getFloor(self):
        return self.data['user']['quests']['QuestRiftValour']['floor']

    def setTrap(self, settings):
        res = api_changeTrap(self.request_cookies, {
            **self.request_body,
            **settings
        })

    def automateHunt(self):
        if not self.isAtCurrentLocation():
            return

        # Champion fire treatments
        if self.getFloorLevel() > 10 :
            self.enableCF()
        elif self.getFloorLevel()%8 == 0:
            self.enableCF()
        elif 0 < self.getCountOfCFToUse() < 5:
            self.enableCF()
        else:
            self.disableCF()

        # Trap treatment
        self.determineAndSetTrap()

        return
