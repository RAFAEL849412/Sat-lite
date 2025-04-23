class JavaRandom {
    constructor(seed) {
        // Converte o seed para um valor compatível com 48 bits
        this.seed = BigInt(seed) & BigInt(0xFFFFFFFFFFFF);
    }

    next() {
        // Fórmula do LCG usada pelo Java
        const multiplier = BigInt(25214903917);
        const addend = BigInt(11);
        const mask = BigInt(0xFFFFFFFFFFFF);

        // Calcula o próximo valor do seed
        this.seed = (this.seed * multiplier + addend) & mask;

        // Retorna os 16 bits mais significativos como um número
        return Number(this.seed >> BigInt(16));
    }
}

// Exemplo de uso
const random = new JavaRandom(12345); // Inicializa o gerador com um seed
console.log(random.next()); // Gera o próximo número pseudo-aleatório
console.log(random.next()); // Gera outro número
