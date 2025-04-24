<!-- FILE: src/routes/permissions/+page.svelte -->
<script lang="ts">
	import { getGroupPermissions, updatePermissions } from '$lib/api';
	import { UserGroupEnum } from '$lib/models'; // Enum de grupos
	import type { GroupPermissions } from '$lib/models';

	// let permissions = {};
	let permissions: GroupPermissions = {
		group_name: UserGroupEnum.VEE_USER, // Valor inicial padrão
		viewer: false,
		contributor: false,
		editor: false,
		admin: false
	};
	// let selectedGroup: UserGroupEnum = UserGroupEnum.VEE_USER;
	let selectedGroup = Object.values(UserGroupEnum)[0]; // Primeiro grupo como padrão

	async function loadPermissions() {
		permissions = await getGroupPermissions(selectedGroup);
	}

	async function savePermissions() {
		await updatePermissions(selectedGroup, permissions);
		alert('Permissões atualizadas!');
	}
</script>

<select bind:value={selectedGroup} on:change={loadPermissions}>
	{#each Object.values(UserGroupEnum) as group (group)}
		<option value={group}>{group}</option>
	{/each}
</select>

{#if permissions}
	<div>
		<h2>Permissões para {selectedGroup}</h2>
		<label>
			<input type="checkbox" bind:checked={permissions.viewer} />
			Viewer
		</label>
		<label>
			<input type="checkbox" bind:checked={permissions.contributor} />
			Contributor
		</label>
		<label>
			<input type="checkbox" bind:checked={permissions.editor} />
			Editor
		</label>
		<label>
			<input type="checkbox" bind:checked={permissions.admin} />
			Admin
		</label>
		<button on:click={savePermissions}>Salvar</button>
	</div>
{/if}
