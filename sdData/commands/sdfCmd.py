from sdData.helpers.fileSd import openFile, saveFile
from sdData.modifiers import keepMeta, removeMeta
import logging
import os


def execute(loggerName: str, cmdArgs: dict):
    logger = logging.getLogger(loggerName)
    # open and get structures
    logger.info("Loading Structures From '{}'".format(cmdArgs["file"]))
    structures = openFile(loggerName, cmdArgs["file"])
    updatedCount = 0
    for s in structures:
        # keep meta data
        if cmdArgs["keepProperties"]:
            logger.debug("Keeping Properties '{}'".format(cmdArgs["keepProperties"]))
            keepMeta(s, cmdArgs["keepProperties"])
        elif cmdArgs["removeProperties"]:
            logger.debug("Removing Properties '{}'".format(cmdArgs["removeProperties"]))
            removeMeta(s, cmdArgs["removeProperties"])
        # add new properties
        if cmdArgs["addPropertiesToAll"]:
            logger.debug("Adding Properties '{}'".format(cmdArgs["addPropertiesToAll"]))
            if (len(cmdArgs["addPropertiesToAll"]) % 2) == 0:
                for i in range(0, len(cmdArgs["addPropertiesToAll"]), 2):
                    s[cmdArgs["addPropertiesToAll"][i]] = cmdArgs["addPropertiesToAll"][i + 1]
        updatedCount += 1
    # figure out file name
    fn, ext = os.path.splitext(cmdArgs["file"])
    if not cmdArgs["overWrite"]:
        cmdArgs["file"] = cmdArgs["file"].replace(ext, "_mod{}".format(ext))
    logger.info("Saving {} Updated Structures To '{}'".format(updatedCount, cmdArgs["file"]))
    saveFile(filename=cmdArgs["file"], sdStructures=structures)
