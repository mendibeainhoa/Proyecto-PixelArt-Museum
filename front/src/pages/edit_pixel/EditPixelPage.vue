
<template>
  <div class="header">
    <h1>Crea tu PixelArt</h1>
    <button class="nes-btn" @click="$router.go(-1)">↩</button>
    <input
      class="name"
      type="text"
      placeholder=" titulo"
      v-model="canva.name"
    />
  </div>

  <div class="pixel-areas">
    <section class="pixel-canva">
      <div
        v-for="(pixel, idx) of canva.pixels"
        :key="idx"
        class="canva"
        v-bind:style="{ backgroundColor: pixel }"
        @click="onPixelClicked(idx)"
      ></div>
    </section>

    <section class="color-picker">
      <div class="colors, nes-input">
        <input
          v-for="color in selectedColor"
          :key="color"
          type="button"
          class="color-box"
          v-bind:style="{ backgroundColor: color }"
          @click="onColorChange(color)"
        />
        <input
          type="color"
          id="color-5"
          v-model="selectedColor[5]"
          @click="onPickerButton(5)"
        />
      </div>
      <button
        type="button"
        id="borrador"
        @click="onResetColor()"
        value="Borrar color"
        class="nes-btn"
      >
        <img
          src="https://s3.amazonaws.com/iconbros/icons/icon_svgs/000/008/875/original/eraser.svg?1592504986"
          height="35"
          width="35"
        />
      </button>

      <section class="pixel-add">
        <p>Añadir pixel</p>
        <button
          @click="onChangeSize"
          type="button"
          id="button-add"
          class="nes-btn"
        >
          +
        </button>
        <button
          @click="onSubstractSize"
          type="button"
          id="button-remove"
          class="nes-btn"
        >
          -
        </button>
      </section>
    </section>
  </div>
  <button @click="onSaveCanva" class="nes-btn is-success">Save</button>
</template>

<script>
import { get_canva_by_id } from "@/services/api.js";
import { canva_post } from "@/services/api.js";

export default {
  data() {
    return {
      selectedColor: [
        "red",
        "blue",
        "green",
        "yellow",
        "#89FA5F",
        "#58C5D6",
        "#9658ED",
        "#D65345",
        "#FAD369",
        "#2D98FA",
        "#585FD6",
        "#9658ED",
        "#C745D6",
        "#FA3E78",
      ],
      index: 0,
      contador: 0,
      borrador: "",
      canva: {
        id: "",
        name: "",
        width: 0,
        height: 0,
        pixels: Array(64).fill("white"),
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
      let response = await canva_post(this.canva);
      if (response.statusText == "OK") {
        alert("Tu diseño se ha guardado con exito");
        this.$router.push("/load_canva");
      }
      console.log(response);
    },
    async canvaBox() {
      this.canva.pixels == this.canva.pixels;
    },
    onChangeSize() {
      this.canva.pixels.push("white");
      console.log(this.canva.pixels);
    },
    onSubstractSize() {
      this.canva.pixels.pop("white");
    },
    onColorChange(color) {
      this.canva.pixels[this.index] = color;
      console.log(color);
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
.header button {
  justify-items: left;
}
.header h1 {
  margin: 1em;
  font-size: 20px;
}
.color-picker {
  display: flex;
  flex-direction: column;
  min-width: 20em;
  max-width: 10rem;
}
.color-picker,
input {
  margin-top: 2em;
}
.pixel-add {
  display: flex;
  align-items: center;
  margin-top: 1em;
}
.pixel-add p {
  text-align: left;
}
.pixel-add button {
  margin-left: 1em;
  padding: 0.3em;
}
.colors {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.pixel-canva {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 20rem;
  border: solid 1px black;
  margin: 2em 5em 2em 0;
}

input {
  margin: 1em;
}
.canva {
  width: 30px;
  height: 30px;
  border: 1px solid black;
  margin: 0;
}
.color-box {
  width: 30px;
  height: 30px;
  border: 1px solid black;
  margin: 0;
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
.return-button {
  display: flex;
  align-content: flex-start;
  margin-left: 1em;
}
.pixel-areas {
  display: flex;
  justify-content: center;
}
</style>

// https://codepen.io/JesusTepec/pen/pjzpOE
