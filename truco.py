#! /usr/bin/env python3

# Federico Abdo
# Paz Fraschini
# Francisco Rizzo
# Pía Rovira

import random

palos = ['oro', 'copa', 'espada', 'basto']
numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
puntaje_normal = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0, 11: 0, 12: 0}
puntaje_pieza = {2: 10, 4: 9, 5: 8, 10: 7, 11: 7}


def puntaje_12(numero):
    return puntaje_pieza[numero]


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def is_pieza(self, muestra):
        if self.palo != muestra.palo:
            return False
        if self.numero not in puntaje_pieza:
            if self.numero == 12 and muestra.numero in puntaje_pieza:
                return True
            else:
                return False
        return True
    
    def valor_normal(self):
        return puntaje_normal[self.numero]

    def valor_pieza(self, muestra):
        if self.numero == 12:
            return puntaje_pieza[muestra.numero]
        return puntaje_pieza[self.numero]

    def __repr__(self):
        return '{:2d} de {}'.format(self.numero, self.palo)


class Mano:
    def __init__(self):
        self.cartas = []
    
    def agregar(self, carta):
        self.cartas.append(carta)

    def get_puntos(self, muestra):
        flor = True
        puntos = self.puntos_flor(muestra)
        if puntos == 0:
            puntos = self.puntos_envido(muestra)
            flor = False
        return puntos, flor

    def puntos_envido(self, muestra):
        cant_piezas = 0
        for i, carta in enumerate(self.cartas):
            if carta.is_pieza(muestra):
                cant_piezas += 1
        if cant_piezas == 1:
            mas_alto = 0
            valor_pieza = 0
            for carta in self.cartas:
                if not carta.is_pieza(muestra):
                    if carta.valor_normal() > mas_alto:
                        mas_alto = carta.valor_normal()
                else:
                    valor_pieza = carta.valor_pieza(muestra)
            puntos = 20 + valor_pieza + mas_alto
            return puntos
        else:  # no hay muestras
            binas = []
            for i in range(3):
                for j in range(i+1, 3):
                    binas.append((self.cartas[i], self.cartas[j]))
            hay_dos = False
            dupla = -1
            for bina in binas:
                if bina[0].palo == bina[1].palo:
                    hay_dos = True
                    dupla = bina
                    break
            
            if hay_dos:
                puntaje = 20 + dupla[0].valor_normal() + dupla[1].valor_normal()
                return puntaje
            else:
                mas_alto = 0
                for carta in self.cartas:
                    if carta.valor_normal() > mas_alto:
                        mas_alto = carta.valor_normal()
                return mas_alto

    def puntos_flor(self, muestra):
        cant_piezas = 0
        for i, carta in enumerate(self.cartas):
            if carta.is_pieza(muestra):
                cant_piezas += 1
        if cant_piezas >= 2:
            puntos = 20
            for carta in self.cartas:
                if carta.is_pieza(muestra):
                    puntos += carta.valor_pieza(muestra)
                else:
                    puntos += carta.valor_normal()
            
            return puntos
        elif cant_piezas == 1:
            palos = []
            for idx, carta in enumerate(self.cartas):
                if not carta.is_pieza(muestra):
                    palos.append(self.cartas[idx].palo)
            if palos[0] == palos[1]:  # son de mismo palo, ya tengo una muestra
                puntos = 20
                for carta in self.cartas:
                    if carta.is_pieza(muestra):
                        puntos += carta.valor_pieza(muestra)
                    else:
                        puntos += carta.valor_normal()
                return puntos
            else:  # son de distinto palo
                return 0
        else:  # chequeo si son 
            if self.cartas[0].palo == self.cartas[1].palo == self.cartas[2].palo:
                puntos = 20
                for carta in self.cartas:
                    puntos += carta.valor_normal()
                return puntos
            return 0


mano_1 = Mano()
mano_2 = Mano()

muestra = None


def main():
    mazo = [Carta(numero, palo) for numero in numeros for palo in palos]
    random.shuffle(mazo)

    for _ in range(3):
        mano_1.agregar(mazo.pop())
        mano_2.agregar(mazo.pop())

    muestra = mazo.pop()

    print('Mano del jugador 1')
    for carta in mano_1.cartas:
        print(carta)

    print('Mano del jugador 2')
    for carta in mano_2.cartas:
        print(carta)

    print('Muestra: ')
    print(muestra)

    # Chequear mano del j1
    puntos_j1, j1_isFlor = mano_1.get_puntos(muestra)
    puntos_j2, j2_isFlor = mano_2.get_puntos(muestra)

    if j1_isFlor:
        print('J1: Flor   de {:2d}'.format(puntos_j1))
    else:
        print('J1: Envido de {:2d}'.format(puntos_j1))

    if j2_isFlor:
        print('J2: Flor   de {:2d}'.format(puntos_j2))
    else:
        print('J2: Envido de {:2d}'.format(puntos_j2))


if __name__ == '__main__':
    main()
