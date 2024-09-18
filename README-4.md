[Accessing OCI Object Storage using Instance Principals](https://medium.com/@deepalimittal23/accessing-oci-object-storage-using-instance-principals-203ac93cb77)

Lista de verificación para configurar Instance Principals en OCI

 Crear una instancia de cómputo en OCI
 Crear un Dynamic Group

 Ir a Identity & Security > Dynamic Groups
 Crear nuevo Dynamic Group
 Definir regla: ANY {instance.compartment.id = 'OCID_del_compartimento'}


 Crear una política

 Ir a Identity & Security > Policies
 Crear nueva política en el compartimento raíz
 Añadir declaraciones:
CopyAllow dynamic-group [Nombre-del-Dynamic-Group] to use generative-ai-family in compartment [Nombre-del-compartimento]
Allow dynamic-group [Nombre-del-Dynamic-Group] to use ai-service-family in compartment [Nombre-del-compartimento]



 Configurar el Virtual Cloud Network (VCN)

 Verificar ruta de salida a Internet (Internet Gateway o NAT Gateway)
 Configurar reglas de seguridad para permitir tráfico saliente al endpoint de Generative AI


 Instalar el SDK de OCI en la instancia

 Ejecutar: pip install oci


 Verificar permisos de la instancia para leer su propi