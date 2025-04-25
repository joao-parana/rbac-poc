<script lang="ts">
	import TreeView from './TreeView.svelte';
    let { node, level = 0 } = $props<{
        node: TreeNode
        level?: number
    }>();

    let isOpen = $state(false);
    let indent = $derived.by(() => `${level * 16}px`);
</script>

<li class="tree-node">
    <div
        class="node-content"
        style:padding-left={indent}
		tabindex="0"
		role="button"
		aria-expanded={node.children?.length ? isOpen : undefined}
		aria-label={node.name}
        onclick={(event) => (node.children?.length ? (isOpen = !isOpen) : null)}
        onkeydown={(event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                if (node.children?.length) {
                    isOpen = !isOpen;
                }
            }
        }}
    >
        {#if node.children?.length}
            <span class:open={isOpen} class="caret">▶</span>
        {:else}
            <span class="spacer"></span>
        {/if}

        <span class="name">{node.name}</span>
    </div>

	{#if node.children?.length && isOpen}
		<ul class="children">
			{#each node.children as child (child.id)}
                <TreeView node={child} level={level + 1} />
			{/each}
		</ul>
	{/if}
</li>

<style>
    .tree-node {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .node-content {
        cursor: pointer;
        padding: 8px 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: background 0.2s;
    }

    .node-content:hover {
        background: #f5f5f5;
    }

    .caret {
        transition: transform 0.2s;
        display: inline-block;
    }

    .open {
        transform: rotate(90deg);
    }

    .spacer {
        width: 16px;
        visibility: hidden;
    }

    .children {
        margin: 0;
        padding: 0;
        position: relative;
    }

    .children::before {
        content: '';
        position: absolute;
        left: 16px;
        top: 0;
        bottom: 0;
        width: 1px;
        background: #ddd;
    }
</style>