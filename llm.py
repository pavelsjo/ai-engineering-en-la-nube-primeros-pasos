import oci

compartment_id = "ocid1.tenancy.oc1..aaaaaaaaogia3wprum3yvc5qhcrdcxzrtwloiusgk5dbb5uibgcayapljwtq"
model_id = "ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyarleil5jr7k2rykljkhapnvhrqvzx4cwuvtfedlfxet4q"

def llama_chat_oci(prompt):
    
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    client = oci.generative_ai_inference.GenerativeAiInferenceClient(
        config={}, signer=signer,
        service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
    )
    
    message = oci.generative_ai_inference.models.Message(
        role="USER",
        content=[oci.generative_ai_inference.models.TextContent(text=prompt)]
    )
    
    chat_request = oci.generative_ai_inference.models.GenericChatRequest(
        api_format="GENERIC", messages=[message],
        max_tokens=1000, temperature=1, top_p=0.75
    )
    
    chat_details = oci.generative_ai_inference.models.ChatDetails(
        serving_mode=oci.generative_ai_inference.models.OnDemandServingMode(model_id=model_id),
        chat_request=chat_request,
        compartment_id=compartment_id
    )
    
    response = client.chat(chat_details)
    print(response.data)
    return response.data.chat_response.choices[0].message.content[0].text

