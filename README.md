## Ejecucion Stack

Inicializamos los contenedores
```bash
docker-compose up -d
```
Detenemos los contenedores
```bash
docker-compose stop
```
Destruimos los contenedores
```bash
docker-compose down
```

### Crear entorno virtual Python
1. Creamos un entorno virtual de Python
python -m venv .venv

2. Activamos el entorno virtual de Python
.venv\Scripts\activate

3. Instalamos las dependencias del proyecto
pip install -r requirements.txt