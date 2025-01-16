def WaterJug(jugA, jugB, goal): 
	stack = []
	visited = set()
	# Initial state (0, 0)
	stack.append((0, 0))
	while stack:
		current_state = stack.pop() 
		x, y = current_state
		print(f"Current state: ({x}, {y})")
		if (x == goal and y == 0) or (y == goal and x == 0): 
			print(f"Last state: ({x}, {y})")
			return True
		if current_state in visited:
			continue
		visited.add(current_state)
		states = set() 
		states.add((jugA, y)) 
		states.add((x, jugB))
		states.add((0, y)) 
		states.add((x, 0))
		pour_AtoB = min(x, jugB - y)
		states.add((x - pour_AtoB, y + pour_AtoB)) 
		pour_BtoA = min(y, jugA - x)
		states.add((x + pour_BtoA, y - pour_BtoA))
		for state in states:
			if state not in visited: 
				stack.append(state)
	return False

jugA = int(input("Enter the capacity of jug A: "))
jugB = int(input("Enter the capacity of jug B: "))
goal = int(input("Enter the goal amount: "))

if WaterJug(jugA, jugB, goal): 
	print("Solution found!")
else:
	print("Solution not found.")