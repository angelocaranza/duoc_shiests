from itertools import cycle

rut = 18278339

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d,f in zip(reversed_digits,factors))
    return (-s) % 11

print("el digito verificador del rut : ",rut, "  es: ", digito_verificador(rut) )   