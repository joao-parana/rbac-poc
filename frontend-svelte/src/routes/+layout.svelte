<script lang="ts">
    //export let data;
    import TopMenuBar from '$lib/components/TopMenuBar.svelte';
    
    // Simular dados do usuário (substituir por dados reais)
    const user = {
        name: 'Iago Souza',
        email: 'iago.souza@empresa.com'
    };
</script>

<div class="global-layout">
    <header>
        <h1>ProCAPEX</h1>
    </header>
    <TopMenuBar {user} />
    <div class="main-content">
        <slot />
    </div>
    <footer>
        <p>© 2025 ProCAPEX</p>
    </footer>
</div>

<style>
    .global-layout {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    header {
        background: #2c3e50;
        color: rgba(255, 255, 255, 0);
        padding: 0rem;
        background-image: url("/CAPA-LINKEDIN_labs.jpg"); /* Caminho para a imagem */
        background-size: cover; /* Faz a imagem cobrir todo o espaço do header */
        background-position: center; /* Centraliza a imagem */
        background-repeat: no-repeat; /* Evita que a imagem se repita */
        height: 100px; /* Ajuste a altura do header conforme necessário */
    }

    .main-content {
        flex: 1;
        padding: 2rem;
    }

    footer {
        background: #f8f9fa;
        text-align: center;
        padding: 1rem;
    }
</style>