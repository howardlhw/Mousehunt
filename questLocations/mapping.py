from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion
from questLocations.mapping_trapSetup import mouseCatchSequence
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
        return {mouse['name']: mouse['unique_id'] for mouse in self.map_data['treasure_map']['goals']['mouse']}

    def getAllCaughtMouseIDs(self):
        caughtMouseID = []
        for hunter in self.map_data['treasure_map']['hunters']:
            caughtMouseID += hunter['completed_goal_ids']['mouse']
        return caughtMouseID

    def checkIfHasMouse(self, mouse):
        if self.getAllMiceOnMap().get(mouse) == None:
            return False
        if self.getAllMiceOnMap().get(mouse) in self.getAllCaughtMouseIDs():
            return False
        return True

    def setTravelDestination(self, destination):
        URL = 'https://www.mousehuntgame.com/managers/ajax/users/changeenvironment.php'
        self.request_body['destination'] = destination
        return api_call(URL, self.request_cookies, self.request_body)

    def setTrap(self, settings):
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})

    # def setTrapSetup(self, setup):
    #     print(setup)
    #     self.setTrap({'weapon': setup['weapon']})
    #     self.setTrap({'bait': setup['bait']})


    # Main Automation
    def automateHunt(self):
        # Get current target mouse
        
        for mouse in mouseCatchSequence:
            # Check if the mouse has been count, if yes, move on
            if not self.checkIfHasMouse(mouse['name']):
                continue

            # eprint('Mapping', f'Hunting {mouse["name"]}')
            
            # Check if the current location is corrent, if yes, means we have been catching there
            # Then move on
            if self.getCurrentLocation() == mouse['destination']:
                return


            # Time to catch the next mouse
            # Travel to the destination and setup trap
            eprint('Mapping', f'Mouse target is {mouse["name"]}')
            self.setTravelDestination(mouse['destination'])
            eprint('Mapping', f'Moving to {mouse["destination"]}')
            self.setTrap({'weapon': mouse['setup']['weapon']})
            self.setTrap({'bait': mouse['bait']})
            eprint('Mapping', f'Changing trap to {mouse["setup"]["weapon"]}')
            return