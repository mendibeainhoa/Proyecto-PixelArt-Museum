<template>
  <section>
    <router-link to="/edit_pixel/new"> Crear nuevo canva</router-link>
    <h1 class="load-title">Tus creaciones de PixelArt</h1>
  </section>

  <div class="canvas-boxes">
    <section class="canvas-section" v-for="canva in canvas" :key="canva.id">
      <div class="title-button">
        <router-link :to="{ path: '/edit_pixel/' + canva.id }">
          <p class="title-canva">{{ canva.name }}</p>
        </router-link>
        <button class="delete-button" @click="onDeleteCanva(canva.id)">
          <span> X </span>
        </button>
      </div>
      <div class="pixel-canva">
        <div
          v-for="pixel in canva.pixels"
          :key="pixel"
          class="canva"
          v-bind:style="{ backgroundColor: pixel }"
        ></div>
      </div>
    </section>
  </div>
</template>

<script>
import { get_canva } from "@/services/api.js";
import { delete_canva } from "@/services/api.js";
export default {
  data() {
    return {
      canvas: [
        {
          name: "",
          pixels: [],
        },
      ],
    };
  },

  mounted() {
    this.onLoadSprite();
  },
  methods: {
    async onLoadSprite() {
      let canva = this.$route.params;
      this.canvas = await get_canva(canva);
      console.log(this.canva);
    },
    async onDeleteCanva(id) {
      if (confirm("¿Estas seguro que quieres eliminar tu dibujo?")) {
        await delete_canva(id);
        location.reload();
        alert("Canva eliminado exitosamente");
      } else {
        console.log("Dibujo no eliminado");
      }
    },
  },
};
</script>


<style scoped >
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
* {
  margin: 0;
  padding: 0;
  font-family: "Press Start 2P", cursive;
}
.title-button {
  display: flex;
  justify-content: space-around;
  width: 100%;
  align-items: center;
  margin: 1em auto;
}

.load-title {
  margin: 1em;
  font-size: 50px;
  color: rgba(42, 121, 42, 0.637);
}
.title-canva {
  font-weight: 8px;
}
.canvas-boxes {
  display: flex;
  grid-template-rows: repeat(1, 1fr);
  flex-wrap: wrap;
  flex-direction: row;
}
.canva {
  width: 30px;
  height: 30px;
  border: 1px solid black;
}
.canvas-section {
  display: flex;
  flex-wrap: wrap;
  width: 20em;
  height: auto;
  border: solid 1px black;
  margin: 3em 1em 1em 35em;
  align-content: flex-start;
  justify-content: center;
}
</style>