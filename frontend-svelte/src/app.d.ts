declare global {
    declare module 'uuid';
    
    type TreeNode = {
        id: string
        name: string
        type: 'root' | 'project' | 'lote' | 'lt' | 'se' | 'category'
        children?: TreeNode[]
    };
}

export {};