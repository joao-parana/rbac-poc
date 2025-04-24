from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from rbac_poc.models import User, GroupPermissions, UpdatePermissionsRequest, UserGroupEnum, ProfileEnum
from rbac_poc.database import PERMISSIONS_DB, USERS_DB
from typing import List
from collections.abc import Callable

_dummy_ = [ProfileEnum]

class RbacPoc():

    def __init__(self, app: FastAPI):
        self.app: FastAPI = app
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:5173"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def define_rest_api_endpoints(self):
        _endpoint_methods: list[Callable] = {list_all_permissions,get_permissions, update_user, update_permissions, create_user, list_users, check_edit_permission, get_user}
        print("==== define_rest_api_endpoints", flush=True)
        # --- Endpoints de Permissões ---
        @self.app.get("/permissions/", response_model=List[GroupPermissions])
        def list_all_permissions():
            return list(PERMISSIONS_DB.values())

        @self.app.get("/permissions/{group_name}", response_model=GroupPermissions)
        def get_permissions(group_name: UserGroupEnum):
            if group_name not in PERMISSIONS_DB:
                raise HTTPException(status_code=404, detail="Group not found")
            return PERMISSIONS_DB[group_name]

        @self.app.put("/users/{user_id}")
        async def update_user(user_id: int, user: User):
            # Lógica para atualizar o usuário no banco de dados
            # ...
            return {"message": "Usuário atualizado com sucesso"}

        @self.app.put("/permissions/{group_name}")
        def update_permissions(group_name: UserGroupEnum, request: UpdatePermissionsRequest):
            if group_name not in PERMISSIONS_DB:
                raise HTTPException(status_code=404, detail="Group not found")

            current_perms = PERMISSIONS_DB[group_name].model_dump()
            update_data = request.model_dump(exclude_unset=True)  # Ignora campos não enviados

            # Atualiza apenas os campos fornecidos
            for field, value in update_data.items():
                if field != "group_name":
                    current_perms[field] = value

            PERMISSIONS_DB[group_name] = GroupPermissions(**current_perms)
            return {"message": "Permissions updated successfully"}

        # --- Endpoints de Usuários ---
        @self.app.post("/users/", response_model=User)
        def create_user(user: User):
            USERS_DB.append(user)
            return user

        @self.app.get("/users/{user_id}")
        async def get_user(user_id: int) -> User:
            # Sua lógica para buscar o usuário no banco de dados
            # Exemplo:
            # user = db.query(User).filter(User.id == user_id).first()
            user
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user

        @self.app.get("/users/", response_model=List[User])
        def list_users():
            return USERS_DB

        # --- Endpoint para verificar acessos ---
        @self.app.get("/users/{user_id}/can-edit")
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

        # TODO: Se necessário implementar check_view_permission(user_id: int), check_contribute_permission(user_id: int) e check_admin_permission(user_id: int)
