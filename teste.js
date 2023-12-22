var valor = 0
for (let i = 1; i <= 10; i += 2) {
    console.log('valor: ' + valor);
    console.log('i: ' + i);
    valor += i
}
console.log('final: ', valor);