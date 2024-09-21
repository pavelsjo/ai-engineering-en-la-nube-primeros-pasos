import rag
from sentence_transformers import SentenceTransformer
import array
import json

encoder = SentenceTransformer('all-MiniLM-L12-v2')

credentials = rag.credentials

connection = rag.connect_adb(credentials["user"], credentials["password"], credentials["dsn"])

table_name = "workshops_nerdearla"
topK = 3

sql = f"""
    select payload, vector_distance(vector, :vector, COSINE) as score
    from {table_name}
    order by score
    fetch approx first {topK} rows only"""   

question = 'Soft Skills?'

with connection.cursor() as cursor:
  embedding = list(encoder.encode(question))
  vector = array.array("f", embedding)
  
with connection.cursor() as cursor:
  embedding = list(encoder.encode(question))
  vector = array.array("f", embedding)

  results  = []

  for (info, score, ) in cursor.execute(sql, vector=vector):
      text_content = info.read()
      results.append((score, json.loads(text_content)))
      
print(results)

# def get_answer(question, faqs):
#     # Obtener respuesta a la pregunta
#     # ...
#     return respuesta



# def procesar_pregunta(question):
#     # Procesar la pregunta
#     # ...
#     return pregunta_procesada

# def obtener_respuesta(question):
#     faqs = load_faqs('.')
#     pregunta_procesada = procesar_pregunta(question)
#     respuesta = get_answer(pregunta_procesada, faqs)
#     return respuesta

# def main():
#     question = input("Ingrese una pregunta: ")
#     respuesta = obtener_respuesta(question)
#     print("Respuesta:", respuesta)

# if __name__ == "__main__":
#     main()