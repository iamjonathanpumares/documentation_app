# documentation_app

Aplicación hecha en Django para documentar tus proyectos.

## Requerimientos

Python 2.7

## Configurar entorno de desarrollo

El proyecto funciona con **Virtualenv**, que es una herramienta para crear entornos virtuales en Python. 

En modo desarrollo se utiliza el archivo de configuración ubicado en `documentation_app/local.py`, por lo que los comandos ejecutados con `python manage.py` deben llevar la opción `--settings=documentation_app.local`.

### Instalar Virtualenv

Si aún no tienes Virtualenv, puedes instalarlo con `pip`

```bash
> pip install virtualenv
```

### Pasos de configuración

1. Crea un entorno virtual para el proyecto con **Virtualenv**:

```bash
> virtualenv venv
```

2. Activa el entorno virtual con:

```bash
# MacOS, Linux
> source venv/bin/activate

# Windows
> venv/scripts/activate
```

3. Instala las dependencias del proyecto:

```bash
> python -m pip install -r requirements.txt
```

4. Ejecuta las migraciones en una nueva base de datos SQLite:

```bash
> python manage.py migrate --settings=documentation_app.local
```

5. Ejecuta el servidor de desarrollo:

```bash
> python manage.py runserver --settings=documentation_app.local
```