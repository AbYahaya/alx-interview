#!/usr/bin/python3
"""
Module that provides the validUTF8 function to check if
a data set represents valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    num_bytes = 0

    # Masks for checking the leading bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF  # Only use the least significant 8 bits of the num

        if num_bytes == 0:
            # Determine how many bytes are in the character
            if byte >> 5 == 0b110:  # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes = 3
            elif byte >> 7:  # 1-byte character should not start with 10xxxxxx
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
