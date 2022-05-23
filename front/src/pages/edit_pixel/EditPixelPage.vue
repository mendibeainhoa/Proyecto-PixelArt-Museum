
<template>
  <h1><p>Grid Canvas</p></h1>
  <section class="pixel-canva">
    <div
      v-for="(pixel, index) in canva.pixels"
      :key="pixel"
      class="canva"
      v-bind:style="{ backgroundColor: pixel }"
      @click="onPixelClicked(index)"
    ></div>
  </section>

  <section id="colorPicker">
    <input
      type="button"
      class="canva"
      id="color-1"
      v-bind:style="{ backgroundColor: selectedColor[0] }"
      @click="onColorChange(0)"
    />
    <input
      type="button"
      class="canva"
      id="color-2"
      v-bind:style="{ backgroundColor: selectedColor[1] }"
      @click="onColorChange(1)"
    />
    <input
      type="button"
      class="canva"
      id="color-3"
      v-bind:style="{ backgroundColor: selectedColor[2] }"
      @click="onColorChange(2)"
    />
    <input
      type="button"
      class="canva"
      id="color-4"
      v-bind:style="{ backgroundColor: selectedColor[3] }"
      @click="onColorChange(3)"
    />
    <input
      type="color"
      id="color-5"
      v-model="selectedColor[5]"
      @click="onPickerButton(5)"
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
    <input class="name" type="text" />
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
    <br />
    <!-- {{ $data }} -->
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
      let response = canva_post(this.canva);
      if (response.status == 200) {
        alert("TU DIBUJO SE HA GUARDADO CON ÉXITO");
      }
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
      console.log(this.index);
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
.name {
  line-height: 28px;
  border: 2px solid transparent;
  border-bottom-color: #777;
  padding: 0.2rem 0;
  outline: none;
  background-color: transparent;
  color: #0d0c22;
  transition: 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
}

.name:focus,
input:hover {
  outline: none;
  padding: 0.2rem 1rem;
  border-radius: 1rem;
  border-color: #7a9cc6;
}

.name::placeholder {
  color: #777;
}

.name:focus::placeholder {
  opacity: 0;
  transition: opacity 0.3s;
}
</style>

// https://codepen.io/JesusTepec/pen/pjzpOE
