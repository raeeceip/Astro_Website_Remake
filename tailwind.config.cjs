/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
	theme: {
		extend: {
			colors: {
				dark: "#000000",

			},
			animation: {
				fade: 'fadeIn 5s ease-in-out',
			},
			keyframes: theme => ({
				fadeIn: {
				  '0%': { backgroundColor: theme('colors.transparent') },
				  '100': { backgroundColor: theme('') },
				},
			  }),
		},
	},
	plugins: [],
};
