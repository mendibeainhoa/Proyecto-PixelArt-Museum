
<template>
  <h1>Edit Pixel</h1>
  <section>
    <div v-bind:style="{ backgroundColor: colors[0] }">A</div>
    <div v-bind:style="{ backgroundColor: colors[1] }">B</div>
    <div v-bind:style="{ backgroundColor: colors[2] }">C</div>
  </section>
  <input type="text" v-model="index" />
  <input type="text" v-model="selectedColor" />
  <p>{{ selectedColor }}</p>
  <button @click="onColorChange">colorear</button>
</template>

<script>
export default {
  data() {
    return {
      selectedColor: "",
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
</style>