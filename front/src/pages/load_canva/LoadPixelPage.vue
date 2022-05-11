<template>
  <h1>Your canvas</h1>
  <section class="canvas-section" v-for="canva in canvas" :key="canva.id">
    {{ canva.id }}
    <div
      v-for="pixel in canva.pixels"
      :key="pixel"
      class="canva"
      v-bind:style="{ backgroundColor: pixel }"
    ></div>
  </section>
</template>

<script>
import { get_canva_by_id } from "@/services/api.js";
export default {
  data() {
    return {
      canvas: [
        {
          id: "canva-1",
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
        {
          id: "canva-2",
          pixels: [
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
            "blue",
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
      ],
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