from rbac_poc.models import GroupPermissions, UserGroupEnum
from typing import List, Optional, Literal

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

# Classe User
# Classe para simular os campos/colunas como no SQLAlchemy
class Column:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: object):
        return ('eq', self.name, other)

# Classe User com os campos como atributos de classe para simular objeto de banco de dados
class User:
    id = Column('id')
    username = Column('username')
    email = Column('email')
    groups = Column('groups')
    is_active = Column('is_active')

    def __init__(self, id: int, username: str, email: str, groups: List[UserGroupEnum], is_active: bool):
        self.id = id
        self.username = username
        self.email = email
        self.groups = groups
        self.is_active = is_active

    def __repr__(self):
        return (f"User(id={self.id}, username='{self.username}', email='{self.email}', "
                f"groups={self.groups}, is_active={self.is_active})")

# Simulando o "banco de dados" e acesso via SQLAlchemy
USERS_DB: List[User] = [
    User(
        id=1,
        username='João',
        email='joao.parana@gmail.com',
        groups=[UserGroupEnum.VSS_USER],
        is_active=True
    ),
    User(
        id=2,
        username='Maria',
        email='maria@gmail.com',
        groups=[UserGroupEnum.ADMIN, UserGroupEnum.VSS_USER],
        is_active=True
    ),
    User(
        id=3,
        username='Inativo',
        email='inativo@gmail.com',
        groups=[UserGroupEnum.SUPPLIER],
        is_active=False
    )
]

class QuerySimulator:
    def __init__(self, data: List[User]):
        self.data = data
        self.filtered_data = data

    def filter(self, condition: tuple[Literal['eq'], str, object] | bool) -> 'QuerySimulator':
        op, field_name, value = condition

        if op == 'eq':
            self.filtered_data = [
                user for user in self.filtered_data
                if getattr(user, field_name) == value
            ]

        return self

    def first(self) -> Optional[User]:
        return self.filtered_data[0] if self.filtered_data else None

# Função que simula o db.query
def query() -> QuerySimulator:
    return QuerySimulator(USERS_DB)

# Função principal para testar
def main():
    print("=== Teste 1: Buscar usuário com id == 2 ===")
    user_id = 2
    user = query().filter(User.id == user_id).first()
    print(user)  # Deve retornar Maria

    print("\n=== Teste 2: Buscar usuário com id == 99 (inexistente) ===")
    user = query().filter(User.id == 99).first()
    print(user)  # Deve retornar None

    print("\n=== Teste 3: Buscar usuário com username == 'João' ===")
    user = query().filter(User.username == 'João').first()
    print(user)  # Deve retornar João

    print("\n=== Teste 4: Buscar usuário inativo ===")
    user = query().filter(User.is_active == False).first()
    print(user)  # Deve retornar o usuário inativo

if __name__ == "__main__":
    main()
