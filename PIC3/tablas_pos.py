#! /usr/bin/env python3

import json
import operator


class Equipo:

    def __init__(self, name):
        self.equipo = name
        self.gan = 0
        self.emp = 0
        self.per = 0
        self.gf = 0
        self.gc = 0
        self.pts = self.get_pts()
        self.dg = self.get_dg()

    def gana(self, favor, contra):
        self.gan += 1
        self.gf += favor
        self.gc += contra
        self.pts = self.get_pts()
        self.dg = self.get_dg()
    
    def pierde(self, favor, contra):
        self.per += 1
        self.gf += favor
        self.gc += contra
        self.pts = self.get_pts()
        self.dg = self.get_dg()
        
    def empata(self, favor, contra):
        self.emp += 1
        self.gf += favor
        self.gc += contra
        self.pts = self.get_pts()
        self.dg = self.get_dg()

    def jug(self):
        return self.gan + self.per + self.emp

    def get_dg(self):
        return self.gf - self.gc

    def get_pts(self):
        return self.gan*3 + self.emp

    def __repr__(self):
        return '{:10} {:3d} {:3d} {:3d} {:3d} {:3d} {:3d} \
{:3d} {:3d}'.format(self.equipo, self.jug(), self.gan, self.emp, self.per, self.dg, self.gf, self.gc, self.pts)


series = {'Serie A': {}, 'Serie B': {}, 'Serie C': {}}
datos = '/var/2019/publico/partidos.json'


def cargar_datos():
    print('Buscando en: ' + datos)
    todos_datos = json.load(open(datos))
    for serie in todos_datos:
        # cargo equipos
        equipos = todos_datos[serie]['Equipos']
        for equipo in equipos:
            series[serie][equipo] = Equipo(equipo)
        partidos = todos_datos[serie]['Partidos']
        for partido in partidos:
            equipos = list(partido.keys())
            eq_0 = (series[serie][equipos[0]], partido[equipos[0]])
            eq_1 = (series[serie][equipos[1]], partido[equipos[1]])
            if eq_0[1] > eq_1[1]:
                eq_0[0].gana(eq_0[1], eq_1[1])
                eq_1[0].pierde(eq_1[1], eq_0[1])
            elif eq_1[1] > eq_0[1]:
                eq_1[0].gana(eq_1[1], eq_0[1])
                eq_0[0].pierde(eq_0[1], eq_1[1])
            elif eq_0[1] == eq_1[1]:
                eq_0[0].empata(eq_0[1], eq_1[1])
                eq_1[0].empata(eq_1[1], eq_0[1])


def main():
    cargar_datos()
    for serie in sorted(series):
        print(serie)
        print('{:10} {:3} {:3} {:3} {:3} {:3} {:3} {:3} {:3}'.format('Equipo', 'Jug', 'Gan', 'Emp', 'Per', 'DG', 'GF', 'GC',
              'Pts'))
        ranking = []
        for equipo in series[serie]:
            ranking.append(series[serie][equipo])
        ranking = sorted(ranking, key=operator.attrgetter('pts', 'dg'), reverse=True)
        for el in ranking:
            print(el)


if __name__ == '__main__':
    main()
    
