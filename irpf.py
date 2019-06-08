#! /usr/bin/env python3

import json

datos = './irpf.json'


def obtener_datos(y):
    todos_los_y = json.load(open(datos))
    datos_de_este_y = todos_los_y['IRPF'][str(y)]
    limite = [el for el, tasa in datos_de_este_y[:-1]]
    porcentaje = [tasa/100 for el, tasa in datos_de_este_y[:-1]]
    base = limite[0]
    mucha_plata = datos_de_este_y[-1][1]
    return (limite, porcentaje, base, mucha_plata)


def calculo_irpf(salario, y):
    (limite, porcentaje, base, mucha_plata) = obtener_datos(y)
    irpf_calculado = 0
    monto_de_cada_tramo = ([base] + [limite[i]-limite[i-1] for i in range(1,
                           len(limite))])
    plata_de_cada_tramo = [mont*porc for mont, porc in
                           zip(monto_de_cada_tramo, porcentaje)]

    try:
        franja = encontrar_franja(salario, limite)
# print("Franja:" + str(franja) + "Borde Inferior" + str(limite[franja-1])
#      + "Porcentaje" + str(porcentaje[franja]))
        ultimo_impuesto = (salario - limite[franja-1])*porcentaje[franja]
        plata_franjas_previas = 0
        for i in range(0, franja):
            plata_franjas_previas += plata_de_cada_tramo[i]
        irpf_calculado = plata_franjas_previas + ultimo_impuesto
        return irpf_calculado
    except FranjaAlta:
        plata_franjas_previas = sum(plata_de_cada_tramo)
        ultimo_impuesto = (salario - limite[-1])*mucha_plata
        irpf_calculado = plata_franjas_previas + ultimo_impuesto
        return irpf_calculado


def encontrar_franja(salario, limite):
    for i, el in enumerate(limite):
        if salario < el:
            return i
    raise FranjaAlta("Multimillonario")


class FranjaAlta(Exception):
    pass


def main():
    while True:
        y = int(input('Ingrese año (0 para finalizar): '))
        if y == 0:
            break
        salario = int(input('Ingrese un salario nominal mensual (0 para finalizar): '))
        if salario == 0:
            break
        print ('El IRPF para un salario mensual de',
               salario, 'pesos es', calculo_irpf(salario, y))


if __name__ == '__main__':
    main()
