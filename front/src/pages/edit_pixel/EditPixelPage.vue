
<template>
  <h1><p>Grid Canvas</p></h1>
  <section class="pixel-canva">
    <div
      v-for="pixel in canva.pixels"
      :key="pixel"
      class="canva"
      v-bind:style="{ backgroundColor: pixel }"
      @click="onPixelClicked(pixel)"
    ></div>
  </section>

  <section id="colorPicker">
    <input
      v-for="color in selectedColor"
      :key="color"
      type="button"
      class="canva"
      v-bind:style="{ backgroundColor: color }"
      @click="onColorChange(color)"
    />
    <input
      type="color"
      id="color-4"
      v-model="selectedColor[4]"
      @click="onPickerButton(4)"
    />
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
  </section>
  <ul class="canva-info">
    <li>Title:</li>
    <input type="text" />
  </ul>

  <section class="pixel-size">
    <button
      @click="onChangeSize"
      type="button"
      class="button-add"
      id="picker__add-columns"
    >
      +
    </button>
    -----------
    <button
      @click="onSubstractSize"
      type="button"
      class="button-remove"
      id="picker__remove-columns"
    >
      -
    </button>
    {{ this.contador }}
  </section>

  <br />
  <button @click="onSaveCanva">Save</button>
  <br />
  <!-- {{ $data }} -->
</template>

<script>
import { get_canva_by_id } from "@/services/api.js";
import { canva_post } from "@/services/api.js";
export default {
  data() {
    return {
      selectedColor: ["red", "blue", "green", "yellow"],
      index: 0,
      contador: 0,
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
    async onSaveCanva() {
      let canva = this.$route.params;
      this.canva = await canva_post(canva);
    },

    onChangeSize() {
      this.contador += 1;
    },
    onSubstractSize() {
      this.contador -= 1;
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
