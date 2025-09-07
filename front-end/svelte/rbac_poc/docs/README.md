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
compila todo o projeto e aborta no primeiro erro encontrado. Entretanto é aconselhavel
executar também `npm run check`

Quando a gente executa `npm run build` em um projeto SvelteKit (que usa Vite como ferramenta
de build), o Vite realiza várias otimizações para preparar seu aplicativo para produção.
A mensagem `vite v6.3.2 building SSR bundle for production...` aparece indicando que o Vite
está gerando um bundle SSR (Server-Side Rendering). Vamos entender cada parte:

## O que é o Vite CLI?

O Vite (pronuncia-se "veet") é um build tool moderno e extremamente rápido para aplicações web.
Ele é usado por padrão no SvelteKit e oferece:

- ⚡ HMR (Hot Module Replacement): Recarrega partes do código instantaneamente durante o desenvolvimento.
- 📦 Bundling otimizado: Empacota seu código para produção de forma eficiente.
- 🛠️ Suporte a TypeScript, Svelte, React, Vue, etc.
- 🔄 Pré-configuração para SSR (Server-Side Rendering).

O CLI do Vite (vite) é o comando que executa essas tarefas, como:

- vite dev → Inicia o servidor de desenvolvimento.
- vite build → Gera os arquivos otimizados para produção.
- vite preview → Simula o ambiente de produção localmente.

O comando vite build gera tanto o cliente comoo servidor.

```bash
ls -lA .svelte-kit/output
```

```txt
drwxr-xr-x   5 joao  staff  160 Apr 23 20:11 client
drwxr-xr-x  11 joao  staff  352 Apr 23 20:11 server
```

Nesta preparação para Deploy o Vite gerou **menos de 260KB para o servidor** e **menos de 150KB para o cliente**.

## SvelteKit vs. Svelte

O Svelte renderiza componentes de interface do usuário (UI). Você pode compor esses componentes e renderizar uma página inteira apenas com o Svelte, mas é preciso mais do que apenas o Svelte para criar um aplicativo completo.

O **SvelteKit** ajuda você a criar aplicativos web seguindo as melhores práticas modernas e fornecendo soluções para desafios comuns de desenvolvimento. Ele oferece desde funcionalidades básicas — como um roteador que atualiza sua UI quando um link é clicado — até recursos mais avançados. Sua extensa lista de recursos inclui **otimizações de build** para carregar apenas o código mínimo necessário; suporte offline; pré-carregamento de páginas antes da navegação do usuário; renderização configurável para lidar com diferentes partes do seu aplicativo no servidor via SSR (Server-Side Rendering), no navegador por meio de renderização do lado do cliente ou em tempo de build com pré-renderização; otimização de imagens; etc. Construir um aplicativo com todas as melhores práticas modernas é extremamente complicado, mas o SvelteKit faz todo o trabalho chato para você, para que possa se dedicar à parte criativa.

Ele reflete as alterações no seu código no navegador instantaneamente para fornecer uma experiência de desenvolvimento extremamente rápida e rica em recursos, aproveitando o Vite com um plugin Svelte para fazer a Substituição de Módulo a Quente (HMR - Hot Module Replacement).

## Workflow de desenvolvimento com SvelteKit

```bash
npx sv create my-app
cd my-app
npm install
npm run dev
```

## Logging no Terminal do Servidor SvelteKit (Node.js Runtime)

Quando você executa `vite dev --open` com SvelteKit, existem várias formas de escrever logs no terminal do servidor (Node.js runtime) a partir do seu código TypeScript:

- `console.log` em componentes Svelte (+page.svelte) → vai para o console do navegador
- `console.log` em arquivos `+page.ts` → também vai para o console do navegador

### Visualizando os Logs

1. Execute o servidor:

```bash
npm run dev
```

2. Os logs aparecerão no terminal onde você executou o comando
3. Faça requisições à sua aplicação para ver os logs sendo gerados

## TODO

- Use as bibliotecas SvelteKit UI.
