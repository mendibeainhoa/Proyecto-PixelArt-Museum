<template>
  <div>
    <br />
    <hr />
    <div id="art">
      <div v-bind="n in 950">
        <Pixel :coloring="color" />
      </div>
    </div>
    <br />
    <hr />
    <br />
  </div>
</template>
<style scoped>
#art {
  width: 762px;
  height: 502px;
  border: 1px solid #000;
}
</style>
<script>
import Pixel from "./Pixel.vue";
export default {
  mounted() {
    console.log("Art");
  },
  computed: {
    color() {
      return this.colors.hex;
    },
  },
  props: ["colors"],
  components: {
    Pixel,
  },
};
</script>