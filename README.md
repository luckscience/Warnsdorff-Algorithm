# Knight's Tour Visualizer

Visualizador interactivo del problema del Recorrido del Caballo (Knight's Tour) utilizando la heurística de Warnsdorff.

El proyecto calcula un recorrido cerrado sobre un tablero de ajedrez de 8x8 y muestra gráficamente el movimiento del caballo paso a paso mediante una interfaz desarrollada con Tkinter.

## Características

* Implementación del algoritmo de Warnsdorff.
* Separación entre lógica e interfaz gráfica.
* Selección de la casilla inicial desde la interfaz.
* Animación automática del recorrido.
* Visualización de la trayectoria completa mediante líneas.
* Numeración de cada movimiento realizado.
* Soporte para imágenes personalizadas del caballo y del tablero.

## Estructura del proyecto

```text
proyecto/
├── src/
│   ├── algorithm.py
│   ├── gui.py
│   └── knight.png
├── README.md
└── requirements.txt
```

### Descripción de archivos

| Archivo      | Descripción                                       |
| ------------ | ------------------------------------------------- |
| algorithm.py | Implementa el algoritmo del recorrido del caballo |
| gui.py  | Interfaz gráfica y animación del recorrido             |
| knight.png  | Imagen utilizada para representar el caballo       |
| README.md    | Documentación del proyecto                        |
| requirements.txt    | Requerimientos del proyecto                |


## Requisitos

* Python 3.10 o superior
* Tkinter (incluido normalmente con Python)

Verificar instalación de Tkinter:

```bash
python -m tkinter
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/luckscience/Warnsdorff-Algorithm.git
```

Entrar al directorio:

```bash
cd TU_CARPETA
```

## Ejecución

Ejecutar la interfaz:

```bash
python gui.py
```

## Uso

1. Ejecuta la aplicación.
2. Haz clic sobre una casilla para seleccionar la posición inicial.
3. Pulsa "Iniciar recorrido".
4. Observa cómo el caballo realiza el recorrido completo sobre el tablero.

## Cómo contribuir

Las contribuciones son bienvenidas.

### Reportar errores

Si encuentras algún problema:

1. Abre un Issue.
2. Describe claramente el comportamiento observado.
3. Incluye pasos para reproducir el problema.

### Proponer mejoras

Puedes abrir un Issue indicando:

* Funcionalidad propuesta.
* Beneficio esperado.
* Posible implementación.

### Enviar cambios mediante Pull Request

1. Haz un Fork del repositorio.
2. Crea una rama para tu cambio:

```bash
git checkout -b feature/nueva-funcionalidad
```

3. Realiza tus modificaciones.
4. Haz commit de los cambios:

```bash
git commit -m "Añadir nueva funcionalidad"
```

5. Envía la rama:

```bash
git push origin feature/nueva-funcionalidad
```

6. Abre un Pull Request.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo LICENSE para más información.
