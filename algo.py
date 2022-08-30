# flights  =  "NY -> Iceland -> London -> Berlin, \
#     NY -> Maine -> London, \
#     Berlin -> Paris -> Amsterdam, \
#     Paris -> London -> Egypt"

# start = ny, end = egypt
# visited = {ny,iceland,london}
# result = [ny-iceland-london-egypt, ny-maine-london-egypt]
# queue = [ny-iceland-london-berlin-paris-amsterdam, ny-maine-london-berlin-paris-amsterdam]
# 

#don't want to add london or berlin yet because other nodes may need to visit london/berlin
#maybe after we process the entire queue? we can add nodes to our set?



#algo currently works for single paths but doesn't work if a deeper node has multiple paths to a given node. For instance, our algorithm returns [NY, Iceland, Paris, London, Egypt] if given NY and Egypt as destinations. However it does not capture [NY, Iceland, London, Egypt] or even [NY Iceland Berlin Paris London Egypt]

# if len(node[-1]) > 1: loop through each edge and append a copy to the queue
#     copy_node = node.copy()
#     copy_node.append(neighbor)
#     queue.append(copy_node)

# if not graph[node[-1]] and node != destination: 
#     #don't add to queue
# if node == destination: 
#     #append to result and don't add back to queue

#add duplicates to the queue for the number of edges of a given node

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


flights  =  "NY -> Iceland -> London -> Berlin NY -> Maine -> London Berlin -> Paris -> Amsterdam Paris -> London -> Egypt Maine -> London -> Berlin Maine -> Berlin Iceland -> Berlin"


# pointer = false
#iterate through the string
    #if element is a string:
        #append to string
        #pointer = false

    #if space
        # if currentIndex + 1 == "-" and pointer == false
            #append string to queue
            #string ""
        #     pointer = true
        # if currentIndex + 1 == string and pointer = false
            #append string to queue
            #string = ""
            #process queue until empty
        
        # if element == str[-1]:
        #     append string to queue
        #     process queue until empty
        

def convert_string(string):
    result = {}
    pointer = False
    queue = []
    city = ""

    for index, char in enumerate(string):
        if char.isalpha():
            city += char
            pointer = False

        if char == " ":
            if string[index+1] == "-" and pointer is False:
                queue.append(city)
                city = ""
                pointer = True

            if string[index+1].isalpha() and pointer is False:
                queue.append(city)
                city = ""
                process_queue(queue, result)
        
        if index == len(string)-1: 
            queue.append(city)
            process_queue(queue, result)

    return result

def process_queue(queue, graph):
    origin = None

    while queue:
        city = queue.pop(0)
        if not origin: 
            origin = city
        else:
            if origin not in graph:
                graph[origin] = [city]
            
            if city not in graph[origin]:
                graph[origin].append(city)

            origin = city

    if origin is not None and origin not in graph:
        graph[origin] = []
        origin = None

    return graph

print(convert_string(flights))

def find_paths_bfs(graph, start, destination):
    result = []
    queue = [[start]]

    while queue:
        node = queue.pop(0)
        visited = set(node)

        if node[-1] == destination:
            result.append(node)
            continue
        
        if not graph[node[-1]] and node != destination:
            continue
            
        for neighbor in graph[node[-1]]:
            if neighbor not in visited:
                copy_node = node.copy()
                copy_node.append(neighbor)
                queue.append(copy_node)        

    return result

# print(find_paths_bfs(graph, "NY", "Paris"))






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
        
# print(find_paths(graph, "NY", "Egypt"))