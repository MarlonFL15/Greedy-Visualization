# Greedy visualization

Implementação e visualização do algoritmo Greedy, algoritmo utilizado para resolver o problema de coloração de grafos.

## Descrição do Problema

O problema é encontrar uma maneira de colorir os vértices de um gráfico de forma que dois vértices adjacentes não sejam coloridos com a mesma cor.

O menor número de cores necessárias para colorir um gráfico G é chamado de **número cromático**.

O problema de encontrar o número cromático de um grafo é dado como NP completo, logo, não existe algoritmo eficiente o suficiente para resolvê-lo. No entanto, existem algoritmos eficientes que podem chegar em resultados aproximados

## Descrição do algoritmo Greedy

O algoritmo Greedy não garante achar o número mínimo de cores. Mas garante um limite superior de d + 1 cores, onde d é o grau máximo de um vértice no grafo.
O funcionamento do algoritmo é bem simples:

1. Pinte o primeiro vértice com a primeira cor
2. Faça o seguinte para os próximos vértices:
    
    Para cada vértice, pinte-o com a menor cor que não foi utilizada em nenhum vértice adjacente. Caso todas as cores usadas anteriormente não estejam disponíveis, adicione uma nova cor ao vértice atual.

## Implementação do algoritmo usando python

A seguir, está a implementação do algoritmo.

Observação: O algortimo recebe por parâmetro um grafo da biblioteca `networkx`

```
def greedy_coloring(G):
    number_of_nodes = G.number_of_nodes()
    
    colors = dict.fromkeys(G.nodes, -1) #Dicionario para armazenar as cores dos nós (se for -1, não foi pintado)
    
    #Pinta o primeiro nó da primeira cor
    colors[list(G.nodes)[0]] = 0

    #Começa a pintar os outros nós
    for index, node in  enumerate(G.nodes):
        available = [True] * number_of_nodes #No início, todos as cores estão disponíveis
 
        for n in G.neighbors(node): #Percorre todos os vizinhos do nó 
            if colors[n] != -1:
                available[colors[n]] = False #Se um dos vizinhos já foi pintado, altera essa cor para falso 

        #Encontra a primeira cor que está disponível
        c = 0
        
        
        while colors[node] == -1:
            if available[c]:
                colors[node] = c
            c += 1
        
    return colors

```

A função acima retorna um dicionário, em que a chave é o vértice e o valor é a cor.

## Implementação do método de Desenhar

Além da implementação do algoritmo, também é possível usar bibliotecas como `networkx` e `matplotlib` para visualizar o grafo sendo colorido pelo algoritmo.

A função recebe por parâmetro o grafo e o retorno da função `greedy_coloring`.

```
import networkx as nx
from matplotlib import pyplot as plt
import matplotlib.animation as animation

dict_colors = {
    0: 'b',
    1: 'g',
    2: 'r',
    3: 'c',
    4: 'm',
    5: 'y',    
}

fig = plt.figure()

def animate(i, colors, G):
    current_colors = [dict_colors[colors[node]] if index+1 <= i else 'k' for index, (node, color) in enumerate(colors.items())]
    fig.clear()
    nx.draw_circular(G, node_color=current_colors, with_labels=True)
    
def draw(G, colors):
    anim = animation.FuncAnimation(fig, animate, frames=G.number_of_nodes()+2, interval=500, fargs=(colors,G))
    plt.show()

```

## Como usar

O primeiro passo é importar e usar as funções que já foram criadas, e a biblioteca `networkx` para criar os gráficos.

```
from greedy_coloring import greedy_coloring
from draw import draw
import networkx as nx
```

Após fazer as importações, crie o grafo de teste para servir como parâmetro para o algoritmo


```
G = nx.Graph()
G.add_edge(5, 1)
G.add_edge(5, 2)
G.add_edge(1, 2)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(2, 7)

```

E por fim, basta chamar as funções e visualizar o algoritmo funcionando :)

```
colors = greedy_coloring(G)
draw(G, colors)
```

