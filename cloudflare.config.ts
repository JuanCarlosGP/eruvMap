import { defineConfig } from "cf/config";

export default defineConfig({
  worker: {
      "name": "eruv",
      "compatibilityDate": "2026-10-19",
    "observability": {
      "enabled": true
    },
    "assets": {
      "notFoundHandling": "single-page-application"
    },
    "domains": ["eruvpedia.com", "www.eruvpedia.com"]
  }
});
