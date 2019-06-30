#! /usr/bin/env python3

import operator
import argparse
import os
import stat
import pwd
import grp
import datetime
import sys
import collections


class Wrapper:
    def __init__(self, name):
        self.name = name
 
    def agregar_datos(self, result):
        self.owner = pwd.getpwuid(result.st_uid).pw_name
        self.group = grp.getgrgid(result.st_gid).gr_name
        self.size = str(result.st_size)
        self.inode = result.st_ino
        self.mod_date = str(datetime.datetime.fromtimestamp(result.st_mtime))
        self.permissions = stat.filemode(result.st_mode)

    def info_extra(self):
        return ' '.join([self.permissions, self.owner, self.group, self.size, self.mod_date])

    def __repr__(self):
        return self.name

banderas = {'all': False, 'directory': False, 'inode': False, 'l': False, 't':
            False, 'documentos': []}
has_flags = False


def parse_args():
    parser = argparse.ArgumentParser(description='Implementación de ls con Python')

    parser.add_argument(
            '--all', '-a',
            default=False,
            action='store_true'
            )
    parser.add_argument(
            '--directory', '-d',
            default=False,
            action='store_true'
            )
    parser.add_argument(
            '--inode', '-i',
            default=False,
            action='store_true'
            )
    parser.add_argument(
            '-l',
            default=False,
            action='store_true'
            )
    parser.add_argument(
            '-t',
            default=False,
            action='store_true'
            )
    parser.add_argument(
            'documentos',
            nargs='*'
            )

    args = vars(parser.parse_args())
    for arg in args:
        global banderas 
        banderas[arg] = args[arg]
        if args[arg]:  # si es una bandera, setea has_flags en true si es true
            global has_flags
            has_flags = True   # si es el caso de la lista, entra solo no vacia 
    #print(str(args) + str(has_flags))
    #print(banderas)


def main():
    global banderas
    parse_args()
    directorios = []
    archivos = []
    not_found = []
    if not has_flags:
        imprimir = []
        directorio = os.scandir()
        for entry in directorio:
            if entry.name[0] != '.':
                imprimir.append(entry.name)
        imprimir.sort()
        for el in imprimir:
            print(el)
    else:  # algo especial va a haber que hacer
        if not banderas['documentos']:
            banderas['documentos'].append('.')
        # para cada ruta en banderas, clasifico en dir, file o not_exist. Si
        # hay muchos dirs o dir y archivo, tengo que imprimir
        # tipo una sección por cada dir
        for ruta in banderas['documentos']:
            completa = os.path.abspath(ruta)
            try:
                result = os.stat(completa)
            except OSError as e:
                print(e)
                not_found.append(ruta)
                continue
            if banderas['directory']:
                archivos.append(ruta)
            else:
                if stat.S_ISDIR(result.st_mode):
                    directorios.append(ruta)
                elif stat.S_ISREG(result.st_mode):
                    archivos.append(ruta)
            directorios.sort()
        # hay mas de un dir o hay files y dirs
        if len(directorios) > 1 or (len(archivos) != 0 and len(directorios) != 0):
            # imprimo primero archivos, luego dirs de a secciones
            imprimir_not_found(not_found)
            imprimir_archivos(archivos)
            imprimir_directorios(directorios)
        elif len(archivos) == 0 and len(directorios) == 1:
            imprimir_directorio(directorios[0])
        else:  # tengo solo archivos
            imprimir_archivos(archivos)


def imprimir_not_found(not_found):
    for el in not_found:
        print("ls: cannot access '" + el + "': No such file or directory")


def imprimir_directorios(directorios):
    for directorio in directorios:
        print(directorio + ':')
        imprimir_directorio(directorio)


def imprimir_directorio(directorio):
    archivos = os.listdir(directorio)
    archivos = [os.path.join(os.path.abspath(directorio), archivo) for archivo
                in archivos]
    imprimir_archivos(archivos)


def imprimir_archivos(archivos):
    if not archivos:
        return
    lista = []
    global banderas
    for archivo in archivos:
        if archivo == '.' or archivo == '..' or archivo == '../' or archivo == './' :
            holder = Wrapper(archivo)
        else:
            holder = Wrapper(os.path.basename(os.path.abspath(archivo)))
        holder.agregar_datos(os.stat(os.path.abspath(archivo)))
        # no checkeo lo de all porque explicitamente se pidió ese archivo
        lista.append(holder)
    if banderas['t']:
        lista = sorted(lista, key=operator.attrgetter('mod_date'), reverse=True)
    else:
        lista = sorted(lista, key=operator.attrgetter('name'))
    for el in lista:
        if not banderas['all'] and not banderas['directory']:
            if el.name.startswith('.'):
                continue
        if banderas['inode']:
            print(el.inode, end=' ')
        if banderas['l']:
            print(el.info_extra(), end=' ')
        print(el.name)


if __name__ == '__main__':
    main()
