
<template>
  <div id="Contenedor">
    <h1><p>Grid Canvas</p></h1>
    <div id="contenedorCanvas">
      <canvas id="canvas1" width="400" height="300"> </canvas>
      <section>
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
      </section>
    </div>
    <!-- <input type="range" id="sizeCuadros" value="20" min="5" max="100" /> -->
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
    <p>{{ selectedColor }}</p>
    <!-- <section>
      <button class="checker" @click="onPickerButton(4)">colorear</button>
    </section> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedColor: ["red", "blue", "green", "yellow"],
      colors: ["", "", "", "", "", "", "", "", ""],
      index: 0,
    };
  },
  methods: {
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
  },
};
</script>

<style scoped >
section {
  display: flex;
  justify-content: center;
}
div {
  color: rgb(0, 0, 0);
  border: 1px solid black;
  margin: 1em;
}
#colorPicker {
  display: flex;
  justify-content: center;
}
.checker {
  margin: 1em;
}
.position {
  margin: 1em;
}
.canva {
  width: 20px;
  height: 20px;
  margin: 1em;
}
</style>

// https://codepen.io/JesusTepec/pen/pjzpOE
// https://www.w3schools.com/html/html5_canvas.asp