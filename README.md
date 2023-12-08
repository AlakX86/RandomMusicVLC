# RandomMusicVLC

## Descripción del Proyecto
Este proyecto, RandomMusicVLC, está diseñado para proporcionar aleatoriedad al reproducir música. Utiliza una combinación de archivos de lista de reproducción en formato xspf (el mismo que usa VLC cuando exportas una lista), el reproductor multimedia VLC, y una función de aleatorización para ofrecer variedad en la reproducción de tus pistas favoritas.

## Cómo instalar
### Requisitos
    python3

    VLC en el path C:\\Program Files\\VideoLAN\\VLC\\vlc.exe
    
### Instalación en Entorno Virtual (Virtualenv)

1. Clona el proyecto:

    ```bash
    git clone https://github.com/AlakX86/RandomMusicVLC.git
    ```

2. Accede a el:

    ```bash
   cd RandomMusicVLC
    ```
    Es muy importante que aquí en la raiz pongas tu .xspf
#### Es probable que no necesites estos 2 ultimos pasos, si unicamente quieres ejecutar el programa, ve a la sección de ejecución, esto es solo es necesario para desarrolladores
3. Instala virtualenv:

    ```bash
    pip install virtualenv
    ```
    
4. Inicializa el entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    (venv) $ pip install -r requirements.txt
    ```

## Ejecución de la Aplicación

1. Ejecuta la aplicación:

    ```bash
    python main.py
    ```

## Dependencias

- `colorama==0.4.6`
- `coverage==7.3.2`
- `iniconfig==2.0.0`
- `packaging==23.2`
- `pluggy==1.3.0`
- `pytest==7.4.3`

### Verificación de Dependencias

Para verificar las dependencias instaladas y asegurarse de que no haya problemas:

```bash
$ pip check
No broken requirements found.
```
