# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | Hit the Lottery (996A) | [Ver no Codeforces](https://codeforces.com/problemset/problem/996/A) | 800 |
| 2 | Torre de Lanches (767A) | [Ver no Codeforces](https://codeforces.com/problemset/problem/767/A) | 1100 |
| 3 | Fibonacci Cubes (2111B) | [Ver no Codeforces](https://codeforces.com/problemset/problem/2111/B) | 1100 |
  
---
 
## Problema 1 — Hit the Lottery (996A) 
 
### O que o problema pede?
O problema pede para descobrir a menor quantidade possível de notas necessárias para sacar um determinado valor em dólares. As notas disponíveis possuem valores fixos (1, 5, 10, 20 e 100), e o objetivo é utilizar o menor número de notas possível.
 
 
### Como eu resolvi?
Resolvi utilizando uma estratégia gulosa (greedy algorithm), sempre escolhendo primeiro a maior nota possível. Comecei verificando quantas notas de 100 cabiam no valor, depois 20, 10, 5 e por fim 1. Após cada etapa, atualizei o valor restante usando o operador de resto (%).
Essa abordagem funciona bem porque escolher as notas maiores primeiro sempre leva ao menor número total de notas nesse caso.
 
### Código
```python
n = int(input())

total = 0

total += n // 100
n %= 100

total += n // 20
n %= 20

total += n // 10
n %= 10

total += n // 5
n %= 5

total += n

print(total)
```
 
---
 
## Problema 2 — Torre de Lanches (767A)
 
### O que o problema pede?
O problema simula a construção de uma torre de lanches onde os maiores devem ficar na base e os menores no topo. Porém, os lanches caem em ordem aleatória, um por dia. O objetivo é imprimir quais lanches podem ser colocados na torre em cada dia, respeitando a ordem correta.
 
### Como eu resolvi?
Utilizei um set() para armazenar os lanches que já haviam chegado, mas ainda não podiam ser colocados na torre. Também criei uma variável (next_needed) para acompanhar qual era o próximo maior lanche esperado.
A cada novo lanche recebido, verificava se ele (ou outros já armazenados) poderiam ser colocados na torre naquele momento. Enquanto o próximo lanche necessário estivesse disponível, ele era removido do conjunto e adicionado à saída do dia.
Escolhi usar set() porque a verificação de existência (in) é muito rápida, o que ajuda no desempenho considerando o limite do problema.
 
### Código
```python
import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    sizes = list(map(int, input().split()))
 
    waiting = set()       
    next_needed = n       
    
    for day in range(n):
        lanche = sizes[day]
        waiting.add(lanche)
        
        placed = []
        while next_needed in waiting:
            placed.append(next_needed)
            waiting.remove(next_needed)
            next_needed -= 1
        
        if placed:
            print(*placed)
        else:
            print()
 
solve()
 
```
 
---
 
## Problema 3 — Fibonacci Cubes (2111B)
 
### O que o problema pede?
O problema pede para verificar se um conjunto de cubos com tamanhos baseados na sequência de Fibonacci consegue caber dentro de diferentes caixas. As caixas possuem largura, comprimento e altura diferentes, e os cubos precisam respeitar regras específicas de empilhamento.
 
### Como eu resolvi?
Primeiro gerei a sequência de Fibonacci necessária para os cubos do problema. Depois, para cada caixa, ordenei suas dimensões para facilitar a comparação.
A estratégia foi verificar se as dimensões da caixa eram suficientes para acomodar os maiores cubos da sequência, já que eles determinam o espaço mínimo necessário. Se a caixa atendesse às dimensões mínimas exigidas, retornava 1; caso contrário, 0.
 
### Código
```python
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    # Fibonacci
    fib = [1, 2]
    for _ in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])

    result = []

    for _ in range(m):
        dims = sorted(map(int, input().split()))

        if dims[0] >= fib[n - 1] and dims[1] >= fib[n - 1] and dims[2] >= fib[n]:
            result.append("1")
        else:
            result.append("0")

    print("".join(result))
```
---
 
## IA utilizada
 
**Qual IA você usou?**
ChatGPT
 
**Como a IA te ajudou?**
Utilizei a IA como apoio para compreender melhor os enunciados, discutir estratégias de resolução e revisar minha lógica antes de implementar o código. Em alguns momentos, também usei para entender erros encontrados durante os testes, especialmente relacionados à execução e diferenças entre ambientes de programação.
A IA funcionou como uma ferramenta de apoio ao aprendizado, me ajudando a entender o raciocínio por trás das soluções em vez de apenas entregar respostas prontas.
 
---
 
## Reflexão
 
### Dificuldades encontradas
A principal dificuldade foi interpretar alguns enunciados, especialmente os que possuem muitas regras e exemplos. Também tive desafios para entender a melhor estratégia de solução e lidar com diferenças de execução entre linguagens e ambientes, como no Codeforces.
 
 
### O que aprendi
Aprendi mais sobre resolução de problemas com algoritmos, especialmente estratégias como algoritmo guloso (greedy), uso de estruturas de dados como set() e análise de lógica antes de começar a programar.
Também aprendi a testar soluções localmente no VS Code, interpretar mensagens de erro e usar a Inteligência Artificial de forma mais estratégica para aprender e evoluir no raciocínio.
 
 
### Como foi a experiência?
A experiência foi desafiadora e ao mesmo tempo muito enriquecedora. Gostei principalmente de entender o raciocínio por trás dos problemas e perceber que, muitas vezes, a maior dificuldade está em interpretar corretamente o enunciado e encontrar o padrão da solução.
Foi uma experiência que me ajudou a praticar lógica de programação e ganhar mais confiança para resolver desafios técnicos.
