<!-- FILE: src/routes/users/[id]/+page.svelte -->
<script lang="ts">
	import { updateUser } from '$lib/api';
	import { UserGroupEnum } from '$lib/models';
	import type { PageData } from './$types';
	import type { User } from '$lib/models';
	// import { onMount } from 'svelte';

	// Tipagem explícita para data
	export let data: PageData; // SvelteKit carrega props via `load`

	let user: User = data.user ?? {
		id: 0,
		username: '',
		email: '',
		groups: [],
		is_active: false
	};

	async function handleSubmit() {
		await updateUser(user.id, user);
		alert('Usuário atualizado!');
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<input type="text" bind:value={user.username} placeholder="Username" />
	<input type="email" bind:value={user.email} placeholder="Email" />

	<h3>Grupos</h3>
	{#each Object.values(UserGroupEnum) as group (group)}
		<label>
			<input
				type="checkbox"
				bind:group={user.groups}
				value={group}
				checked={user.groups.includes(group)}
			/>
			{group}
		</label>
	{/each}

	<button type="submit">Salvar</button>
</form>
