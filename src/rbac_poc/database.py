from rbac_poc.models import User, GroupPermissions, UserGroupEnum

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
        viewer=True,
        contributor=True,
        editor=False
    ),
    UserGroupEnum.ADMIN: GroupPermissions(
        group_name=UserGroupEnum.ADMIN,
        admin=True  # Admin tem acesso total
    )
}

# Dados de usuários (simplificado)
USERS_DB = [
    User(
        id=1,
        username='João',
        email='joao.parana@gmail.com',
        groups=[UserGroupEnum.VSS_USER],  # Um usuário pode estar em múltiplos grupos
        is_active=True
    )
]
