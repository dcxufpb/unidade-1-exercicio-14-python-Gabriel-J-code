[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3382978&assignment_repo_type=AssignmentRepo)
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
