<!-- FILE: src/routes/permissions/+page.svelte -->
<script>
    import { getGroupPermissions, updatePermissions } from "$lib/api.js";
    import { UserGroupEnum } from "$lib/models.js"; // Enum de grupos

    let permissions = {};
    let selectedGroup = Object.values(UserGroupEnum)[0]; // Primeiro grupo como padrão

    async function loadPermissions() {
        permissions = await getGroupPermissions(selectedGroup);
    }

    async function savePermissions() {
        await updatePermissions(selectedGroup, permissions);
        alert("Permissões atualizadas!");
    }
</script>

<select bind:value={selectedGroup} on:change={loadPermissions}>
    {#each Object.values(UserGroupEnum) as group}
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
