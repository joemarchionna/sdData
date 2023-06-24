import logging
import logging.handlers
import pathlib


STD_LINE_FRMT = "%(levelname)-7s | %(asctime)s | %(module)-24s | %(funcName)-24s | %(message)s"


def getLogger(quiet=False, verbose=False):
    logDir = "wkdir/logs/"
    pathlib.Path(logDir).mkdir(parents=True, exist_ok=True)
    return _getLogger(loggerName="SD_DATA", logfile=(logDir + "app.log"), quiet=quiet, verbose=verbose)


def _getLogger(
    loggerName,
    logfile=None,
    logfilecount=90,
    quiet=False,
    verbose=False,
    lineFrmt: str = STD_LINE_FRMT,
    recordFactory=None,
):
    if recordFactory:
        logging.setLogRecordFactory(recordFactory)
    lggr = logging.getLogger(loggerName)
    loglevel = logging.INFO
    if verbose:
        loglevel = logging.DEBUG
    elif quiet:
        loglevel = logging.ERROR
    lggr.setLevel(loglevel)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(loglevel)
    consoleHandler.setFormatter(logging.Formatter(fmt=lineFrmt))
    lggr.addHandler(consoleHandler)

    if logfile:
        fileHandler = logging.handlers.TimedRotatingFileHandler(
            filename=logfile,
            when="midnight",
            backupCount=logfilecount,
            encoding="utf-8",
        )
        fileHandler.setLevel(loglevel)
        fileHandler.setFormatter(logging.Formatter(fmt=lineFrmt))
        lggr.addHandler(fileHandler)
    return lggr
