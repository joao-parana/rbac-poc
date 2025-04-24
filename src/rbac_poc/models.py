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
    # TODO: adicionar id: int, scope:str, lot_id: str
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
