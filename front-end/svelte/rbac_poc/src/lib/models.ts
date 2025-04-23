// Enums para Perfis e Grupos
export enum ProfileEnum {
  VIEWER = "viewer",
  CONTRIBUTOR = "contributor",
  EDITOR = "editor",
  ADMIN = "admin", // Perfil com todos os acessos
}

export enum UserGroupEnum {
  VEE_USER = "VEEuser",
  VED_USER = "VEDuser",
  VSS_USER = "VSSuser",
  SUPPLIER = "supplier",
  ADMIN = "admin",
}

// Interface de Permissões
export interface GroupPermissions {
  group_name: UserGroupEnum;
  viewer: boolean;
  contributor: boolean;
  editor: boolean;
  admin: boolean; // Sobrescreve todas as outras permissões
}

// Interface de Usuário
export interface User {
  id: number;
  username: string;
  email: string;
  groups: UserGroupEnum[]; // Um usuário pode estar em múltiplos grupos
  is_active: boolean;
}

// Requisição para atualizar permissões
export interface UpdatePermissionsRequest {
  group_name: UserGroupEnum;
  viewer?: boolean | null;
  contributor?: boolean | null;
  editor?: boolean | null;
  admin?: boolean | null;
}

// Tipos úteis para formulários
export type UserForm = Omit<User, "id"> & { id?: number };
export type PermissionsForm = Omit<GroupPermissions, "group_name">;
