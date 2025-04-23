// FILE: src/lib/api.js

const API_BASE_URL = 'http://localhost:8093';

// Buscar todos os usuários
export async function getUsers() {
	const response = await fetch(`${API_BASE_URL}/users/`);
	return await response.json();
}

// Buscar permissões de um grupo
export async function getGroupPermissions(groupName) {
	const response = await fetch(`${API_BASE_URL}/permissions/${groupName}`);
	return await response.json();
}

// Atualizar usuários
export async function updateUser(userId, userData) {
	const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
		method: 'PUT', // ou 'PATCH' dependendo da sua API
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(userData)
	});

	if (!response.ok) {
		throw new Error('Falha ao atualizar usuário');
	}

	return await response.json();
}

// Atualizar permissões
export async function updatePermissions(groupName, data) {
	const response = await fetch(`${API_BASE_URL}/permissions/${groupName}`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(data)
	});
	return await response.json();
}

// Criar usuário
export async function createUser(userData) {
	const response = await fetch(`${API_BASE_URL}/users/`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(userData)
	});
	return await response.json();
}
