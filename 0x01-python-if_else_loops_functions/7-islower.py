#!/usr/bin/python3
def islower(c):
    ascii_equiv = ord(c)
    if ascii_equiv >= 97 and ascii_equiv < 123:
        return True

    return False
