// 📡 Importa axios, librería para hacer peticiones HTTP de forma sencilla
import axios from "axios";


// 🌐 URL del backend FastAPI
// Este endpoint entrega el último sismo procesado con análisis incluido
const API_URL = import.meta.env.VITE_API_URL;


// 🚀 Función que consume la API de sismos
// Se exporta para ser usada en componentes Vue
export async function fetchSismos() {

  try {

    // 🔗 Realiza petición GET al backend
    // await espera la respuesta antes de continuar
    const response = await axios.get(API_URL);

    // 📦 Retorna directamente los datos del backend
    // response.data contiene el JSON que envía FastAPI
    return response.data;

  } catch (error) {

    // ❌ Si ocurre un error en la petición (red, backend caído, CORS, etc.)
    console.error("Error al obtener sismos:", error);

    // ⚠️ Relanza el error para que el componente lo maneje
    throw error;
  }
}