# Simulador de Búfer de Entrada en Python

Este proyecto implementa un simulador de un búfer de entrada utilizando Python. La solución está diseñada para procesar datos eficientemente en fragmentos pequeños, utilizando un carácter especial `eof` como centinela para indicar el final de los datos.

## Descripción del Proyecto

El programa:
- Simula un búfer con un tamaño fijo de 10 caracteres.
- Utiliza una lista de caracteres como entrada.
- Implementa dos punteros (`inicio` y `avance`) para simular la lectura del búfer.
- Procesa datos en fragmentos, cargando nuevos datos cuando el búfer actual se agota.
- Imprime cada "lexema" (secuencia de caracteres entre espacios o el final del archivo) procesado.

## Cómo Funciona

1. **Carga de Búfer:**
  - La función `loadBuffer` llena un búfer de tamaño fijo desde la entrada, añadiendo el carácter `eof` cuando se alcanzan los últimos datos.

2. **Procesamiento de Datos:**
  - La función `buffet` recorre el búfer, extrae lexemas y los imprime.
  - Cuando el puntero `avance` alcanza el final del búfer, los datos se recargan desde la entrada.

3. **Finalización:**
  - El programa termina al encontrar el carácter `eof`.

## Requisitos del Sistema

- Python 3.6 o superior.

## Ejecución

1. Clona este repositorio:
  ```bash
  git clone https://github.com/Diegoval-Dev/DLP-input-buffer
  cd DLP-input-buffer
  ```
2. Ejecuta el programa:
  ```bash
  python simulador_buffer.py
  ```
3. Observa la salida en la consola.

## Ejemplo de Entrada y Salida

**Entrada:**
  ```plaintext
  Esto es un ejemplo de entrada con eof
  ```

**Salida:**
  ```plaintext
  Lexema procesado: Esto
  Lexema procesado: es
  Lexema procesado: un
  Lexema procesado: ejemplo
  Lexema procesado: de
  Lexema procesado: entrada
  Lexema procesado: con
  Lexema procesado: eof
  ```

## Explicación Técnica

El programa utiliza dos conceptos importantes:

- **Búfer de Entrada:**
  - Almacena datos temporalmente en bloques pequeños para optimizar el procesamiento.
- **Centinela (eof):**
  - Marca el final de los datos y permite detener el procesamiento cuando no hay más datos disponibles.

## Archivos en el Proyecto

- `simulador_buffer.py`: Código fuente principal.
- `README.md`: Este archivo con la documentación del proyecto.

## Video Explicativo

Enlace al video

## Autores

Diego Valenzuela -
 22309
