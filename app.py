import streamlit as st
import context
import llm

# Cargar contexto
docs = context.read_txt('./db/data.txt')

st.title('Demo Gen AI 2024')

# Campo de entrada para la pregunta (área de texto grande)
question = st.text_area('¿Qué preguntas tienes de las notas clinicas?',
                        height=150)

# Toggle para activar/desactivar contexto
use_rag = st.toggle("Contexto", value=True)

# Botón para obtener recomendación
if st.button('Preguntar'):
    
    with st.spinner('Buscando una respuesta...'):
        try:
            # Generar el prompt según si se activa o no el uso de RAG
            if use_rag:
                prompt = context.augmented_prompt(question, docs)
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
        