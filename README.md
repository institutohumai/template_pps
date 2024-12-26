# LAB

## Descripción

Te presentamos un template para dar soporte a tu Proyecto. La presente estructura permite cargar datos, entrenar un modelo, realizar inferencias y visualizar resultados de manera sencilla. 

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-proyecto.git
    cd tu-proyecto
    ```

2. Instalar dependencias:
    - Usando `pip`:
        ```bash
        pip install -r requirements.txt
        ```
    - Usando `conda`:
        ```bash
        conda env create -f environment.yml
        conda activate mi-entorno
        ```


### Entorno de desarrollo

Para crear un nuevo entorno basado en environment.yml, usa este comando:
```bash
conda env create -f environment.yml
```

Si modificas el archivo environment.yml y necesitas actualizar un entorno existente, usa:
```bash
conda env update -f environment.yml --prune
```
Después de crearlo, no te olvides de activar el entorno.

Si ya tienes un entorno configurado, puedes exportarlo directamente a un archivo environment.yml usando:
```bash
conda env export > environment.yml
```

### Requisitos
Puedes configurar tu entorno en base a el documento requirements.txt mediante el siguiente comando:
```bash
pip install -r requirements.txt
```

Puedes crear tu propio documento de requisitos, para el uso de terceros, usando:
```bash
pip freeze > requirements.txt
```


---

## Uso

Ejecutar el script principal:
```bash
python src/main.py
```

Abrir y ejecutar notebooks interactivos:
```bash
jupyter notebook notebooks/
```

## Estructura
- src/: Código fuente del proyecto.
- notebooks/: Notebooks interactivos para exploración y uso.
- data/: Archivos de datos (sin procesar y procesados).
- docs/: Documentación extendida.
- models/: Modelos preentrenados y checkpoints.



---

## **Sugerencias para Branches**

1. **Branch principal: `main`**
   - Contiene la versión estable del proyecto.
   
2. **Branch de desarrollo: `develop`**
   - Para integrar cambios y características nuevas.
   
3. **Branches de características:** 
   - Crear branches para cada nueva funcionalidad:
     ```plaintext
     feature/[nombre_de_la_funcionalidad]
     ```

4. **Branches de hotfix:**
   - Para correcciones urgentes:
     ```plaintext
     hotfix/[descripción_del_problema]
     ```

---

## **Opciones para Configurar un Entorno de Desarrollo**

1. **Uso de Entornos Virtuales**
   - `virtualenv` o `venv`:
     ```bash
     python -m venv mi-entorno
     source mi-entorno/bin/activate
     ```

2. **Uso de Conda**
   - Archivo `environment.yml`:
     ```bash
     conda env create -f environment.yml
     conda activate mi-entorno
     ```

3. **Uso de Docker**
   - Crear un archivo `Dockerfile`:
     ```dockerfile
     FROM python:3.10
     WORKDIR /app
     COPY . .
     RUN pip install -r requirements.txt
     CMD ["python", "src/main.py"]
     ```
   - Construir y ejecutar:
     ```bash
     docker build -t mi-proyecto .
     docker run -it mi-proyecto
     ```


## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). Consulta el archivo `LICENSE` para más detalles.
