# Unidade 1 - Exercício 14 - Python
Esse exercício foi escrito em Python e testado com pytest.

Crie mais casos de teste e os faça passar para os seguintes cenários:

 - Venda sem itens - o cupom fiscal não pode ser impresso
 - Venda com dois itens diferentes apontando para o mesmo produto - lança erro ao adicionar o item com produto repetido
 - Item de Venda com quantidade zero ou negativa - não pode ser adicionado na venda
 - Produto com valor unitário zero ou negativo - item não pode ser adicionado na venda com produto nesse estado

### Comando para configuração
`sudo -H pip3 install pytest`

### Comando para execução
`pytest`
