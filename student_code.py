from expand import expand
from collections import deque
from queue import PriorityQueue

def heuristic(node, end, dis_map):
    # Implement the heuristic function (e.g., straight-line distance, number of hops)
    return dis_map[node][end] # Example: number of hops

def a_star_search (dis_map, time_map, start, end):
	fringe = PriorityQueue()
	visited = set()  # Set to keep track of visited nodes
    
	pathcost= {}
	heurcost={}
    
	pathcost[start]=0
	heurcost = {start: heuristic(start, end, dis_map)}
    
	# Start with the start node
	fringe.put((heurcost[start], [start]))
    
	while fringe:
        # Get the path with the lowest f(n)
		current_f, path = fringe.get()
		current_node = path[-1]
          
		# Check if the goal is reached
		if current_node == end:
			return path
          
		if current_node not in visited:
			visited.add(current_node)
          
			for next_node in expand(current_node, time_map):
				# Calculate new g, h, and f
				new_g = pathcost[current_node] + time_map[current_node][next_node]
				new_h = heuristic(next_node, end, dis_map)
				new_f = new_g + new_h
				
				if next_node not in pathcost or new_g < pathcost[next_node]:
					# Update g and f for the node
					pathcost[next_node] = new_g
					heurcost[next_node] = new_f
					
					# Add the path to this node to the fringe
					new_path = path + [next_node]
					fringe.put((heurcost[next_node], new_path))
	return None
                    
    
    

    

    



def depth_first_search(time_map, start, end):
    fringe = deque()
    visited = set()
    fringe.append([start])

    while fringe:
        path = fringe.pop()
        current_node = path[-1]

        if current_node == end:
            return path

        if current_node not in visited:
            visited.add(current_node)

            connected_nodes = expand(current_node, time_map)
            for next_node in connected_nodes:
                if next_node not in visited:
                    new_path = path + [next_node]
                    fringe.append(new_path)
                    
        

    
    return None
			


def breadth_first_search(time_map, start, end):
    fringe = deque()
    visited = set()
    fringe.append([start])

    while fringe:
        path = fringe.popleft()
        current_node = path[-1]

        if current_node == end:
            return path

        if current_node not in visited:
            visited.add(current_node)

            connected_nodes = expand(current_node, time_map)
            for next_node in connected_nodes:
                if next_node not in visited:
                    new_path = path + [next_node]
                    fringe.append(new_path)
                    
        

    
    return None
			


		
		
		




	

