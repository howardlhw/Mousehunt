from questLocations.api import api_userData, api_call, api_changeTrap, api_usePotion
from questLocations.bwrift_trapSetup import trapSetup
from util import eprint
from random import randint
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
        currentPortals = self.getCurrentPortals()

        if 'closed' in currentPortals and len(list(set(currentPortals))) == 1:
            return False
        return True

    # Getters
    def getCurrentPortals(self):
        return [
            portal['type']
            for portal in self.data['user']['quests'][self.quest]['portals']
        ]

    def getItemsCount(self, itemName):
        return self.data['user']['quests'][
            self.quest]['items'][itemName]['quantity']

    def getItemIsActiveStatus(self, itemName):
        status = ['selected']
        return self.data['user']['quests'][
            self.quest]['items'][itemName]['status'] in status

    def getStatusEffects(self):
        return self.data['user']['quests'][self.quest]['status_effects']

    def getQuantumQuartsStatus(self):
        if self.data['user']['quests'][self.quest]['items'][
                'rift_quantum_quartz_stat_item']['status'] == 'selected':
            return True
        return False

    def getObeliskCharge(self):
        return self.data['user']['quests'][self.quest]['obelisk_percent']

    # Setters
    def setData(self, data):
        self.data = data

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
        potion_chamber : Ancient Laboratory
        timewarp_chamber: Timewarp Chamber
        ?????? : Guard barracks
        ?????? : Paladin
        ?????? : Hidden Treasury
        lucky_chamber : Lucky Tower

        Useless Chambers
        icy_chamber: Frozen Alcove
        ingress_chamber: Ingress Chamber
        basic_chamber: Gearworks
        
        """
        self.request_body['action'] = 'enter_portal'
        self.request_body['portal_type'] = portalName
        # eprint('Bristle Woods Rift', f'Entering {portalName}')
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
        10. Enter the tower
        11. Never bother to enter ingress chamber

        returns the name of the chamber
        """

        portals = self.getCurrentPortals()
        eprint('Bristle Woods Rift', portals)

        aa_sand_threshold = 50  # For entering acolyate chamber
        sand_threshold_upper = 55  # uppeer sand threshold and stop entering timewarp
        runic_threshold = aa_sand_threshold  # For entering acolyate chamber
        ancient_threshold_lower = 60
        runic_upper_threshold = 70
        timewramp_runicRqd_thresdhold = 30

        # Banished chambers
        if 'ingress_chamber' in portals:
            portals.remove('ingress_chamber')

        if 'basic_chamber' in portals:
            portals.remove('basic_chamber')

        # Condition 1s - Always enter
        if 'guard_chamber' in portals:
            eprint('Bristle Woods Rift', 'Entering Guard Barracks')
            return 'guard_chamber'

        # Condition 1s - Always enter
        if 'silence_chamber' in portals:
            eprint('Bristle Woods Rift', 'Entering Silence Chamber')
            return 'silence_chamber'

        # Condition 1s - Always enter
        if 'security_chamber' in portals:
            eprint('Bristle Woods Rift', 'Entering Security Chamber')
            return 'security_chamber'

        # Condition - Enter Acolyte chamber if all conditions are met
        if self.getItemsCount('rift_hourglass_sand_stat_item') > aa_sand_threshold and \
            self.getItemsCount('runic_string_cheese') > runic_threshold and \
                self.getStatusEffects()['ng'] == 'active' and \
                    'acolyte_chamber' in portals:

            eprint('Bristle Woods Rift',
                   'Acolyte Condiiton met, entering chamber')
            return 'acolyte_chamber'

        # Condition - Gather enough hourglass sand
        if 'timewarp_chamber' in portals and \
            self.getItemsCount('rift_hourglass_sand_stat_item') <= aa_sand_threshold and \
                self.getItemsCount('runic_string_cheese') > timewramp_runicRqd_thresdhold:

            eprint('Bristle Woods Rift', 'Gathering hourglass sand...')
            return 'timewarp_chamber'

        # Condition - Don't get into timewarp if not enough runic cheese
        if 'timewarp_chamber' in portals and \
            self.getItemsCount('rift_hourglass_sand_stat_item') > aa_sand_threshold:
            eprint('Bristle Woods Rift',
                   'Removing timewarp due to insufficient runic cheese')
            portals.remove('timewarp_chamber')

        # Condition - Get runic string cheese, but not too much
        if 'magic_chamber' in portals and \
            self.getItemsCount('runic_string_cheese') <= runic_upper_threshold:
            eprint('Bristle Woods Rift', 'Gathering Runic cheese...')
            return 'magic_chamber'

        # # Condition - Get enough ancient string cheese
        if 'potion_chamber' in portals and \
            self.getItemsCount('ancient_string_cheese') <= ancient_threshold_lower:
            eprint('Bristle Woods Rift', 'Gathering Ancient String Cheese...')
            return 'potion_chamber'

        # Condition - whatever
        if 'lucky_chamber' in portals:
            eprint('Bristle Woods Rift', 'Entering Lucky Chamber')
            return 'lucky_chamber'

        # Condition - whatever
        if 'treasury_chamber' in portals:
            eprint('Bristle Woods Rift', 'Entering Treasury Chamber')
            return 'treasury_chamber'

        if 'magic_chamber' in portals and 'potion_chamber' in portals:
            self.getItemsCount('runic_string_cheese') > runic_upper_threshold
            eprint(
                'Bristle Woods Rift',
                'Gathering Ancient String Cheese due to excessive runic cheese'
            )
            return 'magic_chamber'

        if 'potion_chamber' in portals:
            eprint('Bristle Woods Rift', 'Gathering Ancient String Cheese....')
            return 'potion_chamber'

        if 'magic_chamber' in portals:
            eprint('Bristle Woods Rift', 'Gathering Runic Cheese....')
            return 'magic_chamber'

        # Condition 9
        if 'entrance_chamber' in portals:
            eprint('Bristle Woods Rift', 'Starting the loop again....')
            return 'basic_chamber'

        eprint('Bristle Woods Rift',
               f'No Suitable portal, selecting the first portal')
        return portals[0]

    # Togglers
    def toggleQuantumQuarts(self):
        self.request_body['action'] = 'toggle_loot_boost'
        return api_call(self.URL, self.request_cookies, self.request_body)

    def scramblePortal(self):
        self.request_body['action'] = 'scramble_portals'
        return api_call(self.URL, self.request_cookies, self.request_body)

    # Common Actions
    def chamberSetup(self, setup):
        if setup['quantumQuarts'] and not self.getItemIsActiveStatus(
                'rift_quantum_quartz_stat_item'):
            self.toggleQuantumQuarts()
        if not setup['quantumQuarts'] and self.getItemIsActiveStatus(
                'rift_quantum_quartz_stat_item'):
            self.toggleQuantumQuarts()

        self.setTrap({'bait': setup['bait']})
        self.setTrap({'trinket': setup['trinket']})
        eprint('Bristle Woods Rift', f'Changed Setup')

    def convertPotionToCheese(self, potion, quantity):
        settings = {
            'potion': potion,
            'num_potions': quantity,
            'recipe_index': 0
        }
        api_usePotion(self.request_cookies, {**self.request_body, **settings})
        eprint('Bristle Woods Rift', f'Converted {quantity} {potion}')

    # Main Automation
    def automateHunt(self):
        sandCount = ''

        if not self.isAtCurrentLocation():
            # eprint('Bristle Woods Rift', 'User not at current location')
            return

        # Brew the potions, if any
        if self.getItemsCount('ancient_string_cheese_potion') > randint(6, 10):
            self.convertPotionToCheese(
                'ancient_string_cheese_potion',
                self.getItemsCount('ancient_string_cheese_potion'))
        if self.getItemsCount('runic_string_cheese_potion') > randint(4, 10):
            self.convertPotionToCheese(
                'runic_string_cheese_potion',
                self.getItemsCount('runic_string_cheese_potion'))

        # Toggle for the case at acolyte chamber
        if self.getObeliskCharge() == 100 and self.getQuantumQuartsStatus():
            self.toggleQuantumQuarts()
            self.setTrap({'trinket': 'rift_trinkey'})
            eprint('Bristle Woods Rift',
                   'Obelisk fully charged, disable Quantum Quarts.')

        # End loop if portals are closed
        if not self.isPortalsOpened():
            return

        # Select the portal and enter the chamber, then change trap setup
        determinedPortal = self.determineChamberToEnter()
        if determinedPortal == None:
            return

        if determinedPortal == 'acolyte_chamber':
            sandCount += 'with sandCount ' + str(
                self.getItemsCount("rift_hourglass_sand_stat_item"))
        eprint('Bristle Woods Rift',
               f'Entering {determinedPortal} {sandCount}')
        self.selectChamber(determinedPortal)
        self.chamberSetup(trapSetup[determinedPortal])
