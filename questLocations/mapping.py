from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion, api_userData_body
from questLocations.mapping_trapSetup import loadout_setting, mouseCatchSequence, trapSetup, trapSetup_main, mouseCatchSequence_chrome, mouseCatchSequence_qcgt
from util import eprint
from random import randint
import time


class Mapping():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/users/treasuremap.php"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData_body(self.request_cookies, {"uh": request_acc['uh'], "page_class":"Camp"})    
        self.map_id = self.getMapID()
        self.map_data = self.getMapData()

    def getMapID(self):
        try:
            return self.data['user']['quests']['QuestRelicHunter']['maps'][0][
                'map_id']
        except:
            return None

    def getUserID(self):
        return self.data['user']['user_id']

    def getUserTrap(self):
        if self.getUserID() == 8053208:
            return trapSetup_main

        if self.getUserID() == 8076594:
            return trapSetup

    def getMouseSequence(self):
        if self.getmapName() == 'Queso Canyon Grand Tour Treasure Map':
            return mouseCatchSequence_qcgt

        if self.getmapName() == 'Arduous Chrome Treasure Map':
            return mouseCatchSequence_chrome

        return mouseCatchSequence

    def getmapName(self):
        return self.map_data['treasure_map']['name']

    def getMapData(self):
        self.request_body['action'] = 'map_info'
        self.request_body['map_id'] = self.map_id
        return api_call(self.URL, self.request_cookies, self.request_body)

    def getCurrentLocation(self):
        return self.data['user']['environment_type']

    def getCurrentSetup(self, item):
        # item  == base, weapon, or bait
        try:
            return self.data['page']['layers'][item]['type']
        except:
            return None
        

    def getAllMiceOnMap(self):
        return {
            mouse['name']: mouse
            for mouse in self.map_data['treasure_map']['goals']['mouse']
        }

    def getOneMouseOnMap(self, mouse):
        return self.getAllMiceOnMap().get(mouse)

    def getMouseWeakness(self, mouse):
        for effectiveness in self.getOneMouseOnMap(mouse)['weaknesses']:
            if len(effectiveness['power_types']) != 0:
                return effectiveness['power_types'][0]['name']

    def getMouseLocationId(self, mouse):
        return self.getOneMouseOnMap(mouse)['environment_ids'][0]

    def getLocationName(self, environment_id):
        for environment in self.map_data['treasure_map']['environments']:
            if environment['id'] == environment_id:
                return environment['type']

    def getAllCaughtMouseIDs(self):
        caughtMouseID = []
        for hunter in self.map_data['treasure_map']['hunters']:
            caughtMouseID += hunter['completed_goal_ids']['mouse']
        return caughtMouseID

    def checkIfHasMouse(self, mouse):
        if self.getOneMouseOnMap(mouse) == None:
            return False
        if self.getOneMouseOnMap(
                mouse)['unique_id'] in self.getAllCaughtMouseIDs():
            return False
        return True

    def getCurrentTrinket(self):
        return self.data['user']['trinket_name']

    def setTravelDestination(self, destination):
        URL = 'https://www.mousehuntgame.com/managers/ajax/users/changeenvironment.php'
        self.request_body['destination'] = destination
        return api_call(URL, self.request_cookies, self.request_body)

    def setTrap(self, settings):
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})

    def moveToStationaryHunting(self):
        # loadout = None
        if self.getUserID() == 8053208:
            loadout = loadout_setting.get('vrift')
        if self.getUserID() == 8076594:
            loadout = loadout_setting.get('mopi')
        else:
            loadout = None

        if loadout == None:
            return

        if self.getCurrentLocation() != loadout['environment']:
            eprint('Mapping', f'Moving to {loadout["environment"]}')
            self.setTravelDestination(loadout['environment'])

        if self.getCurrentSetup('weapon') != loadout["weapon"]:
            eprint('Mapping', f'Changing trap to {loadout["weapon"]}')
            self.setTrap({'weapon': loadout["weapon"]})

        if self.getCurrentSetup('bait') != loadout["bait"]:
            eprint('Mapping', f'Changing bait to {loadout["bait"]}')
            self.setTrap({'bait': loadout["bait"]})

        if self.getCurrentTrinket() != loadout['trinket_name']:
            eprint('Mapping', f'Changing trinket to {loadout["trinket"]}')
            self.setTrap({'trinket': loadout["trinket"]})

    def getCurrentLocation(self):
        return self.data['user']['environment_type']

    def isAtCurrentLocation(self):
        if self.getmapName() == 'Queso Canyon Grand Tour Treasure Map':
            if not self.getCurrentLocation() in ['queso_river', 'queso_plains','queso_quarry', 'queso_geyser']:
                return False

        return True



    # Main Automation
    # Map ID can be found under quests /
    def automateHunt(self):
        if self.map_id == None:
            return

        # Location check for mapping
        if not self.isAtCurrentLocation():
            return

        # Get the curent list of mouse to be caught
        mouseList = self.getMouseSequence()

        # Get current target mouse
        for count, mouse in enumerate(mouseList):
            # Do not hunt if the current bait is flaming queso
            if self.getCurrentSetup('bait') == 'flaming_queso_cheese':
                if self.getCurrentLocation() in ['queso_plains','queso_quarry']:
                    return

            # Check if the mouse has been caught, if yes, move on to next loop
            if not self.checkIfHasMouse(mouse['name']):
                # Ending the loop
                if count == len(mouseList) -1 :
                    self.moveToStationaryHunting()
                    return
                    
                continue

            # Get the name of the mouse location
            target_location = self.getLocationName(self.getMouseLocationId(mouse['name']))
            if self.getCurrentLocation() != target_location:
                self.setTravelDestination(target_location)
                eprint('Mapping', f'Moving to {target_location}')

            # Get current equipped trap, and see if there is a need to change.
            trapSetup = self.getUserTrap()

            # Get current equipped trap, and see if there is a need to change.
            target_trap = trapSetup[self.getMouseWeakness(mouse["name"])]["weapon"]
            if self.getCurrentSetup('weapon') != target_trap:
                eprint('Mapping', f'Changing trap to {target_trap}')
                self.setTrap({'weapon':target_trap})

            # Get current equipped trap, and see if there is a need to change.
            target_bait = mouse['bait']
            if self.getCurrentSetup('bait') != target_bait:
                self.setTrap({'bait': target_bait})
                eprint('Mapping', f'Changing bait to {target_bait}')

            return
