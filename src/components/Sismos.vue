<template>
  <div class="container">

    <!-- 🧠 Header estilo app -->
    <div class="header">
      <h2>🌍 Último sismo en Chile</h2>
      <p class="subtitle">Monitoreo inteligente con IA</p>
    </div>

    <!-- ⏳ Loading con estilo -->
    <div v-if="loading" class="card loading">
      ⚡ Analizando actividad sísmica...
    </div>

    <!-- ❌ Error con estilo alerta -->
    <div v-if="error" class="card error">
      ⚠️ {{ error }}
    </div>

    <!-- 📊 Card principal del sismo -->
    <div v-if="!loading && sismo" class="card">

      <!-- 🔴 Badge de magnitud -->
      <div class="top">
        <span class="badge">M {{ sismo.magnitud }}</span>
        <span class="date">{{ sismo.fecha }}</span>
      </div>

      <!-- 📍 Info principal -->
      <div class="info">
        <p class="location">📍 {{ sismo.ubicacion }}</p>
        <p class="depth">🌊 Profundidad: {{ sismo.profundidad }} km</p>
      </div>

      <!-- 🤖 IA -->
      <div>
        <p class="aiTitle">Analisis de riesgo con IA:</p>
        <div class="ai">
          <p> {{ sismo.analisis }}</p>
        </div>
      </div>

    </div>

    <!-- 📭 Sin datos -->
    <p v-if="!loading && !sismo && !error" class="empty">
      📡 No hay actividad sísmica registrada
    </p>

  </div>
</template>

<script>
import { fetchSismos } from "@/services/Services";

export default {
  name: "SismosApp",

  data() {
    return {
      sismo: null,
      loading: false,
      error: null,
    };
  },

  async mounted() {
    this.loading = true;

    try {
      const response = await fetchSismos();

      if (response.error) {
        this.error = response.message;
        this.sismo = null;
        return;
      }

      this.sismo = response.data;

    } catch (e) {
      this.error = "No se pudieron cargar los sismos.";
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
/* 🌌 Fondo general */
.container {
  max-width: 500px;
  margin: auto;
  font-family: Arial, sans-serif;
}

/* 🧠 Header */
.header {
  text-align: center;
}

.subtitle {
  font-size: 12px;
  color: #777;
}

/* 📦 Cards */
.card {
  background: #111;
  color: #fff;
  padding: 30px;
  border-radius: 12px;
  margin-bottom: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

/* ⏳ loading */
.loading {
  text-align: center;
  color: #00d4ff;
}

/* ❌ error */
.error {
  background: #3a0d0d;
  color: #ff4d4d;
}

/* 🔴 magnitud */
.top {
  margin-top: 10px;
  padding-bottom: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.badge {
  background: #ff3b3b;
  padding: 5px 10px;
  border-radius: 20px;
  font-weight: bold;
}

.date {
  font-size: 15px;
  color: #aaa;
}

/* 📍 info */
.location {
  margin-top: 10px;
  font-weight: bold;
}

.depth {
  font-size: 13px;
  color: #bbb;
}

/* IA */
.aiTitle{
  margin-top: 25px;
  padding-top: 20px;
  border-top: 1px solid #333;
}

.ai {
  margin-top: 20px;
  color: #00ffb3;
  font-style: italic;
}

/* 📭 vacío */
.empty {
  text-align: center;
  color: #888;
}
</style>