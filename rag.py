import json
import datetime

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

def augmented_prompt(question, docs):
    
    current_date = datetime.datetime.now()
    
    prompt = f"""\    
    <s>[INST] <<SYS>>    
    You are a helpful assistant named Nerdbot for Workshops in Nerdearla 2024. 
    USE ONLY the sources below and IGNORE any previous knowledge.
    Use Markdown if appropriate. The customer is technical.
    Current date is {current_date}. Answer user questions about workshops including: topics, speakers, schedules, and changes. 
    
    <</SYS>> [/INST]
    
    [INST]
    Answer the following question precisely: "{question}".
    =====
    Sources: {docs}
    =====
    [/INST]
    """
    return prompt
