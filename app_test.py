from questLocations.bwrift import Bwrift
from questLocations.bwrift_trapSetup import trapSetup
from test.test_bwrift_data import test_data, portal_test_cases
import unittest


# Setting up test environment
howard = {
    "HG_TOKEN":
    "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y",
    "uh": "RdQtaaE8"
}

mh_bwrift = Bwrift(howard)
mh_bwrift.setData(test_data)

def setCurrentPortals(testObject, portals):
    # print(testObject.data['user']['quests']['QuestRiftBristleWoods']['portals'])
    for newPortal, oldPortal in zip(portals, testObject.data['user']['quests']['QuestRiftBristleWoods']['portals']):
        oldPortal['type'] = newPortal
    # print(testObject.data['user']['quests']['QuestRiftBristleWoods']['portals'])

def setItemQuantity(testObject, itemName, quantity):
    testObject.data['user']['quests']['QuestRiftBristleWoods']['items'][itemName]['quantity'] = quantity

class BWRift(unittest.TestCase):

    def test_determineChamberToEnter(self):
        for case in portal_test_cases:
            setCurrentPortals(mh_bwrift, portal_test_cases[case]['portals'])
            setItemQuantity(mh_bwrift, 'runic_string_cheese', portal_test_cases[case]['runic_string_cheese'])
            setItemQuantity(mh_bwrift, 'rift_hourglass_sand_stat_item', portal_test_cases[case]['rift_hourglass_sand_stat_item'])
            self.assertEqual(mh_bwrift.determineChamberToEnter(), portal_test_cases[case]['selection'])
            print(f'PASS: {case}')


if __name__ == '__main__':
    unittest.main()
