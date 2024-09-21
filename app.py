import streamlit as st
import rag
import llm

# Cargar los documentos
docs = rag.read_json('./db/data.json')

st.title('Recomendador de Workshops Nerdearla 2024')

# Campo de entrada para la pregunta (área de texto grande)
question = st.text_area('¿Que preguntas tienes de los Workshops?', 
                        '¿Soy programador y me interesa la inteligencia artificial generativa, ¿qué workshops me recomiendas?',
                        height=150)

# Toggle para activar/desactivar RAG
use_rag = st.toggle("RAG")


# Botón para obtener recomendación
if st.button('Obtener Recomendación'):
    with st.spinner('Generando recomendación...'):
        if use_rag:
            prompt = rag.augmented_prompt(question, docs)
        else:
            prompt = question
        
        resultado = llm.llama_chat_oci(prompt)
        
        st.subheader('Recomendación:')
        st.write(resultado)

        if use_rag:
            st.info('Esta recomendación fue generada utilizando RAG.')
        else:
            st.info('Esta recomendación fue generada sin utilizar RAG.')

st.sidebar.header('Acerca de')
st.sidebar.info('''
Esta aplicación utiliza IA generativa para recomendar workshops de Nerdearla 
basados en tus intereses y experiencia. 

Puedes activar o desactivar RAG usando el toggle para ver la diferencia en las recomendaciones.
Luego, presiona 'Obtener Recomendación' para generar una sugerencia.
''')