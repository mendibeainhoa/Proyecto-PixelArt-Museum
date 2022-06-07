<template>
  <h1>Your canvas</h1>
  <section class="canvas-boxes">
    <section class="canvas-section" v-for="canva in canvas" :key="canva.id">
      <router-link :to="{ path: '/edit_pixel/' + canva.id }">
        <h1>{{ canva.name }}</h1>
      </router-link>

      <div
        v-for="pixel in canva.pixels"
        :key="pixel"
        class="canva"
        v-bind:style="{ backgroundColor: pixel }"
      ></div>
    </section>
  </section>
</template>

<script>
import { get_canva } from "@/services/api.js";
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
h1 {
  margin: 1em;
  font-size: 20px;
}
.canvas-boxes {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}
.canva {
  width: 30px;
  height: 30px;
  border: 1px solid black;
}
.canvas-section {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;

  width: 9em;
  border: solid 1px black;
  margin: 3em 1em 1em 35em;
}
</style>