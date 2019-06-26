#! /usr/bin/env python3

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Ejercicio 2 de PIC 3')

    parser.add_argument(
            '--dict', '-d',
            default='/usr/share/dict/spanish'
            )
    parser.add_argument(
            '--empieza', '-e'
            )
    parser.add_argument(
            '--largo', '-l',
            required=True,
            type=int
            )
    parser.add_argument(
            'letras',
            type=str
            )

    args = vars(parser.parse_args())
    return args


def main():

    args = parse_args()
    palabras = None
    lista = []
    letras = args['letras']
    largo = args['largo']
    ruta = args['dict']
    e = args['empieza']
    
    print('Buscando en: ' + ruta)

    with open(ruta) as f:
        palabras = {line.rstrip('\n') for line in f}

    for s in palabras:
        if len(s) == largo and (e is None or s.startswith(e)):
            ocurrencias = {}
            for c in letras:
                if c in ocurrencias:
                    ocurrencias[c] += 1
                else:
                    ocurrencias[c] = 1
            pasa = True
            for c in s:
                if c not in ocurrencias or ocurrencias[c] == 0:
                    pasa = False
                    break
                else:
                    ocurrencias[c] -= 1
            if pasa:
                lista.append(s)

    lista.sort()
    for el in lista:
        print(el)


if __name__ == '__main__':
    main()


