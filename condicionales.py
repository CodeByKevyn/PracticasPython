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

ingresos_mensuales = 3200000
puntaje_crediticio = 780
reportado = True

if reportado:
    print("Credito Rechazado")
elif ingresos_mensuales >= 3000000 and puntaje_crediticio >= 700:
    print("Credito Aprovado")
elif ingresos_mensuales > 2500000 or puntaje_crediticio >=650:
    print("Estudio Manual con Asesor")
else:
    print("Credito Rechazado por Capacidad Insuficiente")


""" Tarifa dinámica de envío con trampa de orden
Una tienda en línea cobra el domicilio según el valor de la compra, pero además ofrece envío gratis 
a clientes con membresía VIP. Tienes el valor de la compra ($45,000) y si el cliente es VIP (True).
Las reglas de cobro son:
Los clientes VIP nunca pagan envío, sin importar cuánto compren.
Para clientes no VIP: si la compra es inferior a $50,000, el envío cuesta $10,000; si está entre $50,000 
y $100,000 (inclusive), cuesta $5,000; y si supera los $100,000, el envío es gratis ($0).
Calcula el valor del envío, súmalo al valor de la compra e imprime el total a pagar. (Ten cuidado con el 
orden de tus if/elif para que un cliente VIP con una compra pequeña no termine pagando envío por error). """


compra = 4000
cliente_vip = False

if cliente_vip == True:
    total = compra
    print("Envio Gratis")
    print("Total a pagar ", total)
elif cliente_vip == False and compra < 50000:
    domicilio = 10000
    total = compra + domicilio
    print("El Domicilio vale: 10000")
    print("Total a pagar ", total)
elif cliente_vip == False and 50000 <= compra <= 100000:
    domicilio = 5000
    total = compra + domicilio
    print("El Domicilio vale: 5000")
    print("Total a pagar ", total)
elif cliente_vip == False and compra > 100000:
    total = compra
    print("Envio es gratis")
    print("Total a pagar ", total)


""" Validador de año bisiesto (Prueba clásica de entrevista)
En análisis de series de tiempo y calendarios financieros es vital saber si un año tiene 365 o 366 días.
Dado un año cualquiera (por ejemplo, 2024, luego prueba con 1900 y con 2000), determina si es bisiesto o no
según las reglas reales del calendario gregoriano:
Un año es bisiesto si es divisible exactamente entre 4 y no es divisible entre 100, o si es divisible
exactamente entre 400.
Imprime si el año evaluado es "Año bisiesto" o "Año normal". """

año = 2024

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("Es un añ0 bisiesto")
else:
    print("Año Normal")
