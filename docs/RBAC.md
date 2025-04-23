Existem padrões recomendados (em inglês) amplamente utilizados em sistemas de controle de acesso (RBAC - Role-Based Access Control). Seguem sugestões de nomenclatura:

### 1. **Perfil "Somente Leitura"**

- **Read Only** (Padrão mais comum)
- **Viewer** (Alternativa comum, ex.: AWS/GCP usam "Viewer")
- **Reader** (Usado em sistemas como Microsoft Azure)

### 2. **Perfil "Inclusão e Leitura"**

- **Contributor** (Padrão comum, permite adicionar + ler, mas não editar existentes)
- **Requester** (Se for específico para solicitações)
- **Creator** (Focado na ação de criar)

### 3. **Perfil "Atualização e Leitura"**

- **Editor** (Padrão comum, permite ler + modificar, mas não ações críticas)
- **Modifier** (Menos comum, mas claro)
- **Operator** (Usado em sistemas de infraestrutura)

### Padrões de Referência:

- **AWS/GCP/Azure**: Usam termos como `Viewer`, `Contributor`, `Editor` e `Admin`.
- **CRUD (Create, Read, Update, Delete)**: Seu caso cobre combinações como:
  - Read (R) → `Viewer`
  - Create + Read (C+R) → `Contributor`
  - Read + Update (R+U) → `Editor`

### Sugestão Final:

| Função                | Nome Recomendado |
| --------------------- | ---------------- |
| Somente Leitura       | **Viewer**       |
| Inclusão + Leitura    | **Contributor**  |
| Atualização + Leitura | **Editor**       |

Se houver um perfil com **todas as permissões**, o nome padrão seria **Admin** ou **Administrator** que inclui também edição de configurações da aplicação.

Esses termos são autoexplicativos, alinhados com boas práticas de UX e padrões de mercado (ex.: Google, Microsoft). Evite siglas ou termos muito técnicos como "ReadWrite" ou "CRU" para manter a clareza.
