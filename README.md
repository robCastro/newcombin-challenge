# NewCombin Backend Challenge

## Pre requisitos:
- Python 3.9
- MySQL >= 5.7

## Instalación (Linux)
- Crea una BD para el sistema. Toma nota del usuario y contraseña para conectarte a dicha BD.
- Clona este repositorio
- Entra a la carpeta donde se clonó el repositorio.
- Copia el archivo .env.example, llama a la copia .env
    ```bash
    cp .env.example .env
    ```
- Configura las variables dentro el archivo .env
- Crea un nuevo virtual environment para el proyecto.

    ```bash
    python -m venv venv
    ```

- Activalo
    ```bash
    source venv/bin/activate
    ```

- Instala los requirements
    ```bash
    pip install -r requirements.txt
    ```

- Corre las migraciones de la BD:
    ```bash
    python manage.py migrate
    ```

- **(Opcional)** Crear registros de payables y transactions:
    ```bash
    python manage.py seed
    ```

- Corre el servidor de prueba
    ```bash
    python manage.py runserver
    ```

## Probando la API

La API se centra en los Payables y Transactions.

### Payables:
Se encuentran en la ruta `/taxes/api/v1/payables/`

#### Crear un payable
- Utilizar metodo POST
- JSON de ejemplo para el body del request:
```json
{
	"barcode": "1234567894",
	"service_type": "G",
	"description": "Test",
	"expiration_date": "2022-04-29",
	"service_import": "1500.00",
	"payment_status": "PE"
}
```

#### Lista de payables
- Utilizar metodo GET
- Todos los payables: `/taxes/api/v1/payables/`
- Payables de Gas: `/taxes/api/v1/payables/?service_type=G`
- Payables de Luz: `/taxes/api/v1/payables/?service_type=L`

### Transactions

Se encuentran en la ruta `/taxes/api/v1/transactions/`

#### Crear una transaction
- Utilizar metodo POST
- JSON de ejemplo para el body del request:
```json
{
	"payment_method": "cash",
	"card_number": "",
	"payment_import": "1200",
	"barcode": "1234567893",
	"payment_date": "2022-04-17"
}
```

#### Listar transactions
- Utilizar método GET
- Definir parametro start_date y end_date.
- Transactions de abril: `/taxes/api/v1/transactions/?start_date=2022-04-01&end_date=2022-04-30`

