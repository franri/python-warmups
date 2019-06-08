#! /usr/bin/env python3


def reemp_fifo(paginas, marcos, debug=False):

    # armo lista para saber que pagina esta en que marco (va a tener paginas
    # como elementos)
    en_memoria = [-1]*marcos
    # armo dict para saber posición actual de una pagina y no tener que buscar
    # cada vez dentro de la lista.
    posicion_paginas = {n: -1 for n in paginas}

    fallos = 0

    for idx, actual in enumerate(paginas):
        if posicion_paginas[actual] == -1:
            if en_memoria[-1] != -1:  # es decir, no llene aun toda la memoria
                viejo = buscar_reemplazo(paginas, idx + 1, en_memoria)
                if type(viejo) is not str:
                    print('UUUPPPSSS: {}'.format(viejo))
                    exit(1)
                cambiar(posicion_paginas, en_memoria, viejo, actual)
            else:
                agregar_directo_a_memoria(posicion_paginas, en_memoria, actual)
            fallos += 1
            if debug:
                # imprimo los fallos y los que no son -1 (ya fueron llenados)
                print('Fallos: {}. Marcos: {}.'.format(
                            fallos, [el for el in en_memoria if el != -1]))


def agregar_directo_a_memoria(posicion_paginas, en_memoria, nuevo):
    for index, el in enumerate(en_memoria):
        if el == -1:
            en_memoria[index] = nuevo
            posicion_paginas[nuevo] = index
            break


# Óptimo
def buscar_reemplazo(paginas, idx, en_memoria):
    primera_necesidad = {el: -1 for el in en_memoria}
    no_usados = set(en_memoria)
    # para los que se precisen, agrego a lista y pongo primera posicion
    for i in range(idx, len(paginas)):
        if paginas[i] in primera_necesidad and primera_necesidad[paginas[i]] == -1:
            no_usados.remove(paginas[i])
            primera_necesidad[paginas[i]] = i
    if len(no_usados) != 0:
        el = next(iter(no_usados))
        return el
    else:
        el = -1
        necesidad_actual = -1
        for key in primera_necesidad:
            if primera_necesidad[key] > necesidad_actual:
                el = key
                necesidad_actual = primera_necesidad[key]
        return el
    

def cambiar(posicion_paginas, en_memoria, viejo, nuevo):
    posicion_para_el_nuevo = posicion_paginas[viejo]
    posicion_paginas[viejo] = -1
    posicion_paginas[nuevo] = posicion_para_el_nuevo
    en_memoria[posicion_para_el_nuevo] = nuevo


if __name__ == '__main__':
    paginas = '012333455501842250'
    marcos = 4
    print(paginas)
    reemp_fifo(paginas, marcos, debug=True)
