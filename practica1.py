""" Tus primeras variables:
Crea 3 variables: ciudad (con el nombre de tu ciudad),
 temperatura (un número decimal, por ejemplo 22.5)
  y esta_lloviendo (True o False). Imprime las 3 variables usando print(). """

ciudad = "Medellin"
temperatura = 26.5
esta_lloviendo = False

print("ciudad: ", ciudad)
print("temperatura: ", temperatura)
print("esta lloviendo: ", esta_lloviendo)


""" Presupuesto mensual:
Crea una variable sueldo = 2000000 y otra gastos = 1350000. 
Crea una tercera variable llamada dinero_libre que reste los gastos al sueldo e imprímela. """

sueldo = 2000000 
gastos = 1350000
dinero_libre = sueldo - gastos

print(dinero_libre)

""" Compra en tienda:
Una camiseta cuesta precio = 45000 y vas a comprar cantidad = 3. 
Crea una variable subtotal que multiplique el precio por la cantidad,
 y luego una variable cuota que divida ese subtotal entre 2. Imprime subtotal y cuota. """

precio = 45000
cantidad = 3
subtotal = precio * cantidad
cuota = subtotal / 2

print(cuota)

""" Ejercicio 1: El reloj digital (// y %)
Un partido o película duró exactamente minutos_totales = 195.
Crea una variable horas usando división entera (//) para saber cuántas horas completas
caben en esos 195 minutos.
Crea una variable minutos_restantes usando módulo (%) para saber cuántos minutos sueltos sobran.
Imprime ambos valores (debe darte 3 horas y 15 minutos). """

minutos_totales = 195
horas = minutos_totales // 60 
minutos_restantes = minutos_totales % 60

print(horas, "horas y", minutos_restantes, "minutos")


""" Ejercicio 2: Seguimiento de estado en un videojuego (Lógica de actualización)
Empiezas una partida con estas dos variables:
Python
puntos = 20
vidas = 3
Actualiza esas mismas variables paso a paso (una línea por cada evento):
Ganas un bono: súmale 15 a puntos.
Pierdes una vida: réstale 1 a vidas.
Multiplicador de nivel: actualiza puntos multiplicándolo por las vidas que te quedan en ese momento 
(puntos = puntos * vidas).
Impuesto final: actualiza puntos guardando únicamente lo que sobra de dividir puntos entre 12 
(puntos = puntos % 12).
Imprime el valor final de puntos y vidas. (Intenta adivinar cuánto da en papel antes de darle Play). """

puntos = 20 
vidas = 3
puntos = puntos + 15
vidas = vidas - 1
puntos = puntos * vidas
puntos = puntos % 12

print(puntos,vidas)

""" Ejercicio 3: Desarmar un código PIN de 3 dígitos (Matemática pura)
Tienes una clave numérica guardada como entero: pin = 836.
Sin convertirlo a texto, usa solo divisiones enteras (//) y residuos (%)
para extraer cada cifra por separado:
primero: divide pin entre 100 con // (te dará el 8).
ultimo: saca el residuo de dividir pin entre 10 con % (te dará el 6).
medio: primero divide pin entre 10 con // (eso te deja 83) y a ese resultado 
sácale el residuo con % 10 (te dará el 3).
Crea una variable suma_digitos que sume primero + medio + ultimo e imprímela. """


pin = 836
primero = pin // 100
ultimo = pin % 10
medio = pin // 10 % 3
suma_digitos = primero + medio + medio
print(suma_digitos)


""" Ejercicio 4: Calculadora de propina inteligente (Conversión + truco booleano)
Recibes estos datos desde una aplicación móvil:
Python
cuenta_str = "84500"
personas_str = "4"
incluir_propina = True
En Python, cuando multiplicas un número por un booleano, True vale 1 y False vale 0.
Aprovecha esto para resolverlo sin usar if:
Convierte cuenta_str y personas_str a enteros usando int().
Calcula la variable propina multiplicando cuenta * 0.10 * incluir_propina.
Calcula total_por_persona sumando cuenta + propina y dividiendo todo entre personas.
Imprime total_por_persona. Luego cambia incluir_propina = False, vuelve a ejecutar el archivo 
y mira cómo el cálculo cambia solo. """

cuenta_str = "84500"
personas_str = "4"
incluir_propina = False
cuenta = int(cuenta_str)
personas = int(personas_str)
propina = cuenta * 0.10 * incluir_propina
total_por_persona = cuenta + propina / personas
print(total_por_persona)


""" Reto Final del Módulo 1 (Para cerrar con broche de oro)
Corrige esas dos líneas en tu archivo practica1.py y resuelve este último ejercicio que combina 
todo lo que aprendiste (conversión de tipos, paréntesis, //, % y actualización):
El cajero automático:
Tienes un cliente que va a retirar monto = 387000. El cajero solo tiene billetes
 de $100,000, $50,000, $20,000 y $2,000, y debe entregar la menor cantidad de billetes posible.
Calcula cuántos billetes de $100,000 entrega usando b100 = monto // 100000.
Actualiza monto con lo que falta por entregar usando módulo: monto = monto % 100000.
Repite exactamente esa misma lógica para calcular b50 (billetes de 50000), b20 (billetes de 20000) 
y b2 (billetes de 2000), actualizando monto después de cada uno.
Imprime cuántos billetes de cada denominación entrega el cajero y cuánto dinero quedó sobrando en monto 
(debe darte 3 de 100k, 1 de 50k, 1 de 20k, 8 de 2k y 1000 sobrando). """


monto = 387000
b100 = monto // 100000
monto = monto % 100000
b50 = monto // 50000
monto = monto % 50000
b20 = monto // 20000
monto = monto % 20000
b2 = monto // 2000
monto = monto % 2000

print(b100)
print(b50)
print(b20)
print(b2)
print(monto)