// FILE: src/routes/users/[id]/+page.server.ts

import type { PageServerLoad } from './$types';
import { getUserById } from '$lib/api';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
	// Converte para número e valida
	const userId = Number(params.id);

	if (isNaN(userId) || !Number.isInteger(userId) || userId <= 0) {
		throw error(400, 'ID de usuário (' + params.id + ') é inválido'); // Retorna status 400
	}

	try {
		const user = await getUserById(userId);
		return { user };
	} catch (err) {
		throw error(404, 'Usuário não encontrado. Error: ' + err); // Retorna status 404
	}
};
