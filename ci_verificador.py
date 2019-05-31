
def verificar_cedula(ci):
    '''
    Dada una cédula sin verificador, devuelve el verificador (número después
    del guión)
    '''
    try:
        int(ci)
    except ValueError:
        return(-1)

    string_ci = '{:07d}'.format(ci)  # padding si la ci no tiene largo 7

    if len(string_ci) != 7:
        return(-1)

    verification_number = '2987634'  # El numero por el que hay que multiplicar 

    total_sum = sum([int(x) * int(y) for x, y in zip(verification_number, string_ci)])

    return((10 - total_sum % 10) % 10)
