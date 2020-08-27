from questLocations.api import api_userData, api_call
from util import eprint, debug
import time

class Labyrinth():
    def __init__(self, request_acc, debug=False):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/environment/labyrinth.php"
        self.quest = "QuestLabyrinth"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData(self.request_cookies)
        self.debug = debug

    def isAtCurrentLocation(self):
        if self.data['user']['quests'].get(self.quest) != None:
            return True
        return False


    def getCurrentDoors(self):
        return [door['choice'] for door in self.data['user']['quests']['QuestLabyrinth']['doors']]


    def checkDesiredDoors(self, doors_preference):
        # y = plain fealty, s = plain scholar, h = plain tech
        # y2 = superior fealty, s2 = superior scholar, h2 = superior tech
        # y3??
        # s = short, m = medium, l = long

        self.data = api_userData(self.request_cookies)

        for preference in doors_preference:
            if preference in self.getCurrentDoors():
                self.chosenDoor = preference
                debug(f'Chosen: {preference}', self.debug)
                return True

        debug(f'Chosen None', self.debug)
        return False

    def enterSelectedDoor(self, choice):
        self.request_body['action'] = 'make_intersection_choice'
        self.request_body['choice'] = choice
        return api_call(self.URL, self.request_cookies, self.request_body)

    
    def scrambleDoor(self):
        self.request_body['action'] = 'scramble_intersections'
        return api_call(self.URL, self.request_cookies, self.request_body)


    def automateHunt(self, doorPreferences):
        if not self.isAtCurrentLocation():
            eprint('Labyrinth', 'User not at current location')
            return

        # Check if the doors are opened
        if len(list(set(self.getCurrentDoors())))==1 and list(set(self.getCurrentDoors()))[0] == None:
            # eprint('Labyrinth', 'Doors closed')
            return 

        # Commence loop to scramble door until the preferred door is available
        while(True):
            # Scarmble door if no preferred door
            if self.checkDesiredDoors(doorPreferences):
                eprint('Labyrinth', f'Found door, door is {self.chosenDoor}')
                break

            self.scrambleDoor()
            eprint('Labyrinth', 'Preferred door not available, scrambled door')
            time.sleep(30)

        eprint('Labyrinth', f'Entering door [{self.chosenDoor}]')
        self.enterSelectedDoor(self.chosenDoor)
        return
        