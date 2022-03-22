
<template>
  <h1>Edit Pixel</h1>
  <section>
    <div class="canva" v-bind:style="{ backgroundColor: colors[0] }"></div>
    <div class="canva" v-bind:style="{ backgroundColor: colors[1] }"></div>
    <div class="canva" v-bind:style="{ backgroundColor: colors[2] }"></div>
  </section>
  <input class="position" type="text" v-model="index" />
  <section id="colorPicker">
    <input
      class="canva"
      id="color-0"
      v-model="selectedColor"
      v-bind:style="{ backgroundColor: selectedColor[0] }"
    />
    <input
      class="canva"
      id="color-1"
      v-model="selectedColor"
      v-bind:style="{ backgroundColor: selectedColor[1] }"
    />
    <input
      class="canva"
      id="color-2"
      v-model="selectedColor"
      v-bind:style="{ backgroundColor: selectedColor[2] }"
    />
    <input
      class="canva"
      id="color-3"
      v-model="selectedColor"
      v-bind:style="{ backgroundColor: selectedColor[3] }"
    />
    <input type="color" id="color-4" v-model="selectedColor" />
  </section>
  <p>{{ selectedColor }}</p>
  <button class="checker" @click="onColorChange">colorear</button>
  <!-- <div id="Contenedor">
    <h1><p>Grid Canvas</p></h1>
    <div id="contenedorCanvas">
      <canvas id="canvas1" width="600" height="580"> </canvas>
    </div>
    <div id="herramientas">
      <input type="range" id="sizeCuadros" value="20" min="5" max="100" />
    </div>
  </div> -->
</template>

<script>
export default {
  data() {
    return {
      selectedColor: {
        0: "red",
        1: "blue",
        2: "green",
        3: "yellow",
        4: "purple",
      },
      colors: { 0: "red", 1: "blue", 2: "green" },
      index: 0,
    };
  },
  methods: {
    onColorChange() {
      this.colors[this.index] = this.selectedColor;
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

// https://tpec05.blogspot.com/2018/02/como-crear-una-cuadricula-de-dibujo-en.html