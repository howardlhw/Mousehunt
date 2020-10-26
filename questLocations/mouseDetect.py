from questLocations.api import api_userData, api_call
from util import eprint, debug
import time

class MouseDetect():
    def __init__(self, request_acc, debug=False):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/pages/page.php"
        self.request_cookies = {
            "HG_TOKEN": request_acc['HG_TOKEN'],
            "has_logged_in": 'true',
            "hg_session[startTime]": '1599402471',
            "hg_session[sessionId]": '8EyVDqM80KbW1JQXHA7VoYtXH86U7s42',
            "hg_session[sessionNum]":'1303'
            }
        self.request_body = {
            "uh": request_acc['uh'], 
            'sn': 'Hitgrab',
            'hg_is_ajax': '1',
            'last_read_journal_entry_id': 91271,
            'page_class': "Camp"}
        self.data = api_userData(self.request_cookies)
        self.debug = debug

    def getLatestMouse(self):
        return self.data['error_message']
        return self.data['page']['journals'][0]

    def automateHunt(self):
        pass
