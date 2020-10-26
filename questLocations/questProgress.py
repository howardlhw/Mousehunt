from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion
from util import eprint
from random import randint
import time

headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Fetch-Dest": "empty",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors"
        }

class Quest():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/users/questsprogress.php"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_call(self.URL, cookies=self.request_cookies, body=self.request_body)



    def getQuestSuccessStatus(self):
        return self.data['progress']['zurreal_trap_research_quest_item']['progress'][2]['percentage'] == 100

    def setTravelDestination(self, destination):
        URL = 'https://www.mousehuntgame.com/managers/ajax/users/changeenvironment.php'
        self.request_body['destination'] = destination
        return api_call(URL, self.request_cookies, self.request_body)

    def setTrap(self, settings):
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})

    # Main Automation
    def automateHunt(self):
        self.setTrap({'weapon': 'upgraded_rune_shark_weapon'})
        self.setTrap({'bait': 'gnarled_cheese'})
        self.setTravelDestination('lagoon')
