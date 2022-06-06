import config from "/config.js";

export async function login(name, password) {
  const settings = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      password: password,
    }),
  };
  const response = fetch(`${config.AUTH_PATH}/login`, settings);
  return response;
}
