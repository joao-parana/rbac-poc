Estrutura de diretórios

```txt
src/
├── lib/
│   ├── api.js          # Cliente API
│   └── stores.js       # Svelte stores (opcional)
├── routes/
│   ├── +page.svelte    # Página principal (listagem)
│   ├── permissions/
│   │   └── +page.svelte  # Gerenciar permissões
│   └── users/
│       ├── [id]/       # Editar usuário (dynamic route)
│       │   └── +page.svelte
│       └── create/     # Criar usuário
│           └── +page.svelte
```

**Frontend:** Execute `npm run build` para gerar arquivos estáticos e servir via Nginx ou `python3 -m http.server`.
Use as bibliotecas SvelteKit UI
