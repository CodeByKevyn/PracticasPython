""" Control de saldo en cajero:
Un cliente tiene $500,000 en su cuenta e intenta retirar $650,000. El sistema debe
validar si le alcanza el dinero. Si la operación es válida, debe confirmar el retiro e informar 
cuánto dinero le queda disponible; de lo contrario, debe rechazarla por falta de fondos. 
(Prueba luego con un retiro de $200,000 para comprobar ambos escenarios). """

monto = 500000
retiro = 200000
if monto >= retiro:
    print("Retiro exitoso")
    print("Su nuevo saldo es:", monto - retiro)
    print()
else:
    print("Retiro Rechazado su saldo es:", monto)


""" Alerta térmica de servidores:
El centro de datos registra una temperatura actual de 28 grados. El sistema de monitoreo clasifica 
el estado ambiental en tres niveles: frío (por debajo de 15 grados), templado (desde 15 hasta 26 grados)
y caluroso (por encima de 26 grados). Imprime en pantalla el estado correspondiente. """

temperatura = 14

if temperatura < 15:
    print("Estado Frio")
elif temperatura >= 15 and temperatura <= 26:
    print("Estado Templado")
else:
    print("Estado Caluroso")


""" Clasificador de turnos por paridad:
A un usuario se le asigna el turno número 47. Necesitas determinar matemáticamente si el número
es par o impar para enviarlo a la fila correspondiente e imprimir el resultado. """

turno = 47

if turno % 2 == 0:
    print("Fila de los pares")
else:
    print("Fila de los impares")

""" Un cliente solicita un préstamo en el banco. Para evaluarlo, cuentas con tres datos: sus ingresos 
mensuales ($3,200,000), su puntaje crediticio (680 puntos) y si actualmente está reportado en centrales
            de riesgo (False).
Las políticas del banco son estrictas:
Si está reportado en centrales de riesgo, el crédito se rechaza de inmediato sin importar sus ingresos 
o puntaje.
Si no está reportado, pero sus ingresos son iguales o superiores a $3,000,000 y su puntaje es mayor o 
igual a 700, recibe aprobación directa.
Si no cumple lo anterior, pero tiene ingresos superiores a $2,500,000 o un puntaje mayor o igual a 650
 (sin estar reportado), pasa a estudio manual con un asesor.
En cualquier otro caso, el crédito se rechaza por capacidad insuficiente.
Imprime la decisión exacta del sistema y prueba cambiando los valores de las variables para asegurarte 
de que los cuatro caminos funcionen. """