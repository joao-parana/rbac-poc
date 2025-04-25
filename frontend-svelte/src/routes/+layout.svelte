<script lang="ts">
    import TopMenuBar from '$lib/components/TopMenuBar.svelte';
    
    // Simular dados do usuário (substituir por dados reais)
    const user = {
        name: 'Iago Souza',
        email: 'iago.souza@empresa.com'
    };
</script>

<TopMenuBar {user} />

<div class="main-content">
    <slot />
</div>

<style>
    :global(body) {
        margin: 0;
        padding-top: 60px; /* Compensar altura do menu */
    }

    .main-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
</style>