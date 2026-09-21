# Ejercicios con Python

## Descripción

Este repositorio reúne ejercicios de programación en Python organizados por tema y dificultad. El objetivo es practicar desde los fundamentos del lenguaje hasta estructuras de datos y algoritmos más avanzados.

## Objetivos del repositorio

1. **Aprender y practicar Python:** trabajar de forma progresiva los principales conceptos del lenguaje.
2. **Fomentar el pensamiento algorítmico:** resolver problemas de forma estructurada y reutilizable.
3. **Mejorar la capacidad de debugging:** practicar la detección, comprensión y corrección de errores.
4. **Mantener una progresión temática clara:** cada carpeta corresponde a un concepto principal; los niveles de dificultad se mantienen dentro del mismo tema.

## Estructura del repositorio

Las carpetas se organizan por **tema principal**, no por nivel de dificultad. Los subtítulos `Nivel Básico`, `Intermedio`, `Avanzado` y `Experto` de [Enunciados.md](Enunciados.md) pertenecen a la misma carpeta temática.

| Nº | Carpeta | Tema | Ejercicios |
|---:|---|---|---|
| 01 | `01_Variables_Operadores_Expresiones_Condicionales_Bucles` | Fundamentos de Python | 1–13 del primer bloque |
| 02 | `02_Funciones` | Funciones | 1–23 del segundo bloque |
| 03 | `03_Listas_Tuplas_Conjuntos_Diccionarios` | Listas, tuplas, conjuntos y diccionarios | 1–36 y 73–107 |
| 04 | `04_Validacion_De_Datos` | Validación y control de entradas | 108–127 |
| 05 | `05_Funciones_De_Orden_Superior` | Funciones de orden superior | 128–147 |
| 06 | `06_Recursividad` | Recursividad y backtracking | 148–157 y 228–237 |
| 07 | `07_Pilas_Y_Colas` | Pilas, colas y colas de prioridad | 158–167 y 238–247 |
| 08 | `08_Programacion_Orientada_A_Objetos` | Clases y objetos | 168–187 |
| 09 | `09_Estructuras_Enlazadas_Con_POO` | Listas enlazadas, pilas y colas con POO | 188–207 |
| 10 | `10_Arboles` | Árboles y sus variantes | 208–227 |
| 11 | `11_Grafos` | Grafos y algoritmos de grafos | 248–267 |
| 12 | `12_Matrices` | Matrices y álgebra lineal | 268–287 |
| 13 | `13_Hash_Y_Tablas_Hash` | Funciones hash y tablas hash | 288–307 |
| 14 | `14_Archivos` | Lectura, escritura y procesamiento de archivos | 308–337 |

> **Nota sobre la numeración:** los tres primeros bloques conservan la numeración histórica con la que ya están nombrados los archivos existentes. A partir del ejercicio 73, la numeración es global y continua. Se corrigió una duplicación que existía originalmente en el bloque de Grafos, por lo que los bloques posteriores terminan actualmente en el ejercicio 337.

### Árbol temático

```text
Ejercicios-con-Python/
├── 01_Variables_Operadores_Expresiones_Condicionales_Bucles/
├── 02_Funciones/
├── 03_Listas_Tuplas_Conjuntos_Diccionarios/
├── 04_Validacion_De_Datos/
├── 05_Funciones_De_Orden_Superior/
├── 06_Recursividad/
├── 07_Pilas_Y_Colas/
├── 08_Programacion_Orientada_A_Objetos/
├── 09_Estructuras_Enlazadas_Con_POO/
├── 10_Arboles/
├── 11_Grafos/
├── 12_Matrices/
├── 13_Hash_Y_Tablas_Hash/
├── 14_Archivos/
├── Enunciados.md
└── README.md
```

Las carpetas se irán creando conforme se avance por los ejercicios. No se crean carpetas distintas únicamente por cambiar de nivel de dificultad.

## Enunciados

La lista completa y ordenada de ejercicios se encuentra en [Enunciados.md](Enunciados.md).

Dentro de ese archivo, los temas principales corresponden a las carpetas anteriores. Algunos temas reaparecen más adelante con ejercicios avanzados —por ejemplo Recursividad o Pilas y Colas—, pero continúan perteneciendo a su misma carpeta.

## Cómo usar este repositorio

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JaimeLapaz/Ejercicios-con-Python.git
   ```

2. Entra en la carpeta del tema que estés practicando.

3. Consulta el enunciado correspondiente en `Enunciados.md`.

4. Ejecuta el ejercicio:

   ```bash
   python Ejercicio_XX.py
   ```

5. Prueba casos adicionales y revisa el código antes de continuar con el siguiente bloque.

## Convención de archivos

Los ejercicios siguen el formato:

```text
Ejercicio_01.py
Ejercicio_02.py
...
```

Cada solución intenta mantener una estructura consistente:

- Enunciado y solución documentados al inicio.
- Funciones separadas cuando aportan claridad o reutilización.
- Bloque `if __name__ == "__main__":` para ejemplos y ejecución directa.
- Pruebas sencillas que permitan verificar el comportamiento.

## Contribuciones

Las mejoras, correcciones y enfoques alternativos son bienvenidos mediante issues o pull requests.

## Contacto

Si tienes alguna pregunta o necesitas ayuda, puedes utilizar los issues del repositorio o contactar en [jl.jaimelapaz@gmail.com](mailto:jl.jaimelapaz@gmail.com).
