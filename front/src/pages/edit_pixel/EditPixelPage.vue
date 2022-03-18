
<template>
  <h1>Edit Pixel</h1>
  <section>
    <div v-bind:style="{ backgroundColor: canvas }">A</div>
    <div v-bind:style="{ backgroundColor: canvas }">B</div>
  </section>
  <input type="text" v-model="selectedColor" />
  <p>{{ selectedColor }}</p>
  <button @click="onColorChange">colorear</button>
</template>

<script>
export default {
  data() {
    return {
      canvas: "#ff0000",
      selectedColor: "",
    };
  },
  methods: {
    onColorChange() {
      this.canvas = this.selectedColor;
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