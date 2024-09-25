![img](./image.png)
---

# AI Engineering en la Nube - Primeros Pasos

Esta guía te llevará a través del proceso de desarrollo y despliegue en [Oracle Cloud Infrastructure (OCI)](https://www.oracle.com/ar/cloud/) para construir tu primera aplicación utilizando modelos fundacionales como `LLAMA 3.1`, `prompt engineering`, y `contexto`, aprovechando principalmente la capa gratuita de OCI.

![img](./demo.gif)

Esta aplicación está diseñada para ayudar a los asistentes de **Nerdearla 2024** a obtener recomendaciones personalizadas sobre los workshops, basándose en sus intereses y preguntas. Utiliza un enfoque híbrido de búsqueda de información Contexto y generación de texto con un modelo de lenguaje grande, en este caso `LLAMA 3.1` proporcionado por Oracle Cloud Infrastructure (OCI).

#### Principales Características

1. **Campo de Entrada para Preguntas**:
   - El usuario puede ingresar preguntas relacionadas con los workshops disponibles en Nerdearla 2024, como por ejemplo:
     *"Soy programador y me interesa la inteligencia artificial generativa, ¿qué workshops de Nerdearla 2024 me recomiendas?"*
   - Este campo es dinámico, permitiendo al usuario formular cualquier tipo de consulta que le ayude a encontrar workshops relevantes.
   - Permite hacerlo altamente personalizable, muy rápidamente.

2. **Integración con RAG**:
   - La aplicación permite activar o desactivar la funcionalidad Contexto mediante un toggle.
   - **Contexto activado**: La pregunta del usuario se enriquece con información relevante obtenida de un conjunto de documentos predefinidos (`data.json`), lo que mejora la precisión de las respuestas.
   - **Contexto desactivado**: La pregunta del usuario se envía directamente al modelo de lenguaje sin ninguna modificación o enriquecimiento.

3. **Modelo de Lenguaje**:
   - La aplicación se apoya en **LLAMA 3.1**, un modelo de lenguaje basado en inteligencia artificial generativa para generar respuestas a las preguntas de los usuarios.
   - Este modelo es utilizado para interpretar la pregunta del usuario y generar una recomendación de workshop que se ajuste a sus intereses.

4. **Interfaz de Usuario Interactiva**:
   - La aplicación se construye con **Streamlit**, lo que permite una experiencia interactiva y fácil de usar.
   - Los usuarios pueden escribir preguntas, activar/desactivar la funcionalidad Contexto y recibir respuestas instantáneas.

5. **Manejo de Errores**:
   - En caso de que haya un error durante la generación de la respuesta, como una solicitud fallida al modelo de lenguaje, la aplicación maneja el error mostrando mensajes claros al usuario para que puedan intentar nuevamente.

> Puedes acceder a OCI [aquí](https://www.oracle.com/ar/cloud/free/) y crear una cuenta gratuita con $300 en créditos universales. Sigue este [tutorial de YouTube](https://www.youtube.com/watch?v=AZAb5hm1xbQ) para guiarte en el proceso.

## 1. Configuración del Entorno de Desarrollo

**Tiempo estimado**: 10 minutos

### Objetivos

- Configurar Visual Studio Code para desarrollo remoto
- Generar una clave SSH usando PowerShell

### 1.1. Instalar Visual Studio Code

1. Descarga e instala [Visual Studio Code](https://code.visualstudio.com/).
2. Abre Visual Studio Code e instala las siguientes extensiones:
   - [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### 1.2. Generar una clave SSH usando PowerShell

1. Abre PowerShell: Presiona `Win + X` y selecciona **Windows PowerShell** o **Windows Terminal**.
2. Ejecuta el siguiente comando para generar una clave SSH:
   ```powershell
   ssh-keygen -t rsa -b 4096
   ```
3. Presiona Enter para aceptar la ubicación predeterminada:  
   `C:\Users\TuNombreDeUsuario\.ssh\id_rsa`
4. Se crearán dos archivos en `~/.ssh/`:
   - `id_rsa`: Tu clave privada (guárdala de forma segura).
   - `id_rsa.pub`: Tu clave pública (esta se compartirá para autenticarte).

## 2. Configuración en OCI

**Tiempo estimado**: 10 minutos

### 2.1. Crear un Compartimiento

1. En el panel de OCI, navega a **Identity & Security** > **Compartimientos**.
2. Haz clic en **Crear Compartimiento** y asígnale un nombre (por ejemplo, `compartimiento-ai`).

### 2.2. Crear una Red Virtual (VCN)

1. En el panel de OCI, navega a **Redes** > **Redes Virtuales en la Nube (VCN)**.
2. Haz clic en **Crear VCN**.
3. Asigna un nombre a la VCN (por ejemplo, `vcn-ai-engineering`).
4. Selecciona **VCN con Internet Gateway y subred pública**.
5. Revisa la configuración y haz clic en **Crear**.

### 2.3. Crear una VM Ubuntu 22.04 Minimal

1. Navega a **Instancias de cómputo** > **Crear Instancia**.
2. Asigna un nombre (ejemplo: `vm-ubuntu-22-04-minimal`).
3. Selecciona la forma `VM.Standard.A1.Flex` (disponible en la capa gratuita).
4. Elige **Ubuntu 22.04 Minimal (aarch64)** como sistema operativo.
5. Configura 1 OCPU (Equivale a 2VCPU) y 8 GB de memoria.
6. Selecciona la subred pública de la VCN creada previamente.
7. Carga tu clave pública `id_rsa.pub` generada en el paso anterior.
8. Haz clic en **Crear**.

### 2.4. Crear un Grupo Dinámico

Para que nuestra VM pueda "autenticarse" y utilizar otros recursos en la nube, necesitamos crear un grupo dinámico:

1. En el menú de OCI, navega a **Identity & Security** >  **Domains** > **Default** > **Grupos Dinámicos**.
2. Haz clic en **Crear Grupo Dinámico**.
3. Asigna un nombre (ejemplo: `grupo-ai-engineering`).
4. Define una regla para incluir las instancias, por ejemplo:
   ```
   ANY {instance.compartment.id = 'ocid1.compartment.oc1..exampleuniqueID'}   
   ```
   Reemplaza `'ocid1.compartment.oc1..exampleuniqueID'` con el OCID de tu compartimiento.

### 2.5. Crear una Política

1. Navega a **Identity & Security** > **Policies**.
2. En el compartimiento raíz, crea una nueva política con las siguientes declaraciones:
   ```
   Allow dynamic-group [Nombre-del-Grupo-Dinámico] to use generative-ai-family in compartment [Nombre-del-Compartimiento]
   ```
   Reemplaza `[Nombre-del-Grupo-Dinámico]` y `[Nombre-del-Compartimiento]` por los nombres correspondientes.

## 3. Conectar a la VM con Visual Studio Code

1. Abre VS Code y abre la paleta de comandos (`Ctrl + Shift + P`).
2. Escribe `Remote-SSH: Add New SSH Host...` y selecciona esta opción.
3. Ingresa la dirección del host en formato `usuario@direccion_ip`, por ejemplo, `ubuntu@123.45.67.89`.
4. Abre nuevamente la paleta de comandos, escribe `Remote-SSH: Connect to Host...` y selecciona el host configurado.
5. Abre la carpeta del proyecto en la VM desde **Archivo > Abrir Carpeta...** y navega a la carpeta deseada.

## 4. Estructura de Archivos del Proyecto

**Tiempo estimado**: 10 minutos

Antes de desplegar la aplicación, es importante que la estructura de archivos sea correcta. A continuación, se muestra cómo debe estar organizada:

```
.
├── db/data.json           # Base de datos de los documentos
├── .env                   # Variables de entorno
├── .gitignore             # Archivos y carpetas ignorados por Git
├── app.py                 # Punto de entrada de la aplicación Streamlit
├── llm.py                 # Módulo para manejo del modelo de lenguaje
├── rag.py                 # Módulo para recuperación de información y generación asistida (RAG)
├── README.md              # Documentación del proyecto
├── requirements.txt       # Dependencias necesarias para ejecutar la aplicación
```

## 5. Instalar Dependencias

1. Una vez conectado a la VM, actualiza los repositorios e instala las librerías necesarias:
   ```bash
   sudo apt update
   sudo apt install -y git python3-pip
   ```
3. Verifica la versión de python:
   ```bash
   python3 --version #Python 3.10.12
   ```
3. Verifica la instalación de `pip`:
   ```bash
   pip3 --version #pip 22.0.2 
   ```
4. Instala las librerías necesarias para tu proyecto:
   ```bash
   pip3 install -r requirements.txt
   ```

### Descripción de los archivos clave

- **db/**: Contiene los documentos necesarios para el proceso de recuperación de información.
- **.env**: Archivo donde se almacenan las variables de entorno, como claves API.
- **.gitignore**: Archivos y directorios que no deben ser versionados por Git.
- **app.py**: El archivo principal de la aplicación, donde se define la lógica y la interfaz de usuario utilizando Streamlit.
- **llm.py**: Módulo que gestiona las interacciones con los modelos de lenguaje.
- **rag.py**: Módulo para la recuperación de información asistida por IA (RAG).
- **requirements.txt**: Lista de las dependencias necesarias para ejecutar la aplicación (como `streamlit`, `oci`, etc.).

## 6. Desplegar la Aplicación

Para desplegar tu aplicación con Streamlit, ejecuta el siguiente comando en la VM:

```bash
streamlit run app.py
```

Y haz tus preguntas:

- Soy programador y me interesa la inteligencia artificial generativa, ¿qué workshops de Nerdearla 2024 me recomiendas?
- ¿Algún Workshop cambio de Horario?
- ¿A que workshops puedo asistir hoy?

# 7. Que sigue?

- Usar el stream de OCI Generative AI Inference
- Usar RAG con una base de datos vectorial para que sea más rápido y use menos tokens.
   - [AI Chatbot engine with Oracle Database 23ai and OCI Generative AI Services](https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=3939&p210_wec=&session=115486261083319)
- Usar tu propio modelo llama 3.1 8B

