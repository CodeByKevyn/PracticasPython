""" Cálculo de promedio manual (Base de estadística):
Tienes una lista con los tiempos de espera en minutos de 6 clientes en una sucursal: 
[8, 12, 5, 15, 10, 10]. Recorre la lista con un ciclo for para sumar todos los tiempos, 
calcula el promedio dividiendo esa suma entre la cantidad de clientes usando len(), e imprime el resultado. """

tiempos_espera = [8, 12, 5, 15, 10, 10]
suma = 0
cantidad_datos = len(tiempos_espera)

for tiempo in tiempos_espera:
    suma = suma + tiempo

print(suma)
print(cantidad_datos)
print("promedio:", suma / cantidad_datos) 
""" aqui es un float  """

""" Recibes una lista con los montos de varias transferencias del día:
[450000, 1200000, 85000, 3500000, 990000, 5100000]. Recorre la lista y cuenta cuántas transacciones
superan $1,000,000. Al finalizar el ciclo, imprime la cantidad total de alertas generadas. """

trasferencias = [450000, 1200000, 85000, 3500000, 990000, 5100000]
contador = 0

for trasferencia in trasferencias:
    if trasferencia > 1000000:
        contador = contador + 1

print("Alertas generadas:", contador)


""" Filtro y limpieza de datos hacia una nueva lista:
Tienes una lista de edades capturadas en una encuesta: [25, -4, 38, 140, 19, 62, 12, 45]. 
Crea una lista vacía llamada edades_validas = []. Recorre la lista original y, usando .append(), 
guarda en edades_validas únicamente aquellas edades que estén entre 18 y 100 (inclusive). Al final,
imprime la lista limpia. """

edades = [25, -4, 38, 140, 19, 62, 12, 45]
edades_validas = []

for edad in edades:
    if edad >= 18 and edad <= 100:
        edades_validas.append(edad)

print(edades_validas)

""" 1. Simulador de meta de ahorro (while)
Un cliente abre una cuenta con $100,000 y cada mes ahorra exactamente $85,000 adicionales (sin intereses).
Quiere saber cuántos meses tardará en alcanzar o superar una meta de $1,000,000.
Usa un ciclo while para simular el paso de cada mes, lleva un contador de meses e imprime cuántos meses 
exactos necesitó y con cuánto dinero terminó. """

cuenta = 100000
ahorro = 85000
contador = 0

while cuenta < 1000000:
    contador = contador + 1
    cuenta = cuenta + ahorro

print("Meses que necesito: ", contador)
print("Termino con", cuenta)


""" En pruebas técnicas es muy común que te prohíban usar las funciones integradas max() y min() para evaluar 
si sabes construir la lógica tú mismo.
Tienes los tiempos de respuesta (en milisegundos) de un servidor: [120, 45, 310, 88, 19, 450, 102].
Recorre la lista con un ciclo for y encuentra tanto el tiempo más rápido (mínimo) como el más lento (máximo)
    comparando elemento por elemento. Al final imprime ambos valores.
(Pista lógica: antes del ciclo, asume que tanto el mínimo como el máximo son el primer elemento de la lista)
. """

servidor = [120, 45, 310, 88, 19, 450, 102]
minimo = servidor[0]
maximo = servidor[0]

for servi in servidor:
    if minimo > servi:
        minimo = servi
    if maximo < servi:
        maximo = servi

print("El minimo es:",minimo)
print("El maximo es:",maximo)


""" Un sistema antifraude revisa en orden cronológico los movimientos de una tarjeta durante el día:
movimientos = [45000, 120000, 80000, -1, 500000, 30000]
El valor -1 representa una alerta crítica de clonación de tarjeta. Recorre los movimientos sumando
el gasto total válido, pero si encuentras el código -1, debes detener el análisis inmediatamente con break,
imprimir "Alerta crítica: tarjeta bloqueada" y mostrar cuánto dinero alcanzó a gastarse antes del bloqueo 
(sin sumar el -1 ni los movimientos posteriores). """

movimientos = [45000, 120000, 80000, -1, 500000, 30000]
dinero = 0

for movi in movimientos:

    if movi < 0:
        print("Tarjeta Bloqueada")
        break
    dinero = dinero + movi

print("Dinero gastado antes del bloqueo", dinero)