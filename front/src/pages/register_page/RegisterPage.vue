<template>
  <section class="register">
    <h1 class="register-title">REGISTRO</h1>
    <label for="name-area"> Nombre </label>
    <input type="text" id="name-area" name="name" v-model="register.name" />
    <label for="email-area"> Email </label>
    <input type="email" id="email-area" name="email" v-model="register.email" />
    <label for="password"> Password </label>
    <input
      type="password"
      id="password-area"
      name="password"
      v-model="register.password"
    />
    <button class="save-button" @click.prevent="onSaveButton">
      Guardar datos
    </button>
  </section>
</template>

<script>
import { users_post } from "@/services/api.js";
export default {
  data() {
    return {
      register: {
        id: "",
        name: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    isEmptyInputs() {
      if (
        this.register.name === "" ||
        this.register.email === "" ||
        this.register.password === ""
      ) {
        return false;
      } else {
        return true;
      }
    },
    async onSaveButton() {
      if (!this.isEmptyInputs()) {
        alert(" Registro denegado: los campos estan vacios ");
        return;
      }
      let response = await users_post(this.register);
      console.log(response);
      let statusLogin = response.status;

      if (statusLogin === 200) {
        this.$router.push("/");
      } else {
        alert("Registro denegado");
      }
    },
  },
};
</script>

<style scoped >
* {
  margin: 0;
  padding: 0;
  font-family: "Press Start 2P", cursive;
}
.register {
  display: grid;
  place-content: center;
  margin: 25em;
  margin-top: 1em;
  border-radius: 20px;
  border: 1px solid #11101062;
  background-color: #18161562;
  color: #a08686;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  box-shadow: 0 9px rgb(61, 58, 58);
}
.register,
label {
  padding: 1em;
}
.register,
input {
  background-color: #eee;
  padding: 12px 15px;
}
.save-button {
  margin-top: 1em;
  border-radius: 20px;
  border: 1px solid #24232362;
  background-color: #3a333262;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  box-shadow: 0 9px #999;
}
.save-button:hover {
  background-color: #242221ce;
}
</style>