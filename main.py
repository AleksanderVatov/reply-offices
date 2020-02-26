from map import Map

m = Map(open('1_victoria_lake.txt','r'))
print("Map contains",len(m.customers), "customers.")
path = m.path(m.customers[0].location, m.customers[-1].location)
print("The path between the first and last customer costs:", path.cost())
print("It passes through the following points:",path.nodes)
