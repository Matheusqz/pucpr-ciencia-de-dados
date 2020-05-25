# Atividade	Fundamentos	de Data Stream Mining

## 1 Implemente o algoritmo a seguir na linguagem de sua preferência

- Algoritmo implementado na `01-atividade.py`.

## 2 Implemente a função ecut do Hoeffding Bound, usada para calcular o erro em relação à média de uma amostra a partir de um fator de confiança delta. 

- Implementação realizada na função `ecut` dentro do `01-atividade.py`.

## 3 Use as séries fornecidas como exemplo e execute o algoritmo sobre elas e responda:

### a) Para que vc acredita que esse algoritmo é útil?

- Poderia servir como um detector de alterações, uma vez que ele só diminui sua janela se houve uma mudança significativa nos últimos tempos. Ele também pode servir como um estimador para a média atual da sequência que estamos lendo, pois, com uma alta probabilidade, partes mais antigas da janela com uma média significativamente diferente são automaticamente eliminadas.

### b) Analise os pontos indicados na saída do algoritmo. O que eles têm de diferente?

- Os pontos indicam quando a janela de analise tem médias muito destoantes, vendo a lista que fizemos os testes os valores da lista nessa parte são bem diferentes dos normais (por exemplo, passando de 0,1;0,2 ou 0,3 para 0.9).

### c) Em quais aplicações você acredita que ele pode ser utilizado? Como e quais resultados ele poderia trazer?

- Seria bem utiliza Ele poderia ser utilizada em aplicações que querem encontrar outliers ou buscar a média em um conjunto de dados.
