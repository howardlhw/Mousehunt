import requests, time

headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Fetch-Dest": "empty",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors"
        }


def mainPageData(cookies):    
    body = {
            }
    
    URL = "https://www.mousehuntgame.com/managers/ajax/pages/page.php"
    res = requests.post(URL, headers=headers, cookies=cookies, json=body)
    return res.json()
    

def toggleCF(cookies, body):    
        
    URL = "https://www.mousehuntgame.com/managers/ajax/environment/rift_valour.php"
    res = requests.post(URL, headers=headers, cookies=cookies, data=body).json()
        
    return res



def api_labyrinth(cookies, body):    
    URL = "https://www.mousehuntgame.com/managers/ajax/environment/labyrinth.php"
    res = requests.post(URL, headers=headers, cookies=cookies, data=body).json()
        
    return res
