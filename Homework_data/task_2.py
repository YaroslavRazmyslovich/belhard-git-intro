from binascii import crc32


a = float (input ('enter the number а='))
b = float (input ('enter the number b='))
c = float (input ('enter the number c='))
dividend = (a**2 + b**2) / (3*b - 4)
divider = 4*c**5/6
print ('the integer part after division is equal to', dividend // divider)
print ('the remainder after division is equal to', dividend % divider)
