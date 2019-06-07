#! /usr/bin/env python3

import random
import sys

filename = '/usr/share/dict/spanish'
max_intentos = 5


def get_random_word(filename):
    with open(filename, 'r') as f:
        global lista
        lista = f.readlines()
        palabra = random.choice(lista)
        if(palabra[-1] == '\n'):
            palabra = palabra[:-1]
    return palabra


def hashear_palabra(palabra):
    mapa = {}
    for i, letra in enumerate(palabra):
        if letra not in mapa:
            vacio = []
            vacio.append(i)
            mapa[letra] = vacio
        else:
            mapa[letra].append(i)
    return mapa


def main():
    palabra = get_random_word(filename)

    intentos = max_intentos
    emboques = ['_']*len(palabra)

    ya_ingresadas = set()

    # cargo palabra en hash
    mapa = hashear_palabra(palabra)

    while ''.join(emboques) != palabra and intentos > 0:
        print('Progreso: {}\nIntentos disponibles:{}'.format('|'.join(emboques), intentos))
        char = input('Ingrese una letra --> ')
        if char in ya_ingresadas:
            print('Ya ingresada! Intente nuevamente')
        elif char in mapa:
            print('Acierto!')
            ya_ingresadas.add(char)
            for i in mapa[char]:
                emboques[i] = char
        else:
            print('Le erraste!')
            ya_ingresadas.add(char)
            intentos -= 1

    if ''.join(emboques) == palabra:
        print('Ganaste! Palabra: {}'.format(palabra))
    else:
        print('Te quedaron {} intentos. Perdiste!\nDe paso, era \
\'{}\''.format(intentos, palabra))


if __name__ == '__main__':
    main()
