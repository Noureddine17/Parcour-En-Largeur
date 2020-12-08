from collections import deque
import os

graph = "C:\\Users\\maroc\\Desktop\\ECOLE\\nsi-tp master\\NSI-TP-master\\Exercice Parcours en Largeur\\PourEleve"

def iterative_bfs(graph, start):
    path = graph + '\\'+ start
    os.chdir(path)
    print(path)
    visited = []
    queue = deque()
    queue.append(path)
    liste_lettre=[]

    while queue:
        node = queue.popleft()
        os.chdir(node)
        if node not in visited:
            visited.append(node)
            if 'text.txt' in os.listdir():
                with open(node+"\\text.txt","r") as file:
                    liste_lettre.append(file.read())
            unvisited = []
            for item in os.listdir():
                if item != 'text.txt':
                    if item not in visited:
                        unvisited.append(node+'\\'+item)
                queue.extend(unvisited)
    return visited, liste_lettre