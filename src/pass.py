# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file
"""

heslo = input('zadej své heslo > ') 

MALA = 'abcdefghchijklmopqrstuvwxyz'
VELKA = MALA.upper()
SPECIAL = '!/?+-*&@#$%^&*\§,.Łł[]{}'
CISLA = '123456789'

if len(heslo) < 8:
    print('heslo je příliš krátké')
    exit(1)

jeMALA = False
jeVLEKA = False
jeSPECIAL = False
jeCISLA = False

for znak in heslo:
    if znak in MALA:
        jeMALA = True
    if znak in VELKA:
        jeVELKA = True
    if znak in SPECIAL:
        jeSPECIAL = True
    if znak in CISLA:
        jeCISLA = True

print(jeMALA, jeVELKA, jeSPECIAL, jeCISLA)
if jeMALA + jeVELKA + jeSPECIAL + jeCISLA >=3:
    print('Heslo je v pořádku')
    exit(0)
else:
    print("Heslo je v pořádku")
    exit(3)
        
    
    