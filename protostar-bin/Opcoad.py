def convertOpcode(opcode, filler):
    '''
        PURPOSE - Convert a string of opcode numbers to little endian values
        INPUT
            opcode - String of opcode numbers (e.g., copied from object code)
            filler - Value to 'round out' the byte alignment
        OUTPUT - String of escaped opcode values byte-ordered for little endian
    '''
    # LOCAL VARIABLES
    retVal = ""  # String of escaped opcode values byte-ordered for little endian
    inStr = opcode  # 'Working' copy of opcode, in case the alignment needs to be rounded out
    wrdIndexStart = 0  # Index of the beginning of the current word
    wrdIndexStop = 0  # Index of the end of the current word
    tmpStr = ""  # Return value from reverse_endianness

    # INPUT VALIDATION
    if not isinstance(opcode, str):
        raise TypeError("Expected string: opcode")
    elif not isinstance(filler, str):
        raise TypeError("Expected string: filler")
    elif 0 == opcode.__len__():
        raise ValueError("Empty string: opcode")
    elif 0 == filler.__len__():
        raise ValueError("Empty string: filler")
    elif 2 < filler.__len__():
        raise ValueError("Too long: filler")
    elif 0 != (inStr.__len__() % 2):
        raise ValueError("Odd length: opcode")
    elif 0 != (inStr.__len__() % (2 * 4)):
        # print("\nBefore:\t{}\n".format(inStr))  # DEBUGGING
        # print("inStr.len() == {}\n".format(inStr.__len__()))
        # print("Missing:\t{}".format(8 - (inStr.__len__() % 8)))
        inStr = inStr + (filler * ((8 - (inStr.__len__() % (2 * 4))) / 2))
        # print(  "After: \t{}\n".format(inStr))  # DEBUGGING

    # REVERSE IT
    while (wrdIndexStop < inStr.__len__()):
        # Setup indices
        wrdIndexStart = wrdIndexStop
        wrdIndexStop += 8
        # Reverse
        tmpStr = reverse_endianness(inStr[wrdIndexStart:wrdIndexStop])

        retVal = retVal + tmpStr

    # print("\ntmpstr:\t{}".format(tmpStr))  # DEBUGGING
    # CONVERT IT
    # tmpStr = retVal
    retVal = escape_hex(retVal)

    # DONE
    return retVal


def reverse_endianness(hexWord):
    '''
        PURPOSE - Flip the byte ordering of a string holding hex values as characters
        INPUT
            hexWord - A string 8 characters long holding stringified values ("90" instead of "\x90")
        OUTPUT - A string holding the reverse stringified values 
    '''
    # LOCAL VARIABLES
    retVal = ""
    hexIndexStart = hexWord.__len__() - 2  # Index of the beginning of the current hex byte
    hexIndexStop = hexWord.__len__()  # Index of the end of the current hex byte

    # INPUT VALIDATION
    if not isinstance(hexWord, str):
        raise TypeError("Expected string: hexWord")
    elif 8 != hexWord.__len__():
        print("\nhexword len:\t{}\n".format(hexWord.__len__()))  # DEBUGGING
        raise ValueError("Invalid length: hexWord")

    # FLIP IT
    while 0 < hexIndexStop:
        retVal += hexWord[hexIndexStart:hexIndexStop]
        # Decrement
        hexIndexStop = hexIndexStart
        hexIndexStart -= 2

    # DONE
    return retVal


def escape_hex(hexString):
    '''
        PURPOSE - Convert a string of hex values into a string of actual hex values
        INPUT
            hexString - A string of hex values represented by characters
        OUTPUT - A string of escaped hex values in a string
        NOTE
            This function will not modify order
    '''
    # LOCAL VARIABLES
    retVal = ""
    curIndex = 2  # End of the two-nibble slice being converted

    # INPUT VALIDATION
    if not isinstance(hexString, str):
        raise TypeError("Expected string: hexString")
    elif 0 == hexString.__len__():
        raise ValueError("Empty string: hexString")
    elif 0 != hexString.__len__() % 2:
        raise ValueError("Invalid length: hexString")

    retVal = bytearray.fromhex(hexString)

    # DONE
    return retVal
