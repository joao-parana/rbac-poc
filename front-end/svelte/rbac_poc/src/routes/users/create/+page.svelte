<!-- FILE: src/routes/users/create/+page.svelte -->
<script lang="ts">
	import type { User } from '$lib/models';
	import { UserGroupEnum } from '$lib/models';

	let user: User = null;
	// let user: User = {
	// 	id: 1,
	// 	username: 'john_doe',
	// 	email: 'john@example.com',
	// 	groups: [UserGroupEnum.VEE_USER],
	// 	is_active: true
	// };

	import { createUser } from '$lib/api.js';

	// Código TypeScript de inicialização
	// ==================================
	// const emptyUserForm: UserForm = {
	//   username: '',
	//   email: '',
	//   groups: [],
	//   is_active: true
	// };

	let newUser = {
		id: 0,
		username: '',
		email: '',
		groups: [],
		is_active: true
	};

	async function handleSubmit() {
		await createUser(newUser);
		window.location.href = '/'; // Redireciona após criação
	}
</script>

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
