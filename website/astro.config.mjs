import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  site: 'http://localhost:3000',
  vite: {
    ssr: {
      noExternal: ['@astrojs/tailwind']
    }
  }
});
