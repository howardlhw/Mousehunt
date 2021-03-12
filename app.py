import time, datetime
from questLocations.labyrinth import Labyrinth
from questLocations.vrift import Vrift
from questLocations.bwrift import Bwrift
from questLocations.mapping import Mapping
from questLocations.questProgress import Quest
from questLocations.mouseDetect import MouseDetect
from questLocations.floatingislands import FloatingIslands
from questLocations.gwh import GWH
from random import randint
from util import eprint
import datetime, traceback

from questLocations.mapping_trapSetup import trapSetup, trapSetup_main


howard = {
    "HG_TOKEN": "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y",
    "uh": "54TYb49T",
    "name": "Main"
}

acc1 = {
    "HG_TOKEN": "ZNBwnUMC4iq22WXf7k5H2o238D5Q76VYfwro0wavTbDG3I4aQUIJU8T2EkQIqJ4s",
    "uh": "wfE8dqqp",
    "name": "Acc1"
}


def runHornContinuously():
    while True:
        try:
            # GWH Locations
            # floating_islands
            # ancient_city
            # rift_whisker_woods
            # desert_oasis
            # lost_city
            # moussu_picchu
            # zugzwang_tower
            # fungal_cavern
            # rift_valour

            # mh_vrift = Vrift(howard)
            # mh_vrift.automateHunt()

            # mh_labyrinth = Labyrinth(howard)
            # mh_labyrinth.automateHunt(['s3l','s3m','s3s','s2l', 's2m', 's2s'])

            # mh_gwh0 = GWH(howard)
            # mh_gwh0.automateHunt([
            #     {'env': 'rift_valour', 'has_hat': 1},
            #     {'env': 'rift_valour', 'has_hat': 1},
            #     {'env': 'rift_valour', 'has_hat': 1}
            # ])

            mh_fi = FloatingIslands(howard)
            mh_fi.automateHunt()

            # mh_mapping = Mapping(acc1)
            # mh_mapping.automateHunt()

            # mh_labyrinth = Labyrinth(acc1)
            # mh_labyrinth.automateHunt(['h3l','h3m','h3s','h2l', 'h2m', 'h2s', 'hl', 'hm', 'hs'])

            # mh_bwrift = Bwrift(acc1)
            # mh_bwrift.automateHunt()
            # mh_bwrift.automateHunt(mode='speedy')

            # y = plain fealty, s = plain scholar, h = plain tech
            # y2 = superior fealty, s2 = superior scholar, h2 = superior tech
            # y3 = epic fealty, s3 = epic scholar, h3 = epic tech
            # s = short, m = medium, l = long
            # mh_labyrinth = Labyrinth(acc2)
            # mh_labyrinth.automateHunt(['s3l','s3m','s3s','s2l', 's2m', 's2s', 'sl', 'sm', 'ss'])
            # mh_labyrinth.automateHunt(['h3l','h3m','h3s','h2l', 'h2m', 'h2s', 'hl', 'hm', 'hs'])

            time.sleep(120)
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            continue


if __name__ == "__main__":
    eprint("Main", "Application Started")
    runHornContinuously()