<script lang="ts">
    import { get } from 'svelte/store';
    import { page } from '$app/stores';
    let { user } = $props<{
        user?: { name: string; email: string }
    }>();

    const menuItems = $state([
        { name: 'Início', path: '/' },
        { name: 'Projetos', path: '/projetos' },
        { name: 'Fornecedores', path: '/fornecedores' },
        { name: 'Documentos', path: '/documentos' }
    ]);

    let isMenuOpen = $state(false);
    let dropdownElement: HTMLElement;

    function handleClickOutside(event: MouseEvent) {
        if (dropdownElement && !dropdownElement.contains(event.target as Node)) {
            isMenuOpen = false;
        }
    }
</script>

<nav class="top-menu">
    <div class="menu-container">
        <!-- Logo -->
        <a href="/" class="logo">
            <img src="/eletrobrascepel_logo.jpeg" alt="ProCAPEX" width="48" height="48" />
            <span>ProCAPEX</span>
        </a>

        <!-- Itens do Menu -->
        <ul class="nav-links">
            {#each menuItems as item}
                <li>
                    <a href={item.path} class:active={$page.url?.pathname === item.path}>
                        {item.name}
                    </a>
                </li>
            {/each}
        </ul>

        <!-- Menu do Usuário -->
        <div class="user-menu" on:click|stopPropagation={() => (isMenuOpen = !isMenuOpen)}>
            <div class="user-avatar">
                {(user?.name?.[0]?.toUpperCase() ?? 'U')}
            </div>
            
            {#if isMenuOpen}
                <div class="dropdown" bind:this={dropdownElement} use:clickOutside={handleClickOutside}>
                    {#if user}
                        <div class="user-info">
                            <strong>{user.name}</strong>
                            <small>{user.email}</small>
                        </div>
                        <hr>
                        <a href="/perfil" class="dropdown-item">Meu Perfil</a>
                        <a href="/configuracoes" class="dropdown-item">Configurações</a>
                    {:else}
                        <a href="/login" class="dropdown-item">Login</a>
                        <a href="/registro" class="dropdown-item">Registrar</a>
                    {/if}
                    <hr>
                    <a href="/sair" class="dropdown-item text-danger">Sair</a>
                </div>
            {/if}
        </div>
    </div>
</nav>

<style>
    .top-menu {
        background: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        height: 60px;
    }

    .menu-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        height: 100%;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
        color: #2c3e50;
        font-weight: 600;
        
        svg {
            color: #3498db;
        }
    }

    .nav-links {
        display: flex;
        gap: 25px;
        margin: 0;
        padding: 0;
        list-style: none;

        a {
            text-decoration: none;
            color: #34495e;
            font-weight: 500;
            padding: 5px 0;
            position: relative;

            &.active {
                color: #3498db;
                
                &::after {
                    content: '';
                    position: absolute;
                    bottom: -8px;
                    left: 0;
                    right: 0;
                    height: 2px;
                    background: #3498db;
                }
            }

            &:hover {
                color: #2980b9;
            }
        }
    }

    .user-menu {
        position: relative;
        cursor: pointer;
    }

    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #3498db;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }

    .dropdown {
        position: absolute;
        right: 0;
        top: 50px;
        background: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        min-width: 200px;
        padding: 10px 0;

        hr {
            margin: 8px 0;
            border-color: #f0f0f0;
        }
    }

    .dropdown-item {
        display: block;
        padding: 10px 20px;
        text-decoration: none;
        color: #2c3e50;
        transition: background 0.2s;

        &:hover {
            background: #f8f9fa;
        }

        &.text-danger {
            color: #e74c3c;
        }
    }

    .user-info {
        padding: 10px 20px;
        
        small {
            display: block;
            color: #7f8c8d;
            font-size: 0.8em;
        }
    }
</style>