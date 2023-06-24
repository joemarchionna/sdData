from prettyHelpFrmt.prettyHelpFormatter import PrettyHelpFormatter
from sdData.constants import ALL_FIELDS, MOL_JSON_LINE_TERMINATOR
import argparse


def getArgumentDict():
    formatter = lambda prog: PrettyHelpFormatter(prog, max_help_position=80, actionSeparation=28)
    parser = argparse.ArgumentParser(description="Structured Chemical Definition Handling", formatter_class=formatter)

    lp = parser.add_mutually_exclusive_group()
    lp.add_argument(
        "-q",
        "--quiet",
        help="Quiet, Produce Almost No Logging",
        action="store_true",
        default=False,
    )

    lp.add_argument(
        "-v",
        "--verbose",
        help="Verbose, Produce Excessive Logging",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="File Path, Get Items To Work On From A File, Each Line An Item",
        metavar="filepath",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-o",
        "--overWrite",
        help="Over-Write Source File With Modified File",
        action="store_true",
        default=False,
    )

    outputParser = parser.add_subparsers(dest="output", title="Save As Output", required=True)
    sdfParser = outputParser.add_parser("sdf", help="SD File", formatter_class=formatter)

    propGrp = sdfParser.add_mutually_exclusive_group()
    propGrp.add_argument(
        "-kp",
        "--keepProperties",
        help="List of Properties to Keep, Discarding All That Are NOT In The List",
        metavar="name",
        type=str,
        nargs="+",
        default=None,
    )
    propGrp.add_argument(
        "-rp",
        "--removeProperties",
        help="List of Properties to Remove, Keeping All That Are NOT In The List",
        metavar="name",
        type=str,
        nargs="+",
        default=None,
    )

    sdfParser.add_argument(
        "-ap",
        "--addPropertiesToAll",
        help="Add Properties To Each Structure Record, Provide Even Number Of Arguments In Key Value Order, ie: k v k v k v",
        metavar="{n} {v}",
        type=str,
        nargs="+",
        default=None,
    )

    csvParser = outputParser.add_parser("csv", help="CSV File", formatter_class=formatter)

    csvParser.add_argument(
        "-p",
        "--properties",
        help="Properties To Output To CSV, default is all",
        metavar="propName",
        type=str,
        nargs="+",
        default=ALL_FIELDS,
    )

    csvParser.add_argument(
        "-x",
        "--csvPath",
        help="CSV File Path, Default Is The Same Location As Source Except With csv Extension",
        metavar="filepath",
        type=str,
        default=None,
    )

    # jsonParser = outputParser.add_parser("json", help="JSON File")

    # jsonParser.add_argument(
    #     "-ld",
    #     "--lineDelimiter",
    #     help="MOL Field Line Delimiter, default is '{}'".format(MOL_JSON_LINE_TERMINATOR),
    #     metavar="lineDelim",
    #     type=str,
    #     default=MOL_JSON_LINE_TERMINATOR,
    # )

    return vars(parser.parse_args())
