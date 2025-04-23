Modelando a estrutura RBAC proposta em [RBAC.md](RBAC.md) usando **Pydantic** e **FastAPI**, considerando:

1. Perfis de acesso (`Viewer`, `Contributor`, `Editor` + `Admin`).
2. Grupos de usuários (`VEEuser`, `VEDuser`, `VSSuser`, `supplier`, `admin`).
3. Tabela de permissões (booleanos) para associar grupos a perfis.

---

### 1. Modelagem com Pydantic

Primeiro, definimos os modelos para **usuários**, **grupos** e **permissões**:

#### `models.py`

```python
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

# Enums para Perfis e Grupos (evitam "strings mágicas")
class ProfileEnum(str, Enum):
    VIEWER = "viewer"
    CONTRIBUTOR = "contributor"
    EDITOR = "editor"
    ADMIN = "admin"  # Perfil com todos os acessos

class UserGroupEnum(str, Enum):
    VEE_USER = "VEEuser"
    VED_USER = "VEDuser"
    VSS_USER = "VSSuser"
    SUPPLIER = "supplier"
    ADMIN = "admin"

# Modelo de Permissões (quais perfis um grupo tem)
class GroupPermissions(BaseModel):
    group_name: UserGroupEnum
    viewer: bool = False
    contributor: bool = False
    editor: bool = False
    admin: bool = False  # Sobrescreve todas as outras permissões

# Modelo de Usuário
class User(BaseModel):
    id: int
    username: str
    email: str
    groups: List[UserGroupEnum]  # Um usuário pode estar em múltiplos grupos
    is_active: bool = True

# Requisição para atualizar permissões
class UpdatePermissionsRequest(BaseModel):
    group_name: UserGroupEnum
    viewer: Optional[bool] = None
    contributor: Optional[bool] = None
    editor: Optional[bool] = None
    admin: Optional[bool] = None
```

---

### 2. Banco de Dados "Fake" (Exemplo)

Simule um banco de dados em memória para teste:

#### `database.py`

```python
from models import GroupPermissions, UserGroupEnum

# Dados iniciais das permissões por grupo
PERMISSIONS_DB = {
    UserGroupEnum.VEE_USER: GroupPermissions(
        group_name=UserGroupEnum.VEE_USER,
        viewer=True,
        contributor=False,
        editor=False
    ),
    UserGroupEnum.VED_USER: GroupPermissions(
        group_name=UserGroupEnum.VED_USER,
        viewer=True,
        contributor=True,
        editor=False
    ),
    UserGroupEnum.VSS_USER: GroupPermissions(
        group_name=UserGroupEnum.VSS_USER,
        viewer=False,
        contributor=False,
        editor=True
    ),
    UserGroupEnum.SUPPLIER: GroupPermissions(
        group_name=UserGroupEnum.SUPPLIER,
        viewer=True
    ),
    UserGroupEnum.ADMIN: GroupPermissions(
        group_name=UserGroupEnum.ADMIN,
        admin=True  # Admin tem acesso total
    )
}

# Dados de usuários (simplificado)
USERS_DB = []
```

---

### 3. Endpoints FastAPI

Crie os endpoints para gerenciar usuários e permissões:

#### `main.py`

```python
from fastapi import FastAPI, HTTPException
from models import User, GroupPermissions, UpdatePermissionsRequest, UserGroupEnum, ProfileEnum
from database import PERMISSIONS_DB, USERS_DB
from typing import List

app = FastAPI()

# --- Endpoints de Permissões ---
@app.get("/permissions/", response_model=List[GroupPermissions])
def list_all_permissions():
    return list(PERMISSIONS_DB.values())

@app.get("/permissions/{group_name}", response_model=GroupPermissions)
def get_permissions(group_name: UserGroupEnum):
    if group_name not in PERMISSIONS_DB:
        raise HTTPException(status_code=404, detail="Group not found")
    return PERMISSIONS_DB[group_name]

@app.put("/permissions/{group_name}")
def update_permissions(group_name: UserGroupEnum, request: UpdatePermissionsRequest):
    if group_name not in PERMISSIONS_DB:
        raise HTTPException(status_code=404, detail="Group not found")

    current_perms = PERMISSIONS_DB[group_name].dict()
    update_data = request.dict(exclude_unset=True)  # Ignora campos não enviados

    # Atualiza apenas os campos fornecidos
    for field, value in update_data.items():
        if field != "group_name":
            current_perms[field] = value

    PERMISSIONS_DB[group_name] = GroupPermissions(**current_perms)
    return {"message": "Permissions updated successfully"}

# --- Endpoints de Usuários ---
@app.post("/users/", response_model=User)
def create_user(user: User):
    USERS_DB.append(user)
    return user

@app.get("/users/", response_model=List[User])
def list_users():
    return USERS_DB

# --- Endpoint para verificar acessos ---
@app.get("/users/{user_id}/can-edit")
def check_edit_permission(user_id: int):
    user = next((u for u in USERS_DB if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verifica se o usuário está em algum grupo com permissão de editor ou admin
    for group in user.groups:
        perms = PERMISSIONS_DB.get(group)
        if perms and (perms.editor or perms.admin):
            return {"can_edit": True}
    return {"can_edit": False}
```

---

### 4. Testando a API

- Use `uvicorn main:app --reload` para iniciar.
- Acesse `http://localhost:8000/docs` para interagir com os endpoints.

#### Exemplos de Requests:

**Atualizar permissões do grupo `VEEuser`:**

```bash
curl -X PUT "http://localhost:8000/permissions/VEEuser" \
-H "Content-Type: application/json" \
-d '{"contributor": true}'
```

**Criar um usuário:**

```bash
curl -X POST "http://localhost:8000/users/" \
-H "Content-Type: application/json" \
-d '{"id": 1, "username": "john_doe", "email": "john@example.com", "groups": ["VEEuser"]}'
```

---

### 5. Validações Adicionais

- **Admin tem acesso total**: Se `admin=True`, ignore outras permissões.
- **Hierarquia de Grupos**: [TODO:] Se necessário, adicione lógica para herança de permissões.
- **Autenticação**: [TODO:] Integrar com `OAuth2` ou `JWT` para proteger os endpoints.

Essa estrutura é escalável e segue boas práticas de design de APIs com FastAPI.
