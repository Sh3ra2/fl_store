/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        textMain : 'var(--text-main)',
        textMediumMain : 'var(--text-medium-main)',
        textMedium : 'var(--text-medium)',
        textUnprimary : 'var(--text-unprimary)',
        'color_primary' : 'var(--color-primary)',
        backgoundUnprimary : 'var(--backgound-unprimary)',
        backgroundMedium : 'var(--background-medium)',
        backgroundMediumMain : 'var(--background-medium-main)',
        backgroundMain : 'var(--background-main)',
        backgroundDanger : '#e02424',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],

}
