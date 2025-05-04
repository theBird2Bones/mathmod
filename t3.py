import networkx as nx

edge_caps = [
    [None, 30, 45, 25, 30, 20, 40],
    [30, None, 55, 25, 35, 40, 25],
    [25, 30, None, 45, 75, 30, 40],
    [15, 10, 25, None, 40, 30, 80],
    [10, 45, 15, 60, None, 60, 75],
    [10, 30, 45, 30, 55, None, 40],
    [15, 25, 45, 30, 40, 50, None]
]

edge_costs = [
    [None, 5, 10, 4, 5, 6, 10],
    [1, None, 7, 10, 15, 5, 5],
    [1, 10, None, 5, 4, 7, 12],
    [2, 6, 4, None, 5, 10, 8],
    [1, 7, 4, 4, None, 9, 2],
    [1, 4, 2, 3, 8, None, 12],
    [1, 10, 5, 6, 8, 16, None]
]

node_caps = [1000, 55, 35, 40, 50, 45, 1000]

nodes_count = 7
graph = nx.DiGraph()

for i in range(nodes_count):
    graph.add_edge(
        f"n{i+1}-in", 
        f"n{i+1}-out", 
        capacity=node_caps[i], 
        weight=0
    )

for i in range(nodes_count):
    for j in range(nodes_count):
        if i != j and edge_costs[i][j] is not None and edge_caps[i][j] > 0:
            graph.add_edge(
                f"n{i+1}-out", 
                f"n{j+1}-in", 
                capacity=edge_caps[i][j], 
                weight=edge_costs[i][j]
            )

s_node = "n1-in"
t_node = "n7-out"

flow_info = nx.max_flow_min_cost(graph, s_node, t_node)
total_cost = nx.cost_of_flow(graph, flow_info)
max_flow = sum(flow_info[s_node][v] for v in graph[s_node])

for u in graph.nodes:
    for v in graph[u]:
        flow = flow_info[u][v]
        if flow > 0:
            print(f"{u} => {v}: {flow}")
print()
print(f"max поток: {max_flow}")
print(f"min стоимость: {total_cost}")