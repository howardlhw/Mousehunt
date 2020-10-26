import requests

headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Fetch-Dest": "empty",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors"
        }


def api_call(URL, cookies, body):
    return requests.post(URL, headers=headers, cookies=cookies, data=body).json()

def api_changeTrap(cookies, body):
    URL = "https://www.mousehuntgame.com/managers/ajax/users/changetrap.php"
    return requests.post(URL, headers=headers, cookies=cookies, data=body).json()

def api_userData(cookies):    
    URL = "https://www.mousehuntgame.com/managers/ajax/pages/page.php"
    return requests.post(URL, headers=headers, cookies=cookies).json()

def api_usePotion(cookies, body):
    URL = "https://www.mousehuntgame.com/managers/ajax/users/usepotion.php"
    return requests.post(URL, headers=headers, cookies=cookies, data=body).json()

