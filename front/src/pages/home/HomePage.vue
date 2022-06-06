<template>
  <h1>Welcome to PixelArt Museum</h1>
  <section class="login">
    <label> Usuario </label>
    <input type="text" v-model="name" />
    <label> Password </label>
    <input type="text" v-model="password" />
    <button @click="onAccessButton">Acceder</button>
  </section>
</template>

<script>
import { login } from "@/services/auth.js";

export default {
  name: "Home",
  data() {
    return {
      name: "",
      password: "",
    };
  },
  methods: {
    isNotAllowedAccessEmptyInputs() {
      if (this.name === "" || this.password === "") {
        return false;
      } else {
        return true;
      }
    },
    async onAccessButton() {
      if (!this.isNotAllowedAccessEmptyInputs()) {
        alert(" Acceso denegado: los campos estan vacios ");
        return;
      }
      let response = await login(this.name, this.password);
      console.log(response);
      let statusLogin = response.status;

      if (statusLogin === 200) {
        this.$router.push("/load_canva");
      } else {
        alert("Acceso denegado");
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
* {
  font-family: "Press Start 2P", cursive;
}
.login {
  border: solid black 1px;
  display: grid;
  place-content: center;
}
.login,
label {
  padding: 1em;
}
.login,
input {
  margin: 0.5em;
}
.login,
button {
  margin-top: 1em;
}
</style>