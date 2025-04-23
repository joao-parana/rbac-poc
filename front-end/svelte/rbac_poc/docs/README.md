## Estrutura de diretórios

```txt
tree -I node_modules svelte/rbac_poc
svelte/rbac_poc
├── README.md             # README gerado automaticamente pelo comando npx sv create rbac_poc
├── docs
│   └── README.md        # Este arquivo
├── eslint.config.js
├── package-lock.json     # Gerado automaticamente pelo comando npx sv create rbac_poc
├── package.json          # Gerado automaticamente pelo comando npx sv create rbac_poc
├── src
│   ├── app.d.ts         # Gerado automaticamente pelo comando npx sv create rbac_poc
│   ├── app.html         # Gerado automaticamente pelo comando npx sv create rbac_poc
│   ├── lib
│   │   ├── api.js      # Cliente API
│   │   ├── index.ts    # Gerado automaticamente pelo comando npx sv create rbac_poc
│   │   ├── models.ts
│   │   └── store.js
│   └── routes
│       ├── +page.svelte # Página principal (listagem)
│       ├── permissions  # Gerenciar permissões
│       │   └── +page.svelte
│       └── users
│           ├── [id]     # Editar usuário (dynamic route)
│           │   └── +page.svelte
│           └── create   # Página para Criar Usuário
│               └── +page.svelte
├── static
│   └── favicon.png      # Gerado automaticamente pelo comando npx sv create rbac_poc
├── svelte.config.js      # Gerado automaticamente pelo comando npx sv create rbac_poc
├── tsconfig.json         # Gerado automaticamente pelo comando npx sv create rbac_poc
└── vite.config.ts        # Gerado automaticamente pelo comando npx sv create rbac_poc
```

**Frontend:** Execute `cd rbac-poc/front-end/svelte/rbac_poc && npm run build` para gerar
arquivos estáticos e servir via Nginx ou `python3 -m http.server`. Este comando também
compila todo o projeto e aborta no primeiro erro encontrado.

**TODO:** Use as bibliotecas SvelteKit UI.
