# 1. Obtener la Clave Pública y Configurar la VM
Antes de conectarte, asegúrate de que la clave pública (generada como id_rsa.pub) esté configurada en la VM:

* Accede a tu VM: Usa el panel de control de tu proveedor de nube para acceder a tu máquina virtual o a la interfaz de administración de la red.

Añadir la clave pública a la VM:

Conéctate a tu VM usando un cliente SSH.
Abre el archivo ~/.ssh/authorized_keys en la VM (si no existe, créalo).
Copia el contenido de tu archivo id_rsa.pub y pégalo en el archivo authorized_keys en la VM.
Guarda y cierra el archivo.

# 2. Configurar Visual Studio Code para Conexión Remota

Abrir VS Code: Inicia Visual Studio Code en tu computadora.

Configurar la Extensión Remote - SSH:

- Abre el panel de extensiones en VS Code (Ctrl+Shift+X o Cmd+Shift+X en macOS).
- Busca e instala la extensión Remote - SSH si aún no lo has hecho.

Configurar la Conexión SSH:

Abre la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P en macOS).
Escribe Remote-SSH: Add New SSH Host... y selecciona esta opción.
Se te pedirá que ingreses la dirección del host en el formato usuario@direccion_ip, por ejemplo, ubuntu@123.45.67.89.
Selecciona el archivo de configuración SSH donde deseas guardar la configuración (por defecto ~/.ssh/config).
Ejemplo de configuración en ~/.ssh/config:

Host mi-vm
    HostName 123.45.67.89
    User ubuntu
    IdentityFile C:\Users\TuNombreDeUsuario\.ssh\id_rsa
Asegúrate de reemplazar 123.45.67.89 con la IP pública de tu VM y ubuntu con el nombre de usuario adecuado.

Conectar a la VM:

Abre la paleta de comandos (Ctrl+Shift+P o Cmd+Shift+P en macOS).
Escribe Remote-SSH: Connect to Host... y selecciona el host que configuraste (mi-vm o el nombre que elegiste).
VS Code intentará conectarse a tu VM. Si es la primera vez que te conectas, es posible que se te pida que confirmes la autenticidad del host.
Abrir la Carpeta de Proyecto en la VM:

Una vez conectado, puedes abrir una carpeta en la VM desde el menú Archivo > Abrir Carpeta....
Navega a la carpeta de tu proyecto o a la ubicación donde deseas trabajar.


# Paso 3: Instalar las dependencias previas
Antes de comenzar, asegúrate de actualizar los repositorios e instalar algunas librerías necesarias:

```bash
sudo apt update
sudo apt install -y git sqlite3 libffi-dev build-essential libssl-dev zlib1g-dev
```

### 1. Instalar pip para Python 3
Primero, asegúrate de tener Python y pip instalados:

```bash
sudo apt update
sudo apt install -y python3-pip
```

### 2. Verificar que pip esté instalado correctamente
Confirma la instalación de pip ejecutando:

```
bash
pip3 --version
```

3. Instalar las librerías necesarias
Ahora puedes instalar las dependencias con pip3:

```bash
pip3 install oracledb sentence-transformers oci
```


# Conectarse a la base de datos oracle

Quick Start: Developing Python Applications for Oracle Autonomous Database
https://www.oracle.com/database/technologies/appdev/python/quickstartpython.html