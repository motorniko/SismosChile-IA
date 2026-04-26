<script>
// 📦 Importa el componente Sismos
// Este componente maneja toda la lógica de API + IA
import Sismos from './components/Sismos.vue';

export default {

  // 🏷️ Nombre del componente principal
  name: "App",

  // 🧩 Registro de componentes hijos
  components: {
    Sismos,
  },
};
</script>

<template>

  <!-- 🌌 Contenedor principal de la app -->
  <div class="app">

    <!-- 🧠 Header de la aplicación -->
    <header class="header">
      <h1>🌍 Sismos + IA</h1>
      <p>Monitoreo inteligente en tiempo real</p>
    </header>

    <!-- 📦 Contenedor del contenido -->
    <main class="content">

      <!-- 🔌 Componente que muestra los sismos -->
      <Sismos />

    </main>

  </div>

</template>

<style scoped>

/* 🌌 Fondo general de la app */
.app {
  min-height: 100vh;
  background: #0b0f14;
  color: #e6f1ff;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Arial, sans-serif;
}

/* 🧠 Header superior */
.header {
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;

}

.header h1 {
  margin: 0;
  font-size: 28px;
  color: #00d4ff;
}

.header p {
  margin: 5px 0 0;
  font-size: 13px;
  color: #8892a6;
}

/* 📦 Contenido principal */
.content {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 20px;
}

</style>