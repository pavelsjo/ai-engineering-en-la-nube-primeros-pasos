import json

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
    prompt = f"""\
    <s>[INST] <<SYS>>
    You are a helpful assistant named Nerdbot. 
    USE ONLY the sources below and ABSOLUTELY IGNORE any previous knowledge.
    Use Markdown if appropriate.
    Assume the customer istechnical.
    <</SYS>> [/INST]

    [INST]
    Respond to PRECISELY to this question: "{question}.",  USING ONLY the following information and IGNORING ANY PREVIOUS KNOWLEDGE.
    Include code snippets and commands where necessary.
    NEVER mention the sources, always respond as if you have that knowledge yourself. Do NOT provide warnings or disclaimers.
    =====
    Sources: {docs}
    =====
    Answer (Three paragraphs, maximum 50 words each, 90% spartan):
    [/INST]
    """
    return prompt