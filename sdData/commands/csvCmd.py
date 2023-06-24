from sdData.helpers.fileSd import openFile
from sdData.helpers.csvSd import saveCsv

import logging
import os


def execute(loggerName: str, cmdArgs: dict):
    logger = logging.getLogger(loggerName)
    # open and get structures
    logger.info("Loading Structures From '{}'".format(cmdArgs["file"]))
    structures = openFile(loggerName, cmdArgs["file"])
    # figure out csv file name
    fn, ext = os.path.splitext(cmdArgs["file"])
    csvFn = cmdArgs["file"].replace(ext, ".csv")
    if cmdArgs.get("csvPath", None):
        csvFn = cmdArgs.get["csvPath"]
    logger.info("Saving {} Structures To '{}'".format(len(structures), cmdArgs["file"]))
    saveCsv(csvFn, sdStructures=structures, metaFieldNames=cmdArgs["properties"])
