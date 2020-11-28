import time, datetime
from questLocations.labyrinth import Labyrinth
from questLocations.vrift import Vrift
from questLocations.bwrift import Bwrift
from questLocations.mapping import Mapping
from questLocations.questProgress import Quest
from questLocations.mouseDetect import MouseDetect
from questLocations.floatingislands import FloatingIslands
from random import randint
from util import eprint
import datetime, traceback

from questLocations.mapping_trapSetup import trapSetup, trapSetup_main


howard = {
    "HG_TOKEN": "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y",
    "uh": "54TYb49T",
}

acc1 = {
    "HG_TOKEN": "72wdLJWpIogUFJ912jQQf6TmcvbgmdM79Y6n094N155aM5BdWHHNmWFL79wS55ly",
    "uh": "LeA1Z1B4"
}

acc2 = {
    "HG_TOKEN": "wI4Q2y0uk4TK1yifrR33vZw9Vq1FkZs73PD22VMSQ600HtOu1f5bn0s6L240278w",
    "uh": "Gc112MbD",
}


def runHornContinuously():
    while True:
        try:

            # mh_vrift = Vrift(howard)
            # mh_vrift.automateHunt()

            # mh_mapping2 = Mapping(howard)
            # mh_mapping2.automateHunt()

            # mh_fi = FloatingIslands(howard)
            # mh_fi.automateHunt()

            # mh_mapping = Mapping(acc1)
            # mh_mapping.automateHunt()

            # mh_labyrinth = Labyrinth(acc1)
            # mh_labyrinth.automateHunt(['h3l','h3m','h3s','h2l', 'h2m', 'h2s', 'hl', 'hm', 'hs'])

            mh_bwrift = Bwrift(acc1)
            # mh_bwrift.automateHunt(mode='speedy')
            mh_bwrift.automateHunt()

            mh_mapping = Mapping(acc2)
            mh_mapping.automateHunt()

            # y = plain fealty, s = plain scholar, h = plain tech
            # y2 = superior fealty, s2 = superior scholar, h2 = superior tech
            # y3 = epic fealty, s3 = epic scholar, h3 = epic tech
            # s = short, m = medium, l = long
            # mh_labyrinth = Labyrinth(acc2)
            # mh_labyrinth.automateHunt(['s3l','s3m','s3s','s2l', 's2m', 's2s', 'sl', 'sm', 'ss'])

            time.sleep(120)
        except Exception as e:
            print(str(e))
            traceback.print_exc()
            continue


if __name__ == "__main__":
    eprint("Main", "Application Started")
    runHornContinuously()