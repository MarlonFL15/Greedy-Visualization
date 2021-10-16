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
