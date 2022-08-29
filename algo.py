import collections
from pydoc import pathdirs

# flights  =  "NY -> Iceland -> London -> Berlin, \
#     NY -> Maine -> London, \
#     Berlin -> Paris -> Amsterdam, \
#     Paris -> London -> Egypt"

graph = {
        "NY": ["Iceland", "Maine", "Jordan", "Egypt"],
        "Jordan": [],
        "Maine": ["London"],
        "London": ["Berlin", "Egypt"],
        "Iceland": ["London"],
        'Berlin': ["Paris"],
        "Paris": ["London", "Amsterdam"],
        "Amsterdam": [],
        "Egypt": []
    }


# arr = [ny, maine, london]

# berlin
# iceland
# stack


def test_dfs(graph, start, destination):
    arr = []
    stack = [start]
    visited = set(start)

    while stack:
        node = stack.pop()
        #if a start/destination doesn't have a path
        #if a node has no edges and is not the destination:
        if node != destination and graph[node]:
            arr.append(node)

        if node == destination:
            arr.append(node)
            return arr

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return False
# paths = [[NY, Maine, London]]

def find_paths(graph, start, destination):
    paths = []
    for neighbor in graph[start]:
        if neighbor == destination:
            paths.append([start, neighbor])
            break

        has_path(graph, start, neighbor, destination, paths)
    
    return paths

def has_path(graph, start, neighbor, destination, paths):
    result = [start]
    stack = [neighbor]
    visited = set(start)
    visited.add(neighbor) 

    while stack:
        node = stack.pop()
        if node != destination and graph[node]:
            result.append(node)

        if node == destination:
            result.append(node)
            paths.append(result)
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False
        
print(find_paths(graph, "NY", "Egypt"))
    # return False

    #may need something to notify if a path was found or not


# print(find_paths(graph, "NY", "Maine"))

# def find_paths(graph, start, destination):
#     queue = [[start]]
#     paths = []
#     visited = set()

#     while queue:
#         node = queue.pop(0)
#         # if node[-1] == destination: break
#         for neighbor in graph[node[-1]]:
#             if node[-1] == start:
#                 queue.append([start, neighbor])
#             else:
#                 # if len(graph[node[-1]]) > 1:
#                     # start = NY, Destination = Paris
#                     # in cases where a node has multiple edges, we have to add to the queue like so:
#                     # [NY, Iceland, London, Berlin] and [NY, Iceland, London, Berlin]. Instead we 

#                 if neighbor != destination:
#                     node.append(neighbor)
#                     queue.append(node)
#                 else:
#                     node.append(neighbor)
#                     paths.append(node)
#                     break

#     return paths if len(paths) > 0 else None


# print(find_paths(graph, "NY", "Berlin"))


#node = [NY], queue = []
#node = [NY], queue = [[NY, Iceland], [NY, Maine]] #neighbors of newyork are Iceland and Maine
#node = [NY, Iceland], queue = [[NY, Maine], [NY, Iceland, London]] #neighbor of Iceland is London
#node = [NY, Maine], queue = [NY, Iceland, London], [NY, Maine, London] #neighbor of Maine is London


def find_paths_stack_dfs(graph, start, destination):
    # if graph.get(start) is None or graph.get(destination) is None: return None
    stack = [[start]]
    # visited.add(start)
    paths = []
    while stack:
        node = stack.pop()
        if node[-1] == destination: continue #breaking because we are skipping the destination node

        for neighbor in graph[node[-1]]:
            if node[-1] == start:
                stack.append([start, neighbor])
            else: 
                node.append(neighbor) 
                stack.append(node)

            if neighbor == destination:
                paths.append(stack[-1])
                # stack = stack.pop()
                # stack = []
                break
        
    return paths if len(paths) > 0 else None


# print(find_paths(graph, "NY", "Egypt")) 
#[['NY', 'Maine', 'London'], ['NY', 'Iceland', 'London'], ['NY', 'Paris', 'London']]
#node = [NY], stack = [[NY, Iceland], [NY, Maine]]
#node = [NY, Maine], stack = [[NY, Iceland]]

