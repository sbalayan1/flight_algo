import collections

# flights  =  "NY -> Iceland -> London -> Berlin, \
#     NY -> Maine -> London, \
#     Berlin -> Paris -> Amsterdam, \
#     Paris -> London -> Egypt"

graph = {"NY": set(["Iceland", "Maine"]),
        "Maine": set(["London"]),
        "London": set(['Berlin', "Egypt"]),
        "Iceland": set(["London"]),
        'Berlin': set(["Paris"]),
        "Paris": set(["London", "Amsterdam"]),
        "Amsterdam": set([]),
        "Egypt": set([])}

def find_paths(graph, start, destination):
    if graph.get(start) is None or graph.get(destination) is None: return None
    visited, queue = set(), collections.deque([start])
    visited.add(start)

    paths = []

    while queue:
        vertex = queue.popleft()
    
        for neighbor in graph[vertex]: 
            if neighbor == destination:
                if start == vertex:
                    paths.append([start, neighbor])
                else:
                    paths.append([start, vertex, neighbor])


            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return paths if len(paths) > 0 else -1


print(find_paths(graph, "NY", "London")) 
#[['NY', 'Maine', 'London'], ['NY', 'Iceland', 'London'], ['NY', 'Paris', 'London']]

print(find_paths(graph, "NY", "Berlin")) # [['NY', 'London', 'Berlin']]
print(find_paths(graph, "Amsterdam", "London")) # -1
print(find_paths(graph, "NY", "Egypt")) # [['NY', 'London', 'Berlin']]
print(find_paths(graph, "California", "Oregon")) # None
print(find_paths(graph, "Paris", "Amsterdam")) # [['Paris', 'Amsterdam']]
print(find_paths(graph, "Berlin", "Amsterdam")) # [['Berlin', 'Paris', 'Amsterdam']]