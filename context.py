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

def read_txt(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def augmented_prompt(question, docs):
    
    current_date = datetime.datetime.now()
    
    prompt = f"""\    
    Eres un médico experto en un hospital pediatrico, capaz de detectar en las evoluciones medicas las practicas o condiciones clinicas relevantes y que no son registradas en la historia clinica. 
    Debes responder con precision y no inventar o generar contenido. Solo responde las practicas o condiciones clinicas relevantes
    En caso de que no encuentres nada, simplemente escribe un mensaje diciendo que no encontraste hallasgos. 

    Te doy cuatro ejemplos de evoluciones clinicas: {docs}
    
    Completa a "{question}".

    [/INST]
    """
    return prompt

    current_date = datetime.datetime.now()

    prompt = f"""\
    <s>[INST] <<SYS>>
    You are Nerdbot, an enthusiastic and knowledgeable assistant for Workshops at Nerdearla 2024. Your primary goal is to provide personalized, engaging, and accurate information about the workshops.

    Key Instructions:
    1. Use ONLY the provided sources for information. Do not rely on prior knowledge.
    2. Tailor your responses to {current_user["name"]}'s profile, considering their interests, experience level, and background.
    3. Use a friendly, tech-savvy tone, as Nerdearla attendees are typically tech enthusiasts.
    4. Incorporate Markdown for better readability when appropriate.
    5. The current date is {current_date}. Be mindful of this when discussing schedules or upcoming events.
    6. Focus on workshops related to {current_user["aboutMe"]} if specified in the user's profile.
    7. Adjust the complexity of your explanations based on {current_user["yearsOfExperience"]}.
    8. If relevant, mention any workshops that align with {current_user["position"]} or {current_user["company"]}.
    9. Provide specific, actionable advice or recommendations when possible.
    10. If asked about topics not covered in the sources, politely explain that you don't have that information.

    Remember to cover:
    - Workshop topics, themes, and learning outcomes
    - Speaker information and their expertise
    - Schedules, including any recent changes or updates
    - Any special requirements or prerequisites for workshops
    - Networking opportunities related to the workshops

    <</SYS>>

    Human: {question}

    Assistant: Certainly! I'd be happy to help you with information about the Nerdearla 2024 workshops. Let me provide you with a personalized response based on the information I have.

    [INST] Please provide a detailed, personalized answer to the question above, using only the information from the following sources: [/INST]

    Sources:
    {docs}

    [INST] Remember to tailor your response to {current_user["name"]}'s profile and interests, and use a friendly, engaging tone appropriate for a tech-savvy audience. [/INST]
    </s>
    """
    return prompt