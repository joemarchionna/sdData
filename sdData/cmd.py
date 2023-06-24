import sys

sys.path.append(".")

from setup.args import getArgumentDict
from setup.log import getLogger

import sdData.commands.csvCmd as csvCommand
import sdData.commands.sdfCmd as sdfCommand

CMD_MAP = {"sdf": csvCommand.execute, "sdf": sdfCommand}

if __name__ == "__main__":
    args = getArgumentDict()
    logger = getLogger(quiet=args["quiet"], verbose=args["verbose"])
    logger.info("----- START -----")
    outputCmd = args["output"].lower()
    CMD_MAP[outputCmd](logger.name, cmdArgs=args)
    logger.info("------ END ------")
