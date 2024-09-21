import json
import oracledb
from dotenv import load_dotenv
import os
import array
from sentence_transformers import SentenceTransformer

def read_json(ruta_archivo):
    """
    Función para leer un archivo JSON.

    :param ruta_archivo: Ruta al archivo JSON que se desea leer.
    :return: Un diccionario con los datos leídos del archivo JSON.
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error al parsear el archivo {ruta_archivo}.")
        return None


def connect_adb(user, password, dsn):
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    print("Successfully connected to Oracle Database")
    return connection

def create_table(connection, tablename):
    
    with connection.cursor() as cursor:
    # Create the table
        create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {tablename.upper()} (
                id NUMBER PRIMARY KEY,
                payload CLOB CHECK (payload IS JSON),
                vector VECTOR
            )"""
        try:
            cursor.execute(create_table_sql)
                      
        except oracledb().DatabaseError as e:
            raise
        
        connection.autocommit = True
                    
        print(f"Table {tablename} created!!")

def populate_table(connection, table_name, data):
    with connection.cursor() as cursor:
        # Truncate the table
        cursor.execute(f"truncate table {table_name}")

        prepared_data = [(row['id'], json.dumps(row['payload']), row['vector']) for row in data]

        # Insert the data
        cursor.executemany(
            f"""INSERT INTO {table_name} (id, payload, vector)
            VALUES (:1, :2, :3)""",
            prepared_data
        )

        connection.commit()

# Encode all texts in a batch
def encode(texts):
    encoder = SentenceTransformer('all-MiniLM-L12-v2')
    embeddings = encoder.encode(texts, batch_size=32, show_progress_bar=True)
    return embeddings


# load .env
load_dotenv()

# load data
path = 'sources/data.json'
docs = read_json(path)

# econde text
embeddings = encode([doc for doc in docs])

# Create structured data
data = []

for idx, (doc, embedding) in enumerate(zip(docs, embeddings)):
    
    data.append({
        'id': idx,
        'payload': doc,
        'vector': array.array("f", embedding)
    })

# define credentials
credentials = {
    "user" : os.getenv('ORACLE_ADB_USER'),
    "password": os.getenv('ORACLE_ADB_PASSWORD'),
    "dsn": os.getenv('ORACLE_ADB_DSN')
}

# create connection
connection = connect_adb(credentials["user"], credentials["password"], credentials["dsn"])

# create table
table_name = "workshops_nerdearla"
create_table(connection, table_name)
populate_table(connection, table_name, data)
