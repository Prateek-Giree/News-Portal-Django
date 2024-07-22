/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/form.html"],
  theme: {
    extend: {},
  },
  plugins: [
    // ...
    require("@tailwindcss/forms"),
  ],
};
