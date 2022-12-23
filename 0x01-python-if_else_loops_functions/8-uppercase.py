#!/usr/bin/python3
for i in str:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        i = str(ord(i) - 32)
        print("{:s}" .format(i), end="")
        print()
