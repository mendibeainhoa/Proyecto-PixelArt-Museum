
<template>
  <h1>Edit Pixel</h1>
  <section>
    <div v-bind:style="{ backgroundColor: canvas }">a</div>
    <div v-bind:style="{ backgroundColor: canvas }">b</div>
  </section>
  <input type="button" v-model="selectedColor" />
  <p>{{ selectedColor }}</p>
  <button @click="onColorChange">colorear</button>
</template>

<script>
export default {
  data() {
    return {
      canvas: ["red"],
      selectedColor: "",
    };
  },
  // methods: {
  //   onColorChange() {
  //     // contador = 0;
  //     // for ( in contador)
  //     // contador += 1
  //     // contador.push(cuadrito);

  //     this.canvas = this.selectedColor;
  //   },
  // },
};
</script>
<style>
section {
  display: flex;
  border: 1px solid black;
}
div {
  align-content: center;
  color: aliceblue;
}
</style>