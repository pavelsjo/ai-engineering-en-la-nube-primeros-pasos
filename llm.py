import oci

compartment_id = "ocid1.tenancy.oc1..aaaaaaaaogia3wprum3yvc5qhcrdcxzrtwloiusgk5dbb5uibgcayapljwtq"

#llama 3.1-70B
model_id = "ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyaiir6nnhmlgwvh37dr2mvragxzszqmz3hok52pcgmpqta"


def llama_chat_oci(prompt):
    
    # Crea un autenticador basado en el rol de instancia de OCI
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    
    # Crea el cliente para el servicio de inferencia de IA generativa
    client = oci.generative_ai_inference.GenerativeAiInferenceClient(
        config={}, signer=signer,
        service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
    )
    
    # Crea el mensaje de entrada para el modelo
    message = oci.generative_ai_inference.models.Message(
        role="USER",
        content=[oci.generative_ai_inference.models.TextContent(text=prompt)]
    )
    
    # Crea la solicitud del chat con parámetros como temperatura, top_p, y número de tokens
    chat_request = oci.generative_ai_inference.models.GenericChatRequest(
        api_format="GENERIC", messages=[message],
        max_tokens=8000, temperature=1, top_p=0.75
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

