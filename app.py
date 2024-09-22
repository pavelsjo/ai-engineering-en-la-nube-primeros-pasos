import streamlit as st
import rag
import llm

# Cargar los documentos
docs = rag.read_json('./db/data.json')

st.title('Workshops Nerdearla 2024')

# Campo de entrada para la pregunta (área de texto grande)
question = st.text_area('¿Qué preguntas tienes de los Workshops?', 
                        'Soy programador y me interesa la inteligencia artificial generativa, ¿qué workshops de Nerdearla 2024 me recomiendas?',
                        height=150)

# Toggle para activar/desactivar RAG
use_rag = st.toggle("RAG", value=True)

# Botón para obtener recomendación
if st.button('Preguntar'):
    
    with st.spinner('Buscando una respuesta...'):
        try:
            # Generar el prompt según si se activa o no el uso de RAG
            if use_rag:
                prompt = rag.augmented_prompt(question, docs)
            else:
                prompt = question

            # Llamar al modelo de lenguaje para obtener la respuesta
            res = llm.llama_chat_oci(prompt)

            # Verificar si la solicitud fue exitosa
            if res.status == 200:
                # Extraer la respuesta del modelo
                data = res.data.chat_response.choices[0].message.content[0].text
                st.subheader('Recomendación:')
                st.write(data)
            else:
                # Manejo de error en caso de que la solicitud no sea exitosa
                st.error(f"Error en la generación de la recomendación: Código {res.status}. Por favor, inténtalo de nuevo.")

        except Exception as e:
            # Manejo de excepciones generales
            st.error(f"Ocurrió un error al generar la recomendación: {str(e)}")
        

# Sección de información en la barra lateral
st.sidebar.header('Acerca de')
st.sidebar.info('''
Esta aplicación utiliza IA generativa para responder a consultas sobre workshops de Nerdearla. \n
Puedes preguntar sobre temas, speakers, horarios y cambios de los workshops. \n
También puedes activar o desactivar el modo RAG para generar respuestas basadas en los documentos.
''')