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

    neighbors = {}
    paths = {}

    while queue:
        vertex = queue.popleft()


        for neighbor in graph[vertex]:
            # if neighbor == destination:
            #     if start == vertex:
            #         paths.append([start, neighbor])
            #     else:
            #         paths.append([start, vertex, neighbor])
            
            #check if the vertex is a neighbor to the start. if it is, create a path
            if vertex in graph[start]:
                paths[vertex] = [start, vertex]
                neighbors[vertex] = set()
                neighbors[vertex].add(neighbor)
                

            #if the vertex is a neighbor to a neighbor, add to that neighbor's path
      
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print(neighbors)
    return paths if len(paths) > 0 else None


print(find_paths(graph, "NY", "London")) 
#[['NY', 'Maine', 'London'], ['NY', 'Iceland', 'London'], ['NY', 'Paris', 'London']]

