import time, datetime
from random import randint
from util import toggleCF, mainPageData, api_labyrinth

cookies_howard = {
            "hg_session[sessionId]": "XW8CIN0wIUUhuE3A65GWJdCm2E473E20",
            "HG_TOKEN": "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y"
            }

body_howard = {
        "uh": "RdQtaaE8",
        }


cookies_acc1 = {
            "hg_session[sessionId]": "AETPxdJdk436jOgTE06P577va4lCBmJ5",
            "HG_TOKEN": "72wdLJWpIogUFJ912jQQf6TmcvbgmdM79Y6n094N155aM5BdWHHNmWFL79wS55ly",
            "bb_sessionhash": "AETPxdJdk436jOgTE06P577va4lCBmJ5"
            }

body_acc1 = {
        "uh": "LeA1Z1B4"
        }


cookies_acc2 = {
            # "hg_session[sessionId]": "AETPxdJdk436jOgTE06P577va4lCBmJ5",
            "HG_TOKEN": "wI4Q2y0uk4TK1yifrR33vZw9Vq1FkZs73PD22VMSQ600HtOu1f5bn0s6L240278w",
            "bb_sessionhash": "0dcaf65baddc3772685ac7cda0d5d9e2",
            }

body_acc2 = {
        "uh": "Gc112MbD"
        }

def eprint(location, message):
    t = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"[{t}] {location}: {message}")

def check_at_eclipse():
    a0 = mainPageData(cookies_howard)
    floor = a0['user']['quests']['QuestRiftValour']['floor']
    at_eclipse = a0['user']['quests']['QuestRiftValour']['is_at_eclipse']
    fuel_enabled = a0['user']['quests']['QuestRiftValour']['is_fuel_enabled']
    eprint('Valor Rift', "floor: %s, eclipse?: %s, fuel_enabled: %s"%(floor, at_eclipse, fuel_enabled))
    
    # CF Toggle determination
    if at_eclipse and not fuel_enabled:
        return True
    if not at_eclipse and fuel_enabled:
        return True
    
    return False


def valorRift(request_cookies, request_body):
    
    if check_at_eclipse():
        eprint('Valour Rift', 'Toggled CF')
        request_body['action'] = 'toggle_fuel'
        toggleCF(request_cookies, request_body)
    
# def bwrift():
#     a0 = mainPageData(cookies_acc1)
#     quests = a0['user']['quests']
#     bwrift = a0['user']['quests']['QuestRiftBristleWoods']
#     time_remaining = a0['user']['quests']['QuestRiftBristleWoods']['progress_remaining']
#     portal = a0['user']['quests']['QuestRiftBristleWoods']['portals']
#     chamber_status = a0['user']['quests']['QuestRiftBristleWoods']['chamber_status']
#     acolyte_sand = a0['user']['quests']['QuestRiftBristleWoods']['acolyte_sand']
#     sand_quantity = a0['user']['quests']['QuestRiftBristleWoods']['items']['rift_hourglass_sand_stat_item']['quantity']
    
#     ancient_string_cheese = a0['user']['quests']['QuestRiftBristleWoods']['items']['ancient_string_cheese']['quantity']
#     runic_cheese = a0['user']['quests']['QuestRiftBristleWoods']['items']['runic_string_cheese']['quantity']
#     magical_string_cheese = a0['user']['quests']['QuestRiftBristleWoods']['items']['magical_string_cheese']['quantity']
    
#     paladin = a0['user']['quests']['QuestRiftBristleWoods']['status_effects']['ng']
#     remove_if_active = a0['user']['quests']['QuestRiftBristleWoods']['status_effects']['un']
#     chamber_name = a0['user']['quests']['QuestRiftBristleWoods']['chamber_name']
#     acolyte_status = a0['user']['quests']['QuestRiftBristleWoods']['minigame']['acolyte_chamber']['acolyte_status']
#     obelisk_percent = a0['user']['quests']['QuestRiftBristleWoods']['minigame']['acolyte_chamber']['obelisk_percent']
#     acolyte_sand = a0['user']['quests']['QuestRiftBristleWoods']['minigame']['acolyte_chamber']['acolyte_sand']

    
#     if portal[0]['type'] == "closed":
#         t = datetime.datetime.now()
#         print("[%s] status: chamber closed"%(t.strftime("%Y-%m-%d %H:%M:%S")))
#         # return
    
    
#     print(time_remaining) 
#     print(portal) # acolyte_chamber,  basic_chamber #Gearworks, potion_chamber #ancient lab
#     print(chamber_status)
#     print(acolyte_sand) # Time of acolyte, need to remove to zero at 100% charge
#     print(sand_quantity) # Current sand count, need to be 60 to be safe
#     print(paladin)
#     print(remove_if_active)
#     print(chamber_name)
#     print(acolyte_status)
#     print(obelisk_percent)
#     print(acolyte_sand)
#     print(ancient_string_cheese)
#     print(runic_cheese)
#     print(magical_string_cheese)
    
#     return a0

def labyrinth(request_cookie, request_body):

    a0 = mainPageData(request_cookie)
    door0 = a0['user']['quests']['QuestLabyrinth']['doors'][0]['choice']
    door1 = a0['user']['quests']['QuestLabyrinth']['doors'][1]['choice']
    door2 = a0['user']['quests']['QuestLabyrinth']['doors'][2]['choice']
    
    if door0 == None:
        eprint('Labyrinth', 'No hallway to enter')
        return False
    
    def checkDoor(doors):
        available_doors = []
        # y = plain fealty, s = plain scholar, h = plain tech
        # s = short, m = medium, l = long
        choices = ['yl', 'ym', 'ys'] # Select the choice of doors 
        for door in doors:
            if door in choices:
                available_doors.append(door)
                
                
        for choice in choices:
            if choice in available_doors:
                return choice
                
        return None
    
    # Check status of door
    selected_hallway = checkDoor([door0, door1, door2])
    
    if selected_hallway == None:
        # Scramble and wait for the next loop
        request_body['action'] ='scramble_intersections'
        api_labyrinth(request_cookie, request_body)
        eprint('Labyrinth', 'Scrambled Doors')
        return False
    
    eprint('Labyrinth', f'Entering Hallway {selected_hallway}')
    request_body['action'] ='make_intersection_choice'
    request_body['choice'] = selected_hallway
    
    res = api_labyrinth(request_cookie, request_body)
    return res
    
    

def runHornContinuously():
    count = 0
    while True:
        count += 1
        # valorRift(cookies_howard, body_howard)
        labyrinth(cookies_acc2, body_acc2)
        time.sleep(600)
        # break


if __name__ == "__main__":
    runHornContinuously()