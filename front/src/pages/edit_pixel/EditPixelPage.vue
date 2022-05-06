
<template>
  <h1><p>Grid Canvas</p></h1>
  <section class="pixel-canva">
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[0] }"
      @click="onPixelClicked(0)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[1] }"
      @click="onPixelClicked(1)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[2] }"
      @click="onPixelClicked(2)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[3] }"
      @click="onPixelClicked(3)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[4] }"
      @click="onPixelClicked(4)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[5] }"
      @click="onPixelClicked(5)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[6] }"
      @click="onPixelClicked(6)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[7] }"
      @click="onPixelClicked(7)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[8] }"
      @click="onPixelClicked(8)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[9] }"
      @click="onPixelClicked(9)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[10] }"
      @click="onPixelClicked(10)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[11] }"
      @click="onPixelClicked(11)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[12] }"
      @click="onPixelClicked(12)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[13] }"
      @click="onPixelClicked(13)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[14] }"
      @click="onPixelClicked(14)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[15] }"
      @click="onPixelClicked(15)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[16] }"
      @click="onPixelClicked(16)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[17] }"
      @click="onPixelClicked(17)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[18] }"
      @click="onPixelClicked(18)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[19] }"
      @click="onPixelClicked(19)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[20] }"
      @click="onPixelClicked(20)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[21] }"
      @click="onPixelClicked(21)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[22] }"
      @click="onPixelClicked(22)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[23] }"
      @click="onPixelClicked(23)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[24] }"
      @click="onPixelClicked(24)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[25] }"
      @click="onPixelClicked(25)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[26] }"
      @click="onPixelClicked(26)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[27] }"
      @click="onPixelClicked(27)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[28] }"
      @click="onPixelClicked(28)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[29] }"
      @click="onPixelClicked(29)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[30] }"
      @click="onPixelClicked(30)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: canva.pixels[31] }"
      @click="onPixelClicked(31)"
    ></div>
  </section>

  <section id="colorPicker">
    <input
      type="button"
      class="canva"
      id="color-0"
      v-bind:style="{ backgroundColor: selectedColor[0] }"
      @click="onColorChange(0)"
    />
    <input
      type="button"
      class="canva"
      id="color-1"
      v-bind:style="{ backgroundColor: selectedColor[1] }"
      @click="onColorChange(1)"
    />
    <input
      type="button"
      class="canva"
      id="color-2"
      v-bind:style="{ backgroundColor: selectedColor[2] }"
      @click="onColorChange(2)"
    />
    <input
      type="button"
      class="canva"
      id="color-3"
      v-bind:style="{ backgroundColor: selectedColor[3] }"
      @click="onColorChange(3)"
    />
    <input
      type="color"
      id="color-4"
      v-model="selectedColor[4]"
      @click="onPickerButton(4)"
    />
  </section>
  <ul class="canva-info">
    <li>Title: {{ canva.name }}</li>
    <li>Width and height: {{ canva.width }} x {{ canva.height }}</li>
  </ul>

  <button
    type="button"
    id="borrador"
    @click="onResetColor()"
    value="Borrar color"
  >
    <img
      src="https://s3.amazonaws.com/iconbros/icons/icon_svgs/000/008/875/original/eraser.svg?1592504986"
      height="35"
      width="35"
    />
  </button>
  <br />
  <!-- <p>{{ selectedColor }}</p> -->
  <button @click="onLoadSprite">Load</button>
  <br />
  {{ $data }}
</template>

<script>
import { get_canva_by_id } from "@/services/api.js";
export default {
  data() {
    return {
      selectedColor: ["red", "blue", "green", "yellow"],

      index: 0,
      borrador: "",
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
      let canvaId = this.$route.params.id;
      if (canvaId != "new") {
        this.canva = await get_canva_by_id(canvaId);
        console.log(this.canva);
      }
    },

    onColorChange(position) {
      this.canva.pixels[this.index] = this.selectedColor[position];
      console.log(this.selectedColor[position]);
    },
    onPickerButton(position) {
      this.canva.pixels[this.index] = this.selectedColor[position];
      console.log(this.selectedColor[position]);
    },
    onPixelClicked(position) {
      this.index = position;
    },
    onResetColor() {
      this.canva.pixels[this.index] = this.borrador;
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
.pixel-canva {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-left: 40%;

  width: 17rem;
  border: solid 1px black;
}

#colorPicker {
  display: flex;
  justify-content: center;
  margin: 1em;
}
input {
  margin: 1em;
}
.canva {
  width: 30px;
  height: 30px;
  border: 1px solid black;
}
.load-button {
  font-size: 10px;
  padding: 0.2em 1em;
}
.save-button {
  font-size: 10px;
  padding: 0.2em 1em;
}
</style>

// https://codepen.io/JesusTepec/pen/pjzpOE
