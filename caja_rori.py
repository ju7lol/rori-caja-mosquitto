from flask import Flask, request, jsonify
from flask_cors import CORS
import paho.mqtt.publish as publish

app = Flask(__name__)
CORS(app, origins=["https://ju7lol.github.io"]) 

# CONFIGURACIÓN MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883

@app.route("/abrir", methods=["POST", "GET"])
def abrir():
    dispositivo = request.args.get("dispositivo")
    if not dispositivo:
        return jsonify({"ok": False, "mensaje": "Falta 'dispositivo'"})

    topic = f"rori/{dispositivo}"
    try:
        publish.single(
            topic=topic,
            payload="abrir",
            hostname=MQTT_BROKER,
            port=MQTT_PORT
        )
        return jsonify({"ok": True, "mensaje": f"{dispositivo} activado"})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
