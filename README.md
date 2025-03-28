# Casa Mecate - Test

Prueba tecnica. Proyecto Flask.

Pasos
=============

1. Restaurar el backup de la base de datos

* Correr el servicio de PostgreSQL: test-casa-mecate
* Crear la BD en un DBMS de PostgreSQL: test-casa-mecate
* Ejecutar las sentencias SQL del archivo: ref/test-casa-mecate-backup.sql

1. Instalas dependencias

* `pip install -r requirements.txt`

3. Correr el proyecto

* `python app.py`

4. Confirmar ejecucion del API ingresando a <http://127.0.0.1:3000/>

```json
{
  "msn": "It Works"
}
```
