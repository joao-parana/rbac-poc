<script lang="ts">
    import { createEventDispatcher } from "svelte";

    import type IUsuario from "../interfaces/IUsuario";
    import type IRepositorio from "../interfaces/IRepositorio";
    import { buscaRepositorios, buscaUsuario } from "../requisicoes";
    import montaUsuario from "../utils/montaUsuario";
    import Botao from "./Botao.svelte";

    let valorInput = "";

    let statusDeErro: null | number = null;

    const dispatch = createEventDispatcher<{
        aoAlterarUsuario: IUsuario | null;
    }>();

    async function aoSubmeter() {
        const respostaUsuario = await buscaUsuario(valorInput);
        const respostaRepositorios = await buscaRepositorios(valorInput);

        if (respostaUsuario.ok && respostaRepositorios.ok) {
            const dadosUsuario: IUsuario = await respostaUsuario.json();
            const dadosRepositorios: IRepositorio[] =
                await respostaRepositorios.json();

            console.log(dadosRepositorios);

            dispatch(
                "aoAlterarUsuario",
                montaUsuario(dadosUsuario, dadosRepositorios),
            );
            statusDeErro = null;
        } else {
            statusDeErro = respostaUsuario.status;
            dispatch("aoAlterarUsuario", null);
        }
    }
</script>

<form on:submit|preventDefault={aoSubmeter}>
    <input
        type="text"
        placeholder="Pesquise aqui o usuário"
        class="input"
        class:erro-input={statusDeErro === 404}
        bind:value={valorInput}
    />

    {#if statusDeErro === 404}
        <span class="erro">Usuário não encontrado!</span>
    {/if}

    <div class="botao-container">
        <Botao>
            Buscar
            <img src="/assets/lupa.svg" alt="ícone de lupa" />
        </Botao>
    </div>
</form>

<style>
    .input {
        padding: 15px 25px;
        width: calc(100% - 8.75rem);
        font-size: 1rem;
        border-radius: 8px;
        border: 1px solid #2e80fa;
        box-shadow: 0px 17px 52px rgba(222, 231, 247, 0.4);
        outline: 0;
    }

    .input::placeholder {
        font-family: "Roboto";
        font-style: italic;
        font-weight: 300;
        font-size: 19.5px;
        line-height: 26px;
        color: #6e8cba;
    }

    .erro {
        position: absolute;
        bottom: -25px;
        left: 0;
        font-style: italic;
        font-weight: normal;
        font-size: 16px;
        line-height: 19px;
        z-index: -1;
        color: #ff003e;
    }

    .erro-input {
        border: 1px solid #ff003e;
    }

    .botao-container {
        position: absolute;
        width: 9.625rem;
        right: 0;
        top: 0;
        bottom: 0;
        display: flex;
    }
</style>
