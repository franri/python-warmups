#! /usr/bin/env python3

from collections import deque

def reemp_fifo(paginas, marcos, debug=False):

    # armo lista para saber que pagina esta en que marco (va a tener paginas
    # como elementos)
    en_memoria = [-1]*marcos    
    # armo dict para saber posición actual de una pagina y no tener que buscar
    # cada vez dentro de la lista.
    posicion_paginas = {n: -1 for n in paginas}

    fallos = 0
    cola = deque()

    for actual in paginas:
        if posicion_paginas[actual] == -1:
            if en_memoria[-1] != -1:  # es decir, no llene aun toda la memoria 
                viejo = buscar_reemplazo(actual, cola)
                cambiar(posicion_paginas, en_memoria, viejo, actual)
            else:
                agregar_directo_a_memoria(posicion_paginas, en_memoria, actual,
                                          cola)
            if debug:
                # imprimo los que no son -1 (ya fueron llenados)
                print([el for el in en_memoria if el != -1])
            fallos += 1


def agregar_directo_a_memoria(posicion_paginas, en_memoria, nuevo, cola):
    for index, el in enumerate(en_memoria):
        if el == -1:
            en_memoria[index] = nuevo
            posicion_paginas[nuevo] = index
            cola.append(nuevo)
            break


# FIFO
def buscar_reemplazo(actual, cola):
    if len(cola) != 0:
        return cola.popleft()


def cambiar(posicion_paginas, en_memoria, viejo, nuevo):
    posicion_para_el_nuevo = posicion_paginas[viejo]
    posicion_paginas[viejo] = -1
    posicion_paginas[nuevo] = posicion_para_el_nuevo
    en_memoria[posicion_para_el_nuevo] = nuevo


if __name__ == '__main__':
    paginas = 'ABBCDEEA'
    marcos = 4
    reemp_fifo(paginas, marcos, debug=True)
