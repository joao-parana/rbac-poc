import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

// export default {
//   // Consult https://svelte.dev/docs#compile-time-svelte-preprocess
//   // for more information about preprocessors
//   preprocess: vitePreprocess(),
// }

/** @type {import('@sveltejs/vite-plugin-svelte').UserConfig} */
export default {
  // ... your other configuration
  preprocess: vitePreprocess(),
  vite: {
    // ... your other Vite configuration
    build: {
      // ... your other build configuration
      rollupOptions: {
        input: {
          main: "src/main.ts", // Or your main entry point
        },
      },
    },
  },
  compiler: {
    compatibility: {
      componentApi: 4,
    },
  },
};
