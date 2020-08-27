from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion
from questLocations.mapping_trapSetup import mouseCatchSequence, trapSetup
from util import eprint
from random import randint
import time


class Mapping():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/users/treasuremap.php"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData(self.request_cookies)

        if request_acc.get('map_id') == None:
            eprint('Mapping', 'Missing Map ID')
            raise Exception('Please ensure map Id is in the body')
        self.map_id = request_acc['map_id']
        self.map_data = self.getMapData()

    def getMapData(self):
        self.request_body['action'] = 'map_info'
        self.request_body['map_id'] = self.map_id
        return api_call(self.URL, self.request_cookies, self.request_body)

    def getCurrentLocation(self):
        return self.data['user']['environment_type']

    def getAllMiceOnMap(self):
        return {mouse['name']: mouse for mouse in self.map_data['treasure_map']['goals']['mouse']}

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
        if self.getOneMouseOnMap(mouse)['unique_id'] in self.getAllCaughtMouseIDs():
            return False
        return True

    def setTravelDestination(self, destination):
        URL = 'https://www.mousehuntgame.com/managers/ajax/users/changeenvironment.php'
        self.request_body['destination'] = destination
        return api_call(URL, self.request_cookies, self.request_body)

    def setTrap(self, settings):
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})


    # Main Automation
    def automateHunt(self):
        # Get current target mouse
        
        for mouse in mouseCatchSequence:
            # Check if the mouse has been caught, if yes, move on
            if not self.checkIfHasMouse(mouse['name']):
                continue
            
            # Check if the current location is corrent, if yes, means we have been catching there
            # Then move on
            target_location = self.getLocationName(self.getMouseLocationId(mouse['name']))
            if self.getCurrentLocation() == target_location:
                return
                
            # Time to catch the next mouse
            # Travel to the destination and setup trap
            eprint('Mapping', f'Mouse target is {mouse["name"]}')
            eprint("DEBUG (Weakness)", self.getMouseWeakness(mouse['name']))
            self.setTravelDestination(target_location)
            eprint('Mapping', f'Moving to {target_location}')
            self.setTrap({'weapon': trapSetup[self.getMouseWeakness(mouse["name"])]["weapon"]})
            self.setTrap({'bait': mouse['bait']})
            eprint('Mapping', f'Changing trap to {trapSetup[self.getMouseWeakness(mouse["name"])]["weapon"]}')
            return