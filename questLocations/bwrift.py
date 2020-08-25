from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion
from questLocations.bwrift_trapSetup import trapSetup
from util import eprint
import time


class Bwrift():
    def __init__(self, request_acc):
        self.URL = "https://www.mousehuntgame.com/managers/ajax/environment/rift_bristle_woods.php"
        self.quest = "QuestRiftBristleWoods"
        self.request_cookies = {"HG_TOKEN": request_acc['HG_TOKEN']}
        self.request_body = {"uh": request_acc['uh']}
        self.data = api_userData(self.request_cookies)

        # Customize settings
        self.usePortalScrambler = False

    # Boolean checkers
    def isAtCurrentLocation(self):
        if self.data['user']['quests'].get(self.quest) != None:
            return True
        return False

    def isPortalsOpened(self):
        if list(set(self.getCurrentPortals()))[0] == "closed":
            return False
        return True

    # Getters
    def getCurrentPortals(self):
        return [
            portal['type']
            for portal in self.data['user']['quests'][self.quest]['portals']
        ]

    def getItemsCount(self, itemName):
        return self.data['user']['quests'][self.quest]['items'][itemName]['quantity']

    def getItemIsActiveStatus(self, itemName):
        status = ['selected']
        return self.data['user']['quests'][self.quest]['items'][itemName]['status'] in status

    def getStatusEffects(self):
        return self.data['user']['quests'][self.quest]['status_effects']

    def getQuantumQuartsStatus(self):
        return self.data['user']['quests'][self.quest]['status_effects']

    # Setters
    def setTrap(self, settings):
        """
        Cheese Options (bait)
        brie_string_cheese
        runic_string_cheese
        ancient_string_cheese

        Charm Options (trinket)
        rift_vacuum_trinket
        super_rift_vacuum_trinket
        rift_trinket

        """
        api_changeTrap(self.request_cookies, {**self.request_body, **settings})

    def selectChamber(self, portalName):
        """
        Chamber Options
        acolyte_chamber: Acolyte Chamber
        magic_chamber: Runic Laboratory
        ?????? : Ancient Laboratory
        timewarp_chamber: Timewarp Chamber
        ?????? : Guard barracks
        ?????? : Paladin
        ?????? : Hidden Treasury
        ?????? : Lucky Tower

        Useless Chambers
        icy_chamber: Frozen Alcove
        ingress_chamber: Ingress Chamber
        basic_chamber: Gearworks
        
        """
        self.request_body['action'] = 'enter_portal'
        self.request_body['portal_type'] = portalName
        eprint('Bristle Woods Rift', f'Entering {portalName}')
        return api_call(self.URL, self.request_cookies, self.request_body)

    # Chamber condition setters
    def determineChamberToEnter(self):
        """
        This method determines the chamber to enter, the priorities are:
        1. Enter Security Chamber to disable alarm
        2. Enter Guard Barracks if the alarm was triggered
        3. Hidden Treasury for gold
        4. Then Lucky tower for loot
        5. Acolyte Chamber if conditions are met
        6. Timewarp chamber if conditions are met
        7. runic chamber if all else fails
        8. ancient chamber if oh well....
        9. Gear works, seriously?

        returns the name of the chamber
        """

        portals = self.getCurrentPortals()

        # Condition 1 (TODO)
        # if 'security_chamber' in chambers:
        #     return 'security_chamber'

        # Condition 2 (TODO)
        # if self.getStatusEffects()['un'] == 'active':
        #     return 'guard_barracks'

        # Condition 3
        if 'lucky_tower' in portals:
            return 'lucky_tower'

        # Condition 4
        if 'hidden_treasury' in portals:
            return 'hidden_treasury'

        # Condition 5
        if self.getItemsCount(
                'rift_hourglass_sand_stat_item') > 65 and self.getItemsCount(
                    'runic_string_cheese'
                ) > 65 and 'acolyte_chamber' in portals:
            return 'acolyte_chamber'

        # Condition 6
        if 'timewarp_chamber' in portals and self.getItemsCount(
                'rift_hourglass_sand_stat_item') < 70:
            return 'timewarp_chamber'

        # Condition 7
        if 'magic_chamber' in portals:
            return 'magic_chamber'

        # # Condition 8 (TODO)
        # if 'ancient_chamber' in portals:
        #     return 'ancient_chamber'
        eprint('Bristle Woods Rift', f'No Suitable portal')

        return None

    # Togglers
    def toggleQuantumQuarts(self):
        self.request_body['action'] = 'toggle_loot_boost'
        return api_call(self.URL, self.request_cookies, self.request_body)

    def scramblePortal(self):
        self.request_body['action'] = 'scramble_portals'
        return api_call(self.URL, self.request_cookies, self.request_body)

    # Common Actions
    def chamberSetup(self, setup):
        if setup['quantumQuarts'] and not self.getItemIsActiveStatus('rift_quantum_quartz_stat_item'):
            self.toggleQuantumQuarts()
        if not setup['quantumQuarts'] and self.getItemIsActiveStatus('rift_quantum_quartz_stat_item'):
            self.toggleQuantumQuarts()

        self.setTrap({'bait': setup['bait']})
        self.setTrap({'trinket': setup['trinket']})
        eprint('Bristle Woods Rift', f'Changed Setup')

    def convertPotionToCheese(self, potion, quantity):
        settings = {'potion': potion, 'num_potions': quantity, 'recipe_index': 0}
        api_usePotion(self.request_cookies, {**self.request_body, **settings})
        eprint('Bristle Woods Rift', f'Converted {quantity} {potion}')

    # Main Automation
    def automateHunt(self):
        if not self.isAtCurrentLocation():
            eprint('Bristle Woods Rift', 'User not at current location')
            return

        # Brew the potions, if any
        if self.getItemsCount('ancient_string_cheese_potion') > 0:
            self.convertPotionToCheese('ancient_string_cheese_potion', self.getItemsCount('ancient_string_cheese_potion'))
        if self.getItemsCount('runic_string_cheese_potion') > 0:
            self.convertPotionToCheese('runic_string_cheese_potion', self.getItemsCount('runic_string_cheese_potion'))

        # End loop if portals are closed
        if not self.isPortalsOpened():
            eprint('Bristle Woods Rift', 'Portals are not opened')
            return

        # Select the portal and enter the chamber, then change trap setup
        determinedPortal = self.determineChamberToEnter()
        if determinedPortal == None:
            return
        self.selectChamber(determinedPortal)
        self.chamberSetup(trapSetup[determinedPortal])
