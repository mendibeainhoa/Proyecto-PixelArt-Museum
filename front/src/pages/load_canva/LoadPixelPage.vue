<template>
  <h1>Your canvas</h1>
  <section>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[0] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[1] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[2] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[3] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[4] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[5] }"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[6] }"
    ></div>
  </section>
</template>

<script>
import { get_canva_by_id } from "@/services/api.js";
export default {
  data() {
    return {
      canva: {
        pixels: [
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
          "white",
        ],
      },
    };
  },

  mounted() {
    this.onLoadSprite();
  },
  methods: {
    async onLoadSprite() {
      let canvaId = this.$route.params;
      this.canva = await get_canva_by_id(canvaId);
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
.canva {
  width: 30px;
  height: 30px;
  border: 1px solid black;
}
</style>