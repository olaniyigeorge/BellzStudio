/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
              "./main/**/*.{html,js}",
              "./stories/**/*.{html,js}",
              "./notes/**/*.{html,js}",
              "./notes/**/inspo.py",
            ],
  theme: {
    extend: {
      colors: {
        
        bellzpurple: '#700CFC',
        "mindcream": "#FFFFDB",
        "mindpurple": "#700170",
        "mindtextmetal": "#121212"
      },
      gridTemplateColumns: {
          'custom-5': 'repeat(5, 40px) '
      },
      screens: {
        // 'xs': '320px',    // Extra small devices (phones)
        'sm': '450px',    // Small devices (phones)
        'md': '600px',    // Medium devices (tablets)
        'lg': '900px',   // Large devices (laptops/desktops)
        'xl': '1024px',   // Extra large devices (large laptops/desktops)
        'xxl': '1204px',  // 2x Extra large devices
      },
      keyframes: {
        fadeIn: {
          '0%': {opacity: '0'},
          '100%': {opacity: '1'},
          
        },
        wiggle: {
          '0%, 100%': {transform: 'rotate(-5deg)'},
          '50%': {transform: 'rotate(5deg)'},
          
        },
        swivvle: {
          '0%, 100%': {transform: 'translateX(-2%)'},
          '50%': {transform: 'translate(2%)'},
          
        },
        slideRtL: {
          from: {transform: 'translateX(25%)'},
          to: {transform: 'translateX(0%)'},
        },
        slideLtR: {
          from: {transform: 'translateX(-25%)'},
          to: {transform: 'translateX(0%)'},
        },
        slideTtB: {
          from: {transform: 'translateY(-25%)'},
          to: {transform: 'translateY(0%)'},
        },
        slideBtT: {
          from: {transform: 'translateY(35%)'},
          to: {transform: 'translateY(0%)'},
        }
      },
      animation: {
        fadeIn: 'fadeIn 1.5s ease-in',
        wiggle: 'wiggle 1s ease-in infinite',
        swivvle: 'swivvle 1.5s ease-in-out infinite',
        slideRtL: 'slideRtL 1s ease-in-out ',
        slideLtR: 'slideLtR 1s ease-in-out ',
        slideTtB: 'slideTtB 1s ease-in-out ',
        slideBtT: 'slideBtT 1s ease-in-out ',

      },
    },
  },
  plugins: [],
}

