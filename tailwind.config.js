/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
              "./main/**/*.{html,js}",
              "./stories/**/*.{html,js}",
            ],
  theme: {
    extend: {
      screens: {
        'xs': '320px',    // Extra small devices (phones)
        'sm': '400px',    // Small devices (phones)
        'md': '600px',    // Medium devices (tablets)
        'lg': '900px',   // Large devices (laptops/desktops)
        'xl': '1024px',   // Extra large devices (large laptops/desktops)
        '2xl': '1204px',  // 2x Extra large devices
        // Add more breakpoints as needed
      },
    },
  },
  plugins: [],
}

