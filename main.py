from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔑 Cargar .env
load_dotenv()

app = FastAPI()

# 🔓 CORSls

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego puedes restringir a tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = "https://api.gael.cloud/general/public/sismos"

# 🔑 Cliente IA (solo si hay API KEY)
client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

# 🧠 Cache simple (evita gastar IA en cada request)
cache = {
    "ultima_magnitud": None,
    "analisis": None
}

def generar_analisis(magnitud: float) -> str:
    # 🔁 Usa cache si es misma magnitud
    if cache["ultima_magnitud"] == magnitud and cache["analisis"]:
        return cache["analisis"]

    if not client:
        return "IA no disponible."

    try:
        prompt = f"Explica en una frase simple el nivel de riesgo de un sismo de magnitud {magnitud}."

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=80
        )

        resultado = response.choices[0].message.content.strip()

        # 💾 guardar en cache
        cache["ultima_magnitud"] = magnitud
        cache["analisis"] = resultado

        return resultado

    except Exception as e:
        print("Error IA:", e)
        return "Error IA"

# 🧪 Health check (útil para Render)
@app.get("/")
def home():
    return {"status": "ok"}

# 📡 Endpoint principal
@app.get("/sismo/latest")
def get_latest_sismo():
    try:
        response = requests.get(API_URL, timeout=5)

        if response.status_code != 200:
            return {"error": True, "message": "API externa falló", "data": None}

        data = response.json()

        if not data:
            return {"error": True, "message": "Sin datos", "data": None}

        s = data[0]

        magnitud = float(s["Magnitud"])
        profundidad = int(s["Profundidad"])

        analisis = generar_analisis(magnitud)

        return {
            "error": False,
            "message": "OK",
            "data": {
                "magnitud": magnitud,
                "ubicacion": s["RefGeografica"],
                "profundidad": profundidad,
                "fecha": s["Fecha"],
                "analisis": analisis
            }
        }

    except Exception as e:
        print("Error backend:", e)
        return {"error": True, "message": "Error interno", "data": None}