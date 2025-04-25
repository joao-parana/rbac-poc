<script lang="ts">
    import TreeView from '$lib/components/TreeView.svelte';
    
    const nodes: TreeNode[] = [
        {
            id: '1',
            name: 'Banco de cadastro de fornecedores',
            type: 'root',
            children: []
        }
    ];
</script>

<div class="container">
    <aside class="sidebar">
        <ul class="tree-root">
            {#each nodes as node (node.id)}
                <TreeView {node} />
            {/each}
        </ul>
    </aside>
    
    <main class="content">
        <h1>Sistema de Cadastro de Fornecedores</h1>
        <!-- Formulário será adicionado aqui -->
    </main>
</div>

<style>
    .layout {
        display: grid;
        grid-template-columns: 300px 1fr;
        min-height: 100vh;
    }

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

    h1 {
        color: #2c3e50;
        margin-bottom: 2rem;
    }

	.container {
        display: grid;
        grid-template-columns: minmax(300px, 25%) 1fr;
        gap: 30px;
    }
</style>