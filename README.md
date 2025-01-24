# generadorTexto-api
Poyecto propuesto por la empresa Roams, basado en implemetar una API para generar un texto con ayuda de un modelo IA

# Anexos
1.[Descarga de VSC](https://code.visualstudio.com/download)
2.[Descarga de Git](https://git-scm.com/downloads)

# Instalación

## Git
1. Iniciar repositorio:

    ```bash

    git init

    ```

2. Clonar repositorio del proyecto:

    ```bash

    git clone https://github.com/wilBrito/generadorTexto-api.git
    
    ```

## VSC
1. Instalar recurso:

    ```bash

    pip install -r requirements.txt

    ```

2. Ejecutar Api:

    ```bash

    uvicorn main:app --reload

    ```

# Prubas

## Postman
1. Post:
    ```bash

    localhost:8000/generar

    ```
    ```bash

    {
        "prompt": "Spain is",
        "longitud": 100,
        "temperatura": 0.8,
        "top_p": 0.9
    }

    ```

    ```bash

    {
        "prompt": "Football is",
        "longitud": 200,
        "temperatura": 0.8,
        "top_p": 0.9
    }

    ```

2. Get:
```bash

    localhost:8000/historial

    ```