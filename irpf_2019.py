#! /usr/bin/env python3


def calculo_irpf(salario):
    irpf_calculado = 0
    limite = [29078, 41540, 62310, 124620, 207700, 311550, 477710]
    tasa = [0, 10, 15, 24, 25, 27, 31]
    porcentaje = [t/100 for t in tasa]
    base = limite[0]
    mucha_plata = 36/100
    monto_de_cada_tramo = ([base] + [limite[i]-limite[i-1] for i in range(1,
                           len(limite))])
    plata_de_cada_tramo = [mont*porc for mont, porc in 
                           zip(monto_de_cada_tramo, porcentaje)]
    
    print(monto_de_cada_tramo)
    print(plata_de_cada_tramo)

    try:
        franja = encontrar_franja(salario, limite)
# print("Franja:" + str(franja) + "Borde Inferior" + str(limite[franja-1])
#      + "Porcentaje" + str(porcentaje[franja]))
        ultimo_impuesto = (salario - limite[franja-1])*porcentaje[franja]
        plata_franjas_previas = 0
        for i in range(0, franja):
            plata_franjas_previas += plata_de_cada_tramo[i]
        print(ultimo_impuesto)
        print(plata_franjas_previas)
        irpf_calculado = plata_franjas_previas + ultimo_impuesto
        return irpf_calculado
    except FranjaAlta as e:
        print(e)
        plata_franjas_previas = sum(plata_de_cada_tramo)
        ultimo_impuesto = (salario - limite[-1])*mucha_plata
        print(plata_franjas_previas)
        print(ultimo_impuesto)
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
        salario = int(input('Ingrese un salario nominal mensual (0 para finalizar): '))
        if salario == 0:
            break
        print ('El IRPF para un salario mensual de',
               salario, 'pesos es', calculo_irpf(salario))


if __name__ == '__main__':
    main()


def calculo_irpf_VIEJO(salario):
    '''
    NO USAR
    Retorna el valor del irpf calculado para ese salario
    '''
    irpf_calculado = 0
    base = 29078
    limite = [29078, 41540, 62310, 124620, 207700, 311550, 477710]
    sublimite = [base] + [limite[i]-limite[i-1] for i in range(1, len(limite))]
    print(sublimite)
    # 41540-29078, etc
    tasa = [0, 10, 15, 24, 25, 27, 31]
    doblete = list(zip(sublimite, tasa))
    print(doblete)
    tasa_multimillonaria = 36

    if salario < 0:
        return 0

    monto = 0
    porcentaje = 1

    for el in doblete:
        print(el)
        print(salario)
        if salario < 0:  # no llego a esa cuota
            return irpf_calculado
        else:
            irpf_calculado += salario*el[porcentaje]/100
        salario -= el[monto]
    else:
        # salario va a ser mayor que cero, podría hacerlo afuera, con o sin
        # if, pero probemos de la forma pitónica
        irpf_calculado += salario*tasa_multimillonaria/100
        return irpf_calculado
