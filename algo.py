import collections
from pydoc import pathdirs

# flights  =  "NY -> Iceland -> London -> Berlin, \
#     NY -> Maine -> London, \
#     Berlin -> Paris -> Amsterdam, \
#     Paris -> London -> Egypt"

graph = {
        "NY": ["Iceland", "Maine"],
        "Maine": ["London"],
        "London": ["Berlin", "Egypt"],
        "Iceland": ["London"],
        'Berlin': ["Paris"],
        "Paris": ["London", "Amsterdam"],
        "Amsterdam": [],
        "Egypt": []
    }

def find_paths(graph, start, destination):
    queue = [[start]]
    paths = []
    visited = set()

    while queue:
        node = queue.pop(0)
        # if node[-1] == destination: break
        for neighbor in graph[node[-1]]:
            if node[-1] == start:
                queue.append([start, neighbor])
            else:
                # if len(graph[node[-1]]) > 1:
                    # start = NY, Destination = Paris
                    # in cases where a node has multiple edges, we have to add to the queue like so:
                    # [NY, Iceland, London, Berlin] and [NY, Iceland, London, Berlin]. Instead we 

                if neighbor != destination:
                    node.append(neighbor)
                    queue.append(node)
                else:
                    node.append(neighbor)
                    paths.append(node)
                    break

    return paths if len(paths) > 0 else None


print(find_paths(graph, "NY", "Berlin"))


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

