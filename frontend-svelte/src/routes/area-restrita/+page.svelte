<!-- FILE: src/routes/+page.svelte -->
<script lang="ts">
	import { logger } from '$lib/logger';
	import { getUsers } from '$lib/api';
	import type { User } from '$lib/models'; // Importe a interface
	import { UserGroupEnum } from '$lib/models'; // Importe o enum
	import TreeView from '$lib/components/TreeView.svelte';

	// Tipagem explícita do array
	let users: User[] = []; // Agora users é um array de objetos User
	let nodes: TreeNode[] = []; // Inicialmente vazio

	async function loadUsers() {
		logger.info('Obtendo Usuários');
		users = await getUsers();
		logger.info('Usuários carregados ', users);
		// Atualiza os nodes após carregar os usuários
        nodes = Object.values(UserGroupEnum).map((group) => ({
            id: group, // Use o valor do enum como ID
            name: group, // Use o valor do enum como nome
            type: 'category', // Tipo fixo ou ajustável conforme necessário
            children: users
                .filter((user) => user.groups.includes(group)) // Filtra usuários que pertencem ao grupo
                .map((user) => ({
                    id: user.id.toString(), // ID do usuário como string
                    name: user.username, // Nome do usuário
                    type: 'user', // Tipo ajustável, aqui definido como 'user'
                    children: [] // Usuários não têm filhos
                }))
        }));
	}
	$: logger.info('Carregando a página principal', users);

	// Criação dinâmica dos nodes a partir do UserGroupEnum
	/*const nodes: TreeNode[] = Object.values(UserGroupEnum).map((group) => ({
		id: group as string, // Use o valor do enum como ID
		name: group as string, // Use o valor do enum como nome
		type: 'category', // Tipo fixo ou ajustável conforme necessário
		children: users
            .filter((user) => user.groups.includes(group)) // Filtra usuários que pertencem ao grupo
            .map((user) => ({
                id: user.id.toString(), // ID do usuário como string
                name: user.username, // Nome do usuário
                type: 'user', // Tipo ajustável, aqui definido como 'user'
                children: [] // Usuários não têm filhos
            }))
	}));*/
</script>

<svelte:head>
	<title>RBAC - Principal</title>
</svelte:head>

<div class="container">
    <aside class="sidebar">
        <ul class="tree-root">
            {#each nodes as node (node.id)}
                <TreeView {node} />
            {/each}
        </ul>
    </aside>
	
	<main class="content">
		<button onclick={loadUsers}>Carregar Usuários</button>

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
	</main>
</div>

<style>
    .sidebar {
        background: #fff;
        border-right: 1px solid #e0e0e0;
        padding: 1rem;
        overflow-y: auto;
    }

    .tree-root {
        padding: 0;
        margin: 0;
    }

    .content {
        padding: 2rem;
        background-color: #f8f9fa;
    }

	.container {
        display: grid;
        grid-template-columns: minmax(300px, 25%) 1fr;
        gap: 30px;
    }
</style>