# Configuración del Entorno de Desarrollo

REFERENCIAS - https://apexapps.oracle.com/pls/apex/r/dbpm/livelabs/run-workshop?p210_wid=3939&p210_wec=&session=115486261083319 AI Chatbot engine with Oracle Database 23ai and OCI Generative AI Services


## Introducción

Esta guía te llevará a través del proceso de configuración para trabajar remotamente con tu las máaquinas virtuales en la nube usando **Visual Studio Code**, sigue estos pasos para configurar la conexión remota y las extensiones necesarias.

**Tiempo estimado**: 20 minutos

## Objetivos

- Configurar Visual Studio Code para desarrollo remoto
- Generar una clave ssh usando Powershell
- Instalar y configurar Jupyter Lab Extension

---

### 1. Instalar Visual Studio Code

1. Descarga e instala [Visual Studio Code](https://code.visualstudio.com/).
2. Abre Visual Studio Code y busca la extensión **Remote - SSH** en el Marketplace de extensiones.
3. Instala la extensión **Remote - SSH**.
4. Busca e instala la extensión **Python**.
5. Busca e instala la extensión **Jupyter**.

---

## Generar una clave SSH usando PowerShell

Para conectarte a tu servidor de forma segura usando Visual Studio Code, necesitas generar una clave SSH. Aquí te mostramos cómo hacerlo:

### Paso 1: Abrir PowerShell

1. Presiona `Win + X` y selecciona **Windows PowerShell** o **Windows Terminal**.
2. Navega a tu carpeta principal (por defecto es `C:\Users\TuNombreDeUsuario`).

### Paso 2: Generar el par de llaves SSH

Ejecuta el siguiente comando en PowerShell para generar tu clave SSH:

```powershell
ssh-keygen -t rsa -b 4096
```

Presiona Enter para aceptar la ubicación predeterminada 

```C:\Users\TuNombreDeUsuario\.ssh\id_rsa```

### Paso 3: Verificar la generación de las llaves
Se crearán dos archivos en ~/.ssh/:

- id_rsa: Tu clave privada (guárdala de forma segura).
- id_rsa.pub: Tu clave pública (compártela para autenticarte en servidores).