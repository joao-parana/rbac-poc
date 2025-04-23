<!-- FILE: src/routes/+page.svelte -->
<script>
    import { getUsers } from "$lib/api.js";
    let users = [];

    async function loadUsers() {
        users = await getUsers();
    }
</script>

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
        {#each users as user}
            <tr>
                <td>{user.id}</td>
                <td>{user.username}</td>
                <td>{user.groups.join(", ")}</td>
                <td>
                    <a href="/users/{user.id}">Editar</a>
                </td>
            </tr>
        {/each}
    </tbody>
</table>

<a href="/users/create">Criar Novo Usuário</a>
