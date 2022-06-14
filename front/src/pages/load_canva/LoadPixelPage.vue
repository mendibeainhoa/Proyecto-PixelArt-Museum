<template>
  <section>
    <router-link to="/edit_pixel/new"> Crear nuevo canva</router-link>
    <div>
      <button class="nes-btn" @click="$router.go(-1)">↩</button>
      <div class="user-title">
        <p>Welcome home {{ name }}</p>
      </div>
      <h1 class="load-title">Tus creaciones de PixelArt</h1>
    </div>
  </section>

  <div class="canvas-boxes">
    <section class="canvas-section" v-for="canva in canvas" :key="canva.id">
      <div class="title-button">
        <router-link :to="{ path: '/edit_pixel/' + canva.id }">
          <p class="title-canva">{{ canva.name }}</p>
        </router-link>
        <button
          class="delete-button, nes-btn is-error"
          @click="onDeleteCanva(canva.id)"
        >
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
import { getUserName } from "@/services/api.js";

export default {
  data() {
    return {
      name: "",
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
    this.userName();
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
    async userName() {
      this.name = await getUserName();
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
.user-title {
  display: flex;
  justify-content: flex-end;
  margin-right: 3em;
}
.title-button {
  display: flex;
  justify-content: space-around;
  width: 100%;
  align-items: center;
  margin: 1em auto;
}

.load-title {
  margin: 2em 0px 2em 0;
  font-size: 30px;
  color: rgba(42, 121, 42, 0.637);
}
.title-canva {
  font-weight: 8px;
}
.canvas-boxes {
  display: flex;
  grid-template-rows: repeat(1, 1fr);
  flex-wrap: wrap;
  justify-content: space-evenly;
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
  align-content: flex-start;
  justify-content: center;
}
</style>