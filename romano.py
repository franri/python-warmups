#! /usr/bin/env python3

import sys


def main():
    numerosEnString = sys.argv[1:]
    for numero in numerosEnString:
        procesarUnNumero(numero)


def procesarUnNumero(numeroEnString):
    numeroPadded = numeroEnString.zfill(4)
    m, c, d, u = numeroPadded
    romano = (convertir(int(m), 'miles') + convertir(int(c), 'centenas') + 
              convertir(int(d), 'decenas') + convertir(int(u), 'unidades'))
    print(romano)


numeros = {
        0: {'miles': '', 'centenas': '', 'decenas': '', 'unidades': ''},
        1: {'miles': 'M', 'centenas': 'C', 'decenas': 'X', 'unidades': 'I'},
        2: {'miles': 'MM', 'centenas': 'CC', 'decenas': 'XX', 'unidades':
            'II'},
        3: {'miles': 'MMM', 'centenas': 'CCC', 'decenas': 'XXX', 'unidades':
            'III'},
        4: {'miles': 'NO EXISTE', 'centenas': 'CD', 'decenas': 'XL',
            'unidades': 'IV'},
        5: {'miles': 'NO EXISTE', 'centenas': 'D', 'decenas': 'L', 'unidades':
            'V'},
        6: {'miles': 'NO EXISTE', 'centenas': 'DC', 'decenas': 'LX', 
            'unidades': 'VI'},
        7: {'miles': 'NO EXISTE', 'centenas': 'DCC', 'decenas': 'LXX', 
            'unidades': 'VII'},
        8: {'miles': 'NO EXISTE', 'centenas': 'DCCC', 'decenas': 'LXXX',
            'unidades': 'VIII'},
        9: {'miles': 'NO EXISTE', 'centenas': 'CM', 'decenas': 'XC', 
            'unidades': 'IX'},
        }


def convertir(numero, modo):
    return numeros[numero][modo] 


if __name__ == "__main__":
    main()
