#! /usr/bin/env python3

import sys

terminaciones = {
            'ar': ('o', 'as', 'a', 'amos', 'áis', 'an'),
            'er': ('o', 'es', 'e', 'imos', 'éis', 'en'),
            'ir': ('o', 'es', 'e', 'emos', 'éis', 'en')
        }

personas = {
        0: 'Yo', 1: 'Tú', 2: 'Él/Ella', 3: 'Nosotros', 4: 'Vosotros', 5:
        'Ellos/Ellas'
        }


def main():
    palabra = sys.argv[1]
    raiz = palabra[:-2]
    terminacion = palabra[-2:]
    for (numero, persona) in personas.items():
        verbo = raiz + terminaciones[terminacion][numero]
        print(f'{persona} {verbo}')


if __name__ == "__main__":
    main()
