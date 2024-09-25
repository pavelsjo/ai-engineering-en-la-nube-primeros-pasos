import oci
from dotenv import dotenv_values

# config 
credentials = dotenv_values(".env")

# get values
compartment_id = credentials["COMPARTMENT_ID"]
model_id = credentials["MODEL_ID"]
service_endpoint = credentials["SERVICE_END_POINT"]


def llama_chat_oci(prompt, service_endpoint=service_endpoint):
    
    # Crea un autenticador basado en el rol de instancia de OCI
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    
    # Crea el cliente para el servicio de inferencia de IA generativa
    client = oci.generative_ai_inference.GenerativeAiInferenceClient(
        config={}, 
        signer=signer,
        service_endpoint=service_endpoint
    )
    
    # Crea el mensaje de entrada para el modelo
    message = oci.generative_ai_inference.models.Message(
        role="USER",
        content=[oci.generative_ai_inference.models.TextContent(text=prompt)]
    )
    
    # Crea la solicitud del chat con parámetros como temperatura, top_p, y número de tokens
    chat_request = oci.generative_ai_inference.models.GenericChatRequest(
        api_format="GENERIC", 
        messages=[message],
        max_tokens=8000, 
        temperature=1, 
        top_p=0.75
    )
    
    # Detalles del chat, incluyendo el modelo y el modo de servicio
    chat_details = oci.generative_ai_inference.models.ChatDetails(
        serving_mode=oci.generative_ai_inference.models.OnDemandServingMode(model_id=model_id),
        chat_request=chat_request,
        compartment_id=compartment_id
    )
    
    # Llama al servicio y obtiene la respuesta
    response = client.chat(chat_details)
    
    return response

