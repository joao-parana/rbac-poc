<!-- FILE: src/routes/users/create/+page.svelte -->
<script lang="ts">
	import type { User } from '$lib/models';
	import { UserGroupEnum } from '$lib/models';
	import { createUser } from '$lib/api';

	// Código TypeScript de inicialização
	// ==================================
	// const emptyUserForm: UserForm = {
	//   username: '',
	//   email: '',
	//   groups: [],
	//   is_active: true
	// };

	let newUser: User = {
		id: 0,
		username: '',
		email: '',
		groups: [],
		is_active: false
	};

	async function handleSubmit() {
		if (import.meta.env.DEV) {
			console.log('newUser = ' + newUser);
		}
		await createUser(newUser);
		window.location.href = '/'; // Redireciona após criação
	}
</script>

<svelte:head>
	<title>RBAC - Criação de Usuário</title>
</svelte:head>

<form on:submit|preventDefault={handleSubmit}>
	<input type="text" bind:value={newUser.username} placeholder="Username" required />
	<input type="email" bind:value={newUser.email} placeholder="Email" required />

	<h3>Grupos</h3>
	{#each Object.values(UserGroupEnum) as group (group)}
		<label>
			<input type="checkbox" bind:group={newUser.groups} value={group} />
			{group}
		</label>
	{/each}

	<button type="submit">Criar Usuário</button>
</form>

<a href="/">Voltar para a página principal</a>
