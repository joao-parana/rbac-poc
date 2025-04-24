<!-- FILE: src/routes/users/[id]/+page.svelte -->

<script lang="ts">
	import { getUsers, updateUser } from '$lib/api';
	import { UserGroupEnum } from '$lib/models';
	import { onMount } from 'svelte';

	export let data; // SvelteKit carrega props via `load`

	let user = data.user;

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
