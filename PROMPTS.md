# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py (Receta)

**Herramienta**: 
Gemini

**Prompt usado**:
 Actuá como tutor de Python 3.13. Dame una receta paso a paso para completar estas 6 funciones con su nombre de funcion y su tipo de dato, de entrada y salida.
 1) crear_saludo(nombre) -> devuelve "Hola, {nombre}!"
 2) suma_enteros(a, b) -> devuelve la suma.
 3) es_mayor_de_edad(edad) -> devuelve True si es >= 18.
 4) tipo_de_dato(valor) -> devuelve el nombre del tipo (como string).
 5) convertir_a_float(valor) -> convierte un string a número decimal.
 6) armar_mensaje(nombre, edad, ciudad) -> 
Mostrame el código limpio para pegar en mi archivo. 

**Resultado obtenido**:
Le pedí a la IA que me pase una "receta" paso a paso para no tener errores. Me ayudó a usar f-strings para los saludos y a entender cómo usar type().name para que el código me diga qué tipo de dato es cada variable directamente. Al final, los tests pasaron.

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 2 - condicionales.py (interaccion invertida)

**Herramienta**: 
Gemini

**Prompt usado**:
Quiero implementar cuatro funciones en Python: clasificar_numero, mayor_de_tres, clasificar_nota y es_bisiesto. Antes de proporcionarme el código, actuá como un verificador y para hacerme 3 preguntas clave sobre las reglas de negocio, el orden de las condiciones y los casos borde (como el año bisiesto o las notas) para confirmar que entiendo la lógica. Una vez que responda, generá el código final.
Sobre las notas (clasificar_nota): Si un alumno saca de nota un 9.5, ¿qué categoría debería devolver el programa? ¿Importa el orden en que pongamos los if (por ejemplo, preguntar primero si es mayor a 6 o primero si es mayor a 9)?
Sobresaliente. si importa. Sobre el número mayor (mayor_de_tres): ¿Qué debería pasar si los tres números son iguales (ejemplo: 6, 6, 6)? Deberia devolver el numero y listo. Sobre el año bisiesto (es_bisiesto): Según el PDF, el año 2100 es divisible por 4 y por 100, pero NO por 400. ¿Entonces es bisiesto o no? No

**Resultado obtenido**:
La IA realizó preguntas de validación sobre el orden de los condicionales, el manejo de números iguales y la lógica de años bisiestos. Tras aclarar que el orden de las notas debe ser descendente y que la función de mayor debe devolver solo el entero, se procedió a implementar el código.

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 3 - listas.py (verificador cognitivo)

**Herramienta**: 
Gemini

**Prompt usado**:
Estoy resolviendo un ejercicio de listas en Python que incluye funciones como suma_lista, filtrar_pares, invertir_lista, eliminar_duplicados y aplanar_lista. ¿Podés actuar como mi verificador cognitivo y revisar mi lógica?
Enumerá casos borde que debería testear (listas vacías, tipos mixtos).
Decime errores típicos (como modificar la lista original por accidente).
Proponé 3 tests con entradas y salidas esperadas para estas funciones sin darme el código final todavía.

**Resultado obtenido**:
Casos Borde: * Lista vacía []: La suma debería ser 0 y el filtro debería devolver []. Si no lo manejás, el código puede fallar. 
Duplicados: Si tenés [1, 2, 1, 3], el resultado debe ser [1, 2, 3]. El orden de "primera aparición" es clave aca. 
Errores Típicos: * Invertir la lista: Si usás lista.reverse(), modificás la original y desaprobás esa función. Hay que usar un método que cree una copia. 
Aplanar: Si la lista tiene diferentes tamaños (ej: [[1], [2, 3]]), el bucle tiene que ser flexible. 

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 4 - diccionarios.py (generacion infinita)

**Herramienta**: 
Gemini

