"""
Initialization of repo
@description:
@authors: Aracelli Melissa Boza Zabarburú A01662934, Adolfo Hernández Fernández A01664412, Luis Enrique Salazar Pérez A00833460
@date: 31 / 10 / 2024
"""

def read_matrix(file_name):
    # Step 1: Parse the adjacency matrix from a file
    with open(file_name, "r") as file:
        data = file.read().strip()

    # Replace line breaks and split by semicolon to get rows
    rows = data.split(";")

    print(rows)
    adj_matrix = [
        [int(value) for value in row.split(",") if value.strip()] 
        for row in rows if row.strip()
    ]

    print(adj_matrix)
    return adj_matrix


def get_edges(adj_matrix):
    print("generating the edges")

    # Step 2: Convert adjacency matrix to edge list
    #format of edges is (weight, node 1, node 2)
    edges = []
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adj_matrix[i][j] != 0:
                edges.append((adj_matrix[i][j], i, j))

    edges.sort()
    return edges #return the edges sorted


matrix = read_matrix("example-adjacency-matrix.txt")

edges = get_edges(matrix)
print("edges:", edges)