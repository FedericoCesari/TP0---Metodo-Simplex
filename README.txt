Resolución de Matrices Simplex

¿Qué hace este proyecto?
-------------------------
Este proyecto implementa un algoritmo Simplex en Python para la resolución de problemas de programación lineal enfocados exclusivamente en problemas de **maximización**. Utiliza el método Simplex para encontrar la solución óptima de una función objetivo lineal, dada una serie de restricciones lineales. El programa permite cargar las matrices manualmente o desde un archivo, facilitando la resolución del problema.

¿Por qué es útil este proyecto?
------------------------------
Este proyecto es útil para:
- Resolver problemas de maximización en programación lineal de manera automática.
- Visualizar las matrices Simplex paso a paso y comprender el proceso iterativo del algoritmo.
- Verificar y validar los resultados de la optimización, ya sea trabajando con matrices cargadas manualmente o desde archivos.

Este proyecto es ideal para estudiantes o profesionales de áreas relacionadas con la optimización matemática y programación lineal.

¿Cómo comenzar con el proyecto?
------------------------------
1. **Requisitos previos**:
   - Tener **Python 3.12** o superior instalado en tu computadora.
   - Instalar las dependencias necesarias:
     - `numpy` (para manejo de matrices)
     - `colorama` (para mejorar la visualización en la terminal)
     - `pandas` (para guardar matrices en un archivo CSV)
     - `os` (para manipular archivos y rutas)
     

2. **Usar el programa**:
   - Clona este repositorio o descarga el código a tu máquina.
   - Ejecuta el script en Python desde la terminal.
   - Ingresa el número de variables y restricciones del problema que deseas resolver.
   - Luego, se te pedirá que ingreses los coeficientes de la función objetivo y las restricciones.

Puedes cargar las matrices desde un archivo (ver el siguiente apartado), o puedes ingresarlas manualmente durante la ejecución del programa.

3. **Cargar matrices desde un archivo**:
 - El programa permite cargar las matrices desde un archivo de texto (.txt).
 - Si decides cargar las matrices desde un archivo, asegúrate de que el archivo siga el formato correcto y sea cargado en el repositorio correcto, como el mostrado en los ejemplos de los archivos cargados por defecto.

4. **Formato del archivo de entrada**:
  - El archivo debe contener los coeficientes de las matrices en el formato adecuado, asegurándote de que los valores estén separados por espacios.

**Ejemplo de formato de archivo de entrada:**

		6.0 2.0 3.0 0.0
		2.0 1.0 1.0 8.0
		1.0 2.0 2.0 10.0
		3.0 2.0 1.0 15.0

  - La primera línea corresponde a los coeficientes de la función objetivo, donde el último valor debe ser 0. 
  - Las siguientes líneas corresponden a las restricciones, y el valor de la última columna representa la disponibilidad máxima del recurso.
  - Los valores pueden ser enteros o flotantes. Si el archivo contiene valores no numéricos, el programa no funcionará correctamente.

En este ejemplo:
  - `6.0 2.0 3.0 0.0` es la función objetivo (el último valor es 0).
  - `2.0 1.0 1.0 8.0` es la primera restricción (con disponibilidad máxima 8).
  - `1.0 2.0 2.0 10.0` es la segunda restricción (con disponibilidad máxima 10).
  - `3.0 2.0 1.0 15.0` es la segunda restricción (con disponibilidad máxima 15).

Si decides usar archivos de ejemplo cargados por defecto, revisa los archivos proporcionados para verificar el formato correcto de las matrices.

¿Dónde pueden los usuarios obtener ayuda con este proyecto?
----------------------------------------------------------
Si tienes problemas con el programa, puedes:
- Revisar el código fuente y los comentarios dentro del mismo.
- Consultar la documentación de Python y las bibliotecas utilizadas (`numpy`, `colorama`, `pandas`, `os`).
- Si encuentras errores o tienes dudas, puedes abrir un "issue" en este repositorio de GitHub.

Si necesitas más ejemplos o tienes problemas con el formato de los archivos, puedes buscar tutoriales sobre programación lineal y el método Simplex en Python en plataformas como YouTube, Stack Overflow, o foros especializados.

¿Quién mantiene y contribuye al proyecto?
------------------------------------------
Este proyecto es mantenido por Federico Cesari y Axel Martino. Si deseas contribuir al proyecto, puedes realizar un **pull request** para añadir nuevas funcionalidades, corregir errores o mejorar la documentación. ¡Las contribuciones son bienvenidas!

