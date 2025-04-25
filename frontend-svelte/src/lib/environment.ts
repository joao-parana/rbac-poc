// FILE: src/lib/environment.ts
export const env = {
	isDev: import.meta.env.DEV,
	isProd: import.meta.env.PROD,
	mode: import.meta.env.MODE,
	homeUrl: import.meta.env.DEV ? 'http://localhost:5173/api' : 'https://procapex.eletrobras.com'
};

// Para use faça:
// import { env } from '$lib/environment';
// if (env.isDev) {
//   console.log('Debug info:', extraData);
// }
