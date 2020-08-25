import time, datetime
from questLocations.labyrinth import Labyrinth
from questLocations.vrift import Vrift
from questLocations.bwrift import Bwrift
from questLocations.bwrift_trapSetup import trapSetup


howard = {
    "HG_TOKEN": "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y",
    "uh": "RdQtaaE8"
}

acc1 = {
    "HG_TOKEN": "72wdLJWpIogUFJ912jQQf6TmcvbgmdM79Y6n094N155aM5BdWHHNmWFL79wS55ly",
    "uh": "LeA1Z1B4"
}


acc2 = {
    "HG_TOKEN": "wI4Q2y0uk4TK1yifrR33vZw9Vq1FkZs73PD22VMSQ600HtOu1f5bn0s6L240278w",
    "uh": "Gc112MbD"
}


def runHornContinuously():
    while True:
        mh_vrift = Vrift(howard)
        mh_vrift.automateHunt()

        mh_bwrift = Bwrift(acc1)
        # mh_bwrift.chamberSetup(trapSetup['acolyte_chamber']) # Currently has 87 sands
        mh_bwrift.automateHunt()

        mh_labyrinth = Labyrinth(acc2, debug=True)
        mh_labyrinth.automateHunt(['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys'])

        time.sleep(600)

if __name__ == "__main__":
    runHornContinuously()