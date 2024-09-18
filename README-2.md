# Desplegar una VM en OCI con Ubuntu 22.04 Minimal (aarch64), una Base de Datos Autónoma 23c AI y una VCN

Este tutorial te guiará para crear y configurar una instancia de VM Ubuntu 22.04 Minimal en OCI utilizando la capa gratuita, además de configurar una Base de Datos Autónoma 23c AI y una red virtual (VCN).

## Prerrequisitos

1. Tener una cuenta en Oracle Cloud con acceso a la capa gratuita.
2. Acceder al [Panel de Control de OCI](https://cloud.oracle.com).

---

## Paso 1: Crear una Red Virtual (VCN)

1. En el panel de OCI, navega a **Redes** > **Redes Virtuales en la Nube (VCN)**.
2. Haz clic en **Crear VCN**.
3. Asigna un nombre a la VCN (por ejemplo, `vcn-free-tier`).
4. Selecciona la opción de **VCN con Internet Gateway y subred pública**.
5. Revisa la configuración y haz clic en **Crear**.

---

## Paso 2: Crear una VM Ubuntu 22.04 Minimal (aarch64)

1. Navega a **Instancias de cómputo** en el menú de OCI.
2. Haz clic en **Crear Instancia**.
3. Asigna un nombre a la instancia (por ejemplo, `vm-ubuntu-22-04-minimal`).
4. Selecciona la **forma** como `VM.Standard.A1.Flex` (compatible con la arquitectura aarch64 y disponible en la capa gratuita).
5. En la sección **Imagen del sistema operativo**, selecciona **Ubuntu 22.04 Minimal (aarch64)**.
6. Configura la cantidad de OCPUs (1 OCPU) y la memoria (mínimo 1 GB).
7. Asegúrate de que la instancia esté conectada a la VCN creada previamente y selecciona la **subred pública**.
9. Asegurate de cargar como opción la clave `id_rsa.pub``que creaste previamente.
8. Haz clic en **Crear** para lanzar la VM.

---

## Paso 3: Configurar una Base de Datos Autónoma 23c AI

1. Navega a **Bases de Datos** > **Base de Datos Autónoma** en el menú de OCI.
2. Haz clic en **Crear Base de Datos Autónoma**.
3. Asigna un nombre a la base de datos (por ejemplo, `adb-23c-ai`).
4. Selecciona el tipo de **Base de Datos Transaccional**.
5. En la sección de versión, selecciona **Oracle Database 23c AI**.
6. Selecciona la **VCN** que creaste en el paso 1 para conectividad.
7. Completa los detalles adicionales de configuración, como el nombre de usuario, contraseña y el tamaño de almacenamiento (los valores por defecto están optimizados para la capa gratuita).
8. Haz clic en **Crear Base de Datos**.

---


