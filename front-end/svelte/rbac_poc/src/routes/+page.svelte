<!-- FILE: src/routes/+page.svelte -->
<script lang="ts">
	import { logger } from '$lib/logger';

	import { getUsers } from '$lib/api';
	import type { User } from '$lib/models'; // Importe a interface

	// Tipagem explícita do array
	let users: User[] = []; // Agora users é um array de objetos User

	async function loadUsers() {
		logger.info('Obtendo Usuários');
		users = await getUsers();
		logger.info('Usuários carregados ', users);
	}
	$: logger.info('Carregando a página principal', users);
</script>

<svelte:head>
	<title>RBAC - Principal</title>
</svelte:head>

<button on:click={loadUsers}>Carregar Usuários</button>

<table>
	<thead>
		<tr>
			<th>ID</th>
			<th>Nome</th>
			<th>Grupos</th>
			<th>Ações</th>
		</tr>
	</thead>
	<tbody>
		{#each users as user (user)}
			<tr>
				<td>{user.id}</td>
				<td>{user.username}</td>
				<td>{user.groups.join(', ')}</td>
				<td>
					<a href="/users/{user.id}" data-sveltekit-preload-data="off">Editar</a>
				</td>
			</tr>
		{/each}
	</tbody>
</table>

<a href="/users/create">Criar Novo Usuário</a>
