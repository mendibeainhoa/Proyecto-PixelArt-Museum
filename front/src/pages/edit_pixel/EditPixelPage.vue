
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
  <p>{{ selectedColor }}</p>
  <input type="button" value="Save" />
  <input type="button" value="Load" />
</template>

<script>
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
      ],
      index: 0,
      borrador: "",
      sprites: [],
    };
  },
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/sprites");
      this.sprites = await response.json();
      console.log(this.loadData);
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
* {
  margin: 0;
  padding: 0;
}
h1 {
  margin: 1em;
}
.pixel-canva {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-left: 48em;
  margin-right: 48em;
  width: 17rem;
  border: solid 1px black;
}
div {
  position: relative;
  width: 99px;
  height: 97px;

  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
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
</style>

// https://codepen.io/JesusTepec/pen/pjzpOE
