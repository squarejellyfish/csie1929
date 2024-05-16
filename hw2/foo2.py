projects = ["A", "C", "B"]
capitals = [1, 3, 2]

output = [c for p, c, in sorted(zip(projects, capitals))]
print(output)
