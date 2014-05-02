#! /usr/bin/python
#!encoding: UTF-8

#Importamos el módulo "modulo.py" que contiene la funcion "calculo" para la aproximacion de pi.
import modulo


#Definimos la funcion que calculará el porcentaje de errores.
def error (n, m, umbral):     #n = intervalos; m=iteraciones; 
    err = 0.0
    valor_pi = modulo.calculo(n) 
    for j in range (m):
        aprox_pi = modulo.calculo(n)
        if (abs(aprox_pi - valor_pi) > umbral): 
            err = err + 1
    return (err/m) * 100
#Si el valor absoluto de la aproximacion de pi - el valor de pi es mayor que el umbral que le indicamos, entonces nos da el fallo. Para pasarlo a porcentaje 
#lo tenemos en la línea 18 con el "return", y de ahí tenemos todos los casos posibles, por lo que no hace falta hacer un "else".

    
#Cuerpo de comprobaciones del módulo, si este fichero es el principal, se ejecuta:
if (__name__ == "__main__"):
    #Importamos la librería sys para usar de sys.argv.
    import sys
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    umbral = float(sys.argv[3])
    Sol = error(n, m, umbral)            #Importamos la función error 
    print ("\nHay un %.4f %% de errores.\n" %Sol) #Nos imprime el porcentaje de errores con cuatro decimales. 
    
