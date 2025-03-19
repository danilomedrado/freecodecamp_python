
#learn-algorithm-design-by-building-a-shortest-path-algorithm
#https://github.com/freeCodeCamp/freeCodeCamp/blob/main/curriculum/challenges/english/07-scientific-computing-with-python/learn-algorithm-design-by-building-a-shortest-path-algorithm/65576ff7888f9e96f52a4be1.md

#A graph is called a weighted graph when its edges are associated with weights, representing a distance, time or other quantitative value.
#In your case, these weights will be the distances between each node, or point in space. To represent a weighted graph you can modify your dictionary, using a list of tuples for each value.
#The first element in the tuple will be the connected node, and the second element will be an integer number indicating the distance.
#Modify my_graph['A'] into a list of tuples, considering that the A-B distance is 3 and the A-D distance is 1.
#The algorithm will start at a specified node. Then it will explore the graph to find the shortest path between the starting node, or source, and all the other nodes.
#For that your function needs two parameters: graph, and start. Add them to your function declaration.
#To keep track of the visited nodes, you need a list of all the nodes in the graph. Once a node is visited, it will be removed from that list.
#Now, replace the pass keyword with a variable named unvisited and assign it an empty list.
#Create a for loop to iterate over your graph, and use the .append() method to add each node to the end of the unvisited list.
#While the algorithm explores the graph, it should keep track of the currently known shortest distance between the starting node and the other nodes.
#Before your for loop, create a new variable named distances and assign it an empty dictionary.
#The distance from the starting node is zero, because the algorithm begins its assessment right from there.
#After appending node to unvisited in your loop, create an if statement that triggers if the node is equal to the starting node. 
#Then assign 0 to that node inside the distances dictionary.
#At the beginning, all the other nodes in the graph are considered to be at infinite distance from the source node, because the distance has not been determined yet.
#Create an else clause and assign an infinite value to the node in the distances dictionary. 
#For that, use the float() function with the string 'inf' as argument to generate a floating point number representing the positive infinity.
#After your for loop, add a print() call and pass in the following string to see the values of the variables you have created: f'Unvisited: {unvisited}\nDistances: {distances}'.
#All the distances in distances are set to infinite, except for the starting node. 
#The unvisited list contains all the nodes in your graph. But actually, you don't need that for loop to achieve this result.
#Remove your for loop with its entire body. --> aqui eu criei outra função



my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path_old(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

#Your function is going to explore all the nodes connected to the starting node. It will calculate the shortest paths for all of them. 
#Then, it will remove the starting node from the unvisited nodes.
#Next, the closest neighbor node will be visited and the process will be repeated until all the nodes are visited.    
def shortest_path(graph, start, target=''):
    #The list() type constructor enables you to build a list from an iterable.
    #Modify the assignment of your unvisited variable to use list(), and pass graph as the iterable.
    unvisited = list(graph)
    distances = {}    

    #With a dictionary comprehension, you can create a dictionary starting from an existing dictionary:
    #{key: val for key in dict}
    #In the example above, val is the value that key will have in the new dictionary, and dict is the existing dictionary.
    #You want to keep track of the paths between the starting node and each other node.
    #After the distances variable, create a paths variable and assign it a dictionary with all the keys from graph. 
    #Assign an empty list to each key and use a dictionary comprehension to build your dictionary.
    
    paths = {node: [] for node in graph}

    #Dictionary comprehensions support conditional if/else syntax too:
    #{key: val_1 if condition else val_2 for key in dict}
    #In the example above, dict is the existing dictionary. 
    #When condition evaluates to True, key will have the value val_1 , otherwise val_2.
    #Use a dictionary comprehension to create a dictionary based on graph and assign it to the distances variable. 
    #Give the key a value of zero if the node is equal to the starting node, and infinite otherwise. Use float('inf') to achieve the latter.
    distances = {node: 0 if node == start else float('inf') for node in graph}

    #Since the algorithm begins its assessment from the starting node, after creating the paths dictionary, you need to add the starting node to its own list in the paths dictionary.
    #Use the .append() method to append start to the paths[start] list.
    paths[start].append(start)

    #min() takes also a keyword-only argument. 
    #Passing a function as an additional argument to min(), you can modify the way the list items are compared.
    #The result of the line you've just written in the previous step is the node that comes first in alphabetical order. 
    #Instead you want to select the unvisited node having the smallest distance from the starting node.
    #Pass key=distances.get as the second argument to your min() call. 
    #In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.    

    print(f'\nGraph: {graph}\nUnvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}\n')

    #Inside the while loop, the first thing to do is define the current node to visit. 
    #For that you can use the min() function. It returns the smallest item from the iterable passed as the argument.
    #Remove pass, then create a variable called current and assign it min(unvisited).
    #min() takes also a keyword-only argument. Passing a function as an additional argument to min(), you can modify the way the list items are compared.
    #The result of the line you've just written in the previous step is the node that comes first in alphabetical order. 
    #Instead you want to select the unvisited node having the smallest distance from the starting node.
    #Pass key=distances.get as the second argument to your min() call. 
    #In this way, the comparison will take place depending on the value each unvisited list item has inside the distances dictionary.

    while unvisited:
        current = min(unvisited, key=distances.get)
        print('current', current)
        print(f'graph no node current[{current}]', graph[current])

        for node, distance in graph[current]:
            print('node', node)
            print('distance', distance)
            print(f'distances no node [{node}]', distances[node])
            print(f'distances em current[{current}]', distances[current])

            #Create an if statement to check if the distance of the neighbor node (the second item in the processed tuple) plus the distance of current is less than the currently known distance of the neighbor node (the first item in the processed tuple).
            #Once the distance to a node is set inside the distances dictionary, you need to keep track of the path to that node, too. 
            #If the distance for the node in the processed tuple has been updated, the last item in its path is the node itself.
            #Inside your conditional, nest another if statement that triggers when the last element of paths[node] is equal to node.

            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                print(f'nova distances no node [{node}]', distances[node])
                print('\npaths', paths)
                print(f'paths no node [{node}]', paths[node])
                print(f'paths de current[{current}]', paths[current])
                if paths[node] and paths[node][-1] == node:
                    print(f'paths no node [{node}][-1]', paths[node][-1])
                    #When a shorter distance is found for a neighbor node, paths[current] gets assigned to the neighbor node path, paths[node].
                    #This means both variables point to the same list. Since lists are mutable, when you append the neighbor node to its path, both paths[node] and paths[current] are modified because they are the same list. 
                    #This results in wrong paths, although the distances are correct.
                    #You can fix that bug by assigning a copy of paths[current] to the neighbor node path.                    
                    paths[node] = paths[current][:]
                else:
                    #The .extend() method, allows you to add elements from an iterable to the end of a list:
                    #Example Code
                    #my_list = ['larch', 'birch']
                    #tree_list = ['fir', 'redwood', 'pine']
                    #my_list.extend(tree_list)
                    #print(my_list) # Output: ['larch', 'birch', 'fir', 'redwood', 'pine']                    
                    paths[node].extend(paths[current])

                print(f'paths novo node [{node}]', paths[node])
                paths[node].append(node)
                print('______\n')

        #The .remove() method removes from a list the first matching element that is passed as the argument:
        unvisited.remove(current)
        print('+++++++++\n')
    print(f'Graph: {graph}\nUnvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}\n')


def shortest_path_new(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    #Python provides a concise way to write if/else conditionals by using the ternary syntax:
    #val_1 if condition else val_2
    #The expression above evaluates to val_1 if condition is true, otherwise to val_2.    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

shortest_path(my_graph, 'A')