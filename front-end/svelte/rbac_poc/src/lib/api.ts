// FILE: src/lib/api.ts

const API_BASE_URL = 'http://localhost:8093';

// src/lib/api.ts
import type { User, GroupPermissions, UpdatePermissionsRequest, UserGroupEnum } from './models';

// Buscar todos os usuários
export async function getUsers(): Promise<User[]> {
	const response = await fetch(`${API_BASE_URL}/users/`);
	if (!response.ok) throw new Error('Failed to fetch users');
	return await response.json();
}

// Buscar permissões de um grupo
export async function getGroupPermissions(groupName: UserGroupEnum): Promise<GroupPermissions> {
	const response = await fetch(`${API_BASE_URL}/permissions/${groupName}`);
	if (!response.ok) throw new Error('Failed to fetch permissions');
	return await response.json();
}

// Atualizar permissões
export async function updatePermissions(
	groupName: UserGroupEnum,
	data: Partial<UpdatePermissionsRequest>
): Promise<void> {
	const response = await fetch(`${API_BASE_URL}/permissions/${groupName}`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(data)
	});
	if (!response.ok) throw new Error('Failed to update permissions');
}

// Criar usuário
export async function createUser(userData: Omit<User, 'id'>): Promise<User> {
	const response = await fetch(`${API_BASE_URL}/users/`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(userData)
	});
	if (!response.ok) throw new Error('Failed to create user');
	return await response.json();
}

// Atualizar usuário
export async function updateUser(userId: number, userData: Partial<User>): Promise<User> {
	const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(userData)
	});
	if (!response.ok) throw new Error('Failed to update user');
	return await response.json();
}
