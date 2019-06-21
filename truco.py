#! usr/bin/env python3

import random

palos = ['oro', 'copa', 'espada', 'basto']
numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
puntaje_normal = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0, 11: 0, 12: 0}
puntaje_pieza = {2: 30, 4: 29, 5: 28, 10: 27, 11: 27, 12: 9999}


def puntaje_12(numero):
    return puntaje_pieza[numero]


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def is_muestra(self, muestra):
        if self.palo != muestra.palo:
            return False
        if self.carta not in puntaje_pieza:
            return False
        return True
    
    def valor_normal(self):
        return puntaje_normal[self.numero]

    def valor_pieza(self, muestra):
        if self.numero == 12:
            return puntaje_pieza(muestra.numero)
        return puntaje_pieza[self.numero]

    def __repr__(self):
        return self.numero + ' de ' + self.palo


class Mano:
    def __init__(self):
        self.cartas = []
    
    def agregar(self, carta):
        self.cartas.append(carta)

    def puntos_flor(self, muestra):
        cant_muestras = 0
        es_muestra = []
        for i, carta in enumerate(self.cartas):
            if carta.is_muestra():
                cant_muestras += 1
                es_muestra[i] = True
            else:
                es_muestra[i] = False
        if cant_muestras >= 2:
            puntos = 0
            for carta in self.cartas:
                if carta.is_muestra():
                    puntos += carta.puntaje_pieza(muestra)
                else:
                    puntos += carta.puntaje_normal()
            return puntos
        elif cant_muestras == 1:


        


mano_1 = Mano()
mano_2 = Mano()

muestra = None


def main():
    mazo = [Carta(numero, palo) for numero in numeros for palo in palos]
    random.shuffle(mazo)

    for _ in range(2):
        mano_1.agregar(mazo.pop())
        mano_2.agregar(mazo.pop())

    muestra = mazo.pop()

    print('Mano del jugador 1')
    for carta in mano_1:
        print(carta)

    print('Mano del jugador 2')
    for carta in mano_2:
        print(carta)

    print('Muestra: ')
    print(muestra)

    # Chequear mano del j1
    puntos_j1 = mano_1.get_puntos(muestra)
