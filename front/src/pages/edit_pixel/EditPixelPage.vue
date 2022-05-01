
<template>
  <h1><p>Grid Canvas</p></h1>
  <section class="pixel-canva">
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[0] }"
      @click="onPixelClicked(0)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[1] }"
      @click="onPixelClicked(1)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[2] }"
      @click="onPixelClicked(2)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[3] }"
      @click="onPixelClicked(3)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[4] }"
      @click="onPixelClicked(4)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[5] }"
      @click="onPixelClicked(5)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[6] }"
      @click="onPixelClicked(6)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[7] }"
      @click="onPixelClicked(7)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[8] }"
      @click="onPixelClicked(8)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[9] }"
      @click="onPixelClicked(9)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[10] }"
      @click="onPixelClicked(10)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[11] }"
      @click="onPixelClicked(11)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[12] }"
      @click="onPixelClicked(12)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[13] }"
      @click="onPixelClicked(13)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[14] }"
      @click="onPixelClicked(14)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[15] }"
      @click="onPixelClicked(15)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[16] }"
      @click="onPixelClicked(16)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[17] }"
      @click="onPixelClicked(17)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[18] }"
      @click="onPixelClicked(18)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[19] }"
      @click="onPixelClicked(19)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[20] }"
      @click="onPixelClicked(20)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[21] }"
      @click="onPixelClicked(21)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[22] }"
      @click="onPixelClicked(22)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[23] }"
      @click="onPixelClicked(23)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[24] }"
      @click="onPixelClicked(24)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[25] }"
      @click="onPixelClicked(25)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[26] }"
      @click="onPixelClicked(26)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[27] }"
      @click="onPixelClicked(27)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[28] }"
      @click="onPixelClicked(28)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[29] }"
      @click="onPixelClicked(29)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[30] }"
      @click="onPixelClicked(30)"
    ></div>
    <div
      class="canva"
      v-bind:style="{ backgroundColor: colors[31] }"
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
    <li>Title: {{canva.name}}</li>
    <li>Width and height: {{canva.width}} x {{canva.height}}</li>
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
  <input class="save-button" type="button" value="Save" />
  <router-link to="`/canva/{canva.id}/update`">
  <button> Load </button></router-link>
  <br />
  {{ $data }}
</template>

<script>
import { canva_get_by_id } from "@/services/api.js";
export default {
  data() {
    return {
      selectedColor: ["red", "blue", "green", "yellow"],
      colors: [
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
      index: 0,
      borrador: "",
      canva: {},
    };
  },
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      let canvaId = this.$route.params.id;
      this.canva = await canva_get_by_id(spriteId)
    },

    onColorChange(position) {
      this.colors[this.index] = this.selectedColor[position];
      console.log(this.selectedColor[position]);
    },
    onPickerButton(position) {
      this.colors[this.index] = this.selectedColor[position];
      console.log(this.selectedColor[position]);
    },
    onPixelClicked(position) {
      this.index = position;
    },
    onResetColor() {
      this.colors[this.index] = this.borrador;
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
