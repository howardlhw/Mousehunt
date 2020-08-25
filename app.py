import time, datetime
from labyrinth import labyrinth
from vrift import vrift
from bwrift import bwrift, trap_setup

cookies_howard = {
    "hg_session[sessionId]": "X719P43hXAZQM0C2ts840FK35vB52Zms",
    "HG_TOKEN":
    "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y"
}

body_howard = {"uh": "RdQtaaE8",}

cookies_acc1 = {
    "hg_session[sessionId]": "AETPxdJdk436jOgTE06P577va4lCBmJ5",
    "HG_TOKEN":
    "72wdLJWpIogUFJ912jQQf6TmcvbgmdM79Y6n094N155aM5BdWHHNmWFL79wS55ly",
}

body_acc1 = {"uh": "LeA1Z1B4"}

cookies_acc2 = {
    "HG_TOKEN":
    "wI4Q2y0uk4TK1yifrR33vZw9Vq1FkZs73PD22VMSQ600HtOu1f5bn0s6L240278w",
    "bb_sessionhash": "0dcaf65baddc3772685ac7cda0d5d9e2",
}

body_acc2 = {"uh": "Gc112MbD"}

def runHornContinuously():
    while True:
        # mh_vrift = vrift(cookies_howard, body_howard)
        # mh_vrift.automateHunt()

        mh_bwrift = bwrift(cookies_acc1, body_acc1)
        # mh_bwrift.chamberSetup(trap_setup['magic_chamber'])
        mh_bwrift.automateHunt()

        mh_labyrinth = labyrinth(cookies_acc2, body_acc2, debug=True)
        mh_labyrinth.automateHunt(['y3l','y3m','y3s','y2l', 'y2m', 'y2s', 'yl', 'ym', 'ys'])

        time.sleep(600)

if __name__ == "__main__":
    runHornContinuously()