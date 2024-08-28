/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors:{
        light: {
          background: '#ffffff',
          text: '#1a202c',
          primary: '#00b4d8',
          secondary: '#4b5563',
          accent: '#10b981',
          muted: '#e5e7eb',
        },
        dark: {
          background: '#1a202c',
          text: '#ffffff',
          primary: '#00b4d8',
          secondary: '#9ca3af',
          accent: '#34d399',
          muted: '#374151',
        },
        custom: {
          background: '#fdf6e3',
          text: '#01FD62',
          primary: '#b58900',
          secondary: '#268bd2',
          accent: '#2aa198',
          muted: '#eee8d5',
        },
        light_blue: {
          text_main: '#03045e',
          text_medium_main: '#023e8a',
          text_medium: '#0077b6',
          text_unprimary: '#0096c7',
          primary: '#00b4d8',
          backgound_unprimary: '#48cae4',
          background_medium: '#90e0ef',
          background_medium_main: '#ade8f4',
          background_main: '#caf0f8'
        },
        dark_blue: {
          text_main: '#caf0f8',
          text_medium_main: '#ade8f4',
          text_medium: '#90e0ef',
          text_unprimary: '#48cae4',
          primary: '#00b4d8',
          backgound_unprimary: '#0096c7',
          background_medium: '#0077b6',
          background_medium_main: '#023e8a',
          background_main: '#03045e'
        },
        light_green:{
          text_main: '#081c15',
          text_medium_main: '#1b4332',
          text_medium: '#2d6a4f',
          text_unprimary: '#40916c',
          primary: '#52b788',
          backgound_unprimary: '#74c69d',
          background_medium: '#95d5b2',
          background_medium_main: '#b7e4c7',
          background_main: '#d8f3dc'
        }
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],

}
