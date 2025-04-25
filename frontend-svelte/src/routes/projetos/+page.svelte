<script lang="ts">
    import TreeView from '$lib/components/TreeView.svelte';
    
    const nodes: TreeNode[] = [
        {
            id: '1',
            name: 'Projeto Leilão XX/20XX',
            type: 'project',
            children: [
                {
                    id: '1-1',
                    name: 'Lote XX',
                    type: 'lote',
                    children: [
                        {
                            id: '1-1-1',
                            name: 'LT XX',
                            type: 'lt',
                            children: [
                                { id: '1-1-1-1', name: 'Gastos Administrativos', type: 'category' },
                                { id: '1-1-1-2', name: 'Fundiário', type: 'category' },
                                { id: '1-1-1-3', name: 'BOQ', type: 'category' },
                                { id: '1-1-1-4', name: 'EPC', type: 'category' },
                                { id: '1-1-1-5', name: 'Comissionamento', type: 'category' }
                            ]
                        },
                        {
                            id: '1-1-2',
                            name: 'LT XY',
                            type: 'lt',
                            children: [
                                { id: '1-1-2-1', name: 'Gastos Administrativos', type: 'category' },
                                { id: '1-1-2-2', name: 'Fundiário', type: 'category' },
                                { id: '1-1-2-3', name: 'BOQ', type: 'category' },
                                { id: '1-1-2-4', name: 'EPC', type: 'category' },
                                { id: '1-1-2-5', name: 'Comissionamento', type: 'category' }
                            ]
                        }
                    ]
                }
            ]
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
        <h1>Sistema de Cadastro de Leilão</h1>
        <!-- Formulário será adicionado aqui -->
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