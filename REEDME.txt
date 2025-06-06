# RORI Caja (versión local con Mosquitto)

Este repositorio contiene el prototipo funcional de la Caja RORI que opera con dispositivos ESP32 dentro de la **misma red local**, usando **Flask** como servidor y **Mosquitto** como broker MQTT.

---

## 🚀 ¿Qué hace?

- Expone una API en `/abrir?dispositivo=esp32/1`
- Publica un mensaje MQTT en el topic `rori/esp32/1`
- El ESP32 escucha ese topic y activa su relé al recibir `"abrir"`

---

## 📦 Requisitos

- Python 3.8 o superior
- Mosquitto instalado y corriendo localmente
- Red local compartida con los ESP32
- [Ngrok](https://ngrok.com/) para exponer el servidor local a internet

---

## 📁 Estructura

rori-caja-local/
├── caja_rori.py ← Servidor Flask
├── requirements.txt ← Librerías necesarias

---

## 🔧 Instalación y ejecución

```bash
git clone https://github.com/TU_USUARIO/rori-caja-local.git
cd rori-caja-local
pip install -r requirements.txt
python caja_rori.py

---

## 🌍 Acceso remoto con Ngrok - Pruebas

1. Instala ngrok desde https://ngrok.com/download

2. Ejecuta tu servidor:

python caja_rori.py

3. En otra terminal, corre:

ngrok http 5000

4. Copia la URL pública que aparece, como:

https://abcd1234.ngrok.io

5. Usa esa URL desde cualquier parte del mundo para abrir dispositivos:

https://abcd1234.ngrok.io/abrir?dispositivo=esp32/1

---

## 🌍 Uso en API

POST /abrir?dispositivo=esp32/1

- Esto publicará el mensaje "abrir" en el topic MQTT:

rori/esp32/1

---

## 🔌 Conexión con ESP32

Tu ESP32 debe estar conectado a la misma red WiFi y suscribirse al topic correspondiente.

Ejemplo (en Arduino):
client.setServer("IP_DE_LA_CAJA", 1883);
client.subscribe("rori/esp32/1");

---

## 🧱 Limitaciones
Funciona solo en red local

No apto para dispositivos fuera de red sin VPN o broker externo