**Prompt usado**:
Actuá como un generador de ejemplos de diccionarios en Python. Generá 8 ejemplos distintos de diccionarios que representen frecuencias de palabras, mapeos de claves-valores invertibles y combinaciones de diccionarios. Para cada ejemplo, mostrá cómo se vería antes y después de aplicar funciones como contar_palabras, invertir_diccionario, merge_diccionarios y filtrar_por_valor. Finalmente, derivá una regla general y proporcioná el código para implementar estas funciones en mi TP.

**Resultado obtenido**:
Para que el código pase el pytest, hay que tener cuidado con:
contar_palabras: El enunciado pide comparar en minúsculas.
invertir_diccionario: Si un valor se repite, la última clave que lo use "pisará" a la anterior (esto es normal en diccionarios).
merge_diccionarios: Si d1 y d2 tienen la misma clave, mandan los datos de d2

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 5 - loops.py (refinamiento de preguntas)

**Herramienta**: 
Gemini

**Prompt usado**:
P1: ¿Cómo genero una lista de números del 1 al N usando range en Python? P2: ¿Cuál es la forma más eficiente de sumar los dígitos de un número sin convertirlo a string? P3: ¿Cómo puedo verificar si un número es primo optimizando el bucle para que no recorra todos los números? P4: Para la serie de Fibonacci, ¿cómo manejo los casos donde N es 0 o 1 para evitar errores en la lista? P5: Mostrame la implementación final de estas funciones para mi TP.

**Resultado obtenido**:
Para que los tests no te reboten, hay que tener en cuenta estos detalles: contar_hasta: El range tiene que ser (1, n + 1) para que incluya al número N. suma_digitos: Aunque se puede hacer con strings, usar el operador % 10 y // 10 es lo que suelen pedir en programación para trabajar con restos. es_primo: Recordá que el 1 no es primo. El bucle debe empezar desde 2.

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 6 - funciones.py (reflexion)

**Herramienta**: 
Gemini

**Prompt usado**:
Necesito implementar aplicar_funcion, componer, memoizar y reducir en Python 3.13. Antes de darme el código, realizá una reflexión sobre la diferencia entre ejecutar una función y "devolver una función" (como en componer y memoizar). Analizá qué enfoque es más claro para evitar efectos secundarios y proporcioná la implementación más legible para un nivel inicial. Resultado obtenido: La IA reflexionó sobre el concepto de closures y funciones como objetos de primera clase. Se determinó que usar bucles simples para reducir es más legible que la recursión, y se implementó un decorador básico para la memoización.

**Resultado obtenido**:
 La IA reflexionó sobre el concepto de closures y funciones como objetos de primera clase. Se determinó que usar bucles simples para reducir es más legible que la recursión, y se implementó un decorador básico para la memoización.

**¿Lo usaste tal cual o lo modificaste?**
 Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

### 7 - operaciones.py

**Herramienta**: 
Gemini

**Prompt usado**:
Necesito implementar es_palindromo, capitalizar_palabras, contar_vocales y caesar_cipher. Compará dos enfoques: 1- Usar métodos de strings de Python como .title(), .replace() y slicing, y 2- Hacerlo manualmente con bucles y comparaciones de códigos ASCII. Analizá cuál es más mantenible y proporcioná la solución definitiva. 

**Resultado obtenido**:
La IA comparó el uso de métodos nativos (más legibles) frente a lógica manual (más educativa). Se optó por una mezcla: métodos nativos para limpieza de texto y lógica de caracteres para el cifrado César.

**¿Lo usaste tal cual o lo modificaste?**
Use el mismo tipo de PROMPT, pero no el que estaba en el github.

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Varia mucho para lo que se necesita, ya que para cada ejercicio se necesita algo especifico. Es importante conocer el funcionamiento individual de cada uno para poder resolver de la mejor forma posible.
- ¿En qué casos la IA fue útil y en cuáles no?
En todos fue util, al ser ejercicios simples no presento alguna "ineficiencia" en estos casos, pero si fuesen mas complejos, habrian casos donde no seria util.
- ¿Qué harías diferente la próxima vez?
tratar de enfocarme en un tipo de patron y explotarlo mas
