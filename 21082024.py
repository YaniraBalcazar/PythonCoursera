def mezclador(string_a, string_b):
  return string_a[:2] + string_b[-2:]

resultado = mezclador("Programación", "Strings")
print(resultado)

def intercalar(string_a, string_b):
    resultado = ""
    for letra in string_a:
        resultado += letra + string_b
    return resultado

resultado = intercalar("paz", "so")
print(resultado)

def ocurrencias(string):
    cantidad_unos = string.count('1')
    cantidad_ceros = string.count('0')
    return cantidad_unos - cantidad_ceros

resultado = ocurrencias("11000110101")
print(resultado)

def remover_enesimo(s, n):
  return s[:n] + s[n+1:]

resultado = remover_enesimo("Hasta luego", 3)
print(resultado)

def reemplazo(string):
    resultado = ""
    for caracter in string:
        if caracter.isupper():
            resultado += "$"
        else:
            resultado += caracter
    return resultado


