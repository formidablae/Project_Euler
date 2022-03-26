paths = {}
paths[0] = [1]
paths[1] = [1, 2, 1]
paths[2] = [1, 4, 6, 4, 1]


def lattice_paths(n):
    if n in paths.keys():
        return paths[n]
    lower_path = lattice_paths(n - 1)
    for times in range(2):
        new_path = [1]
        for i in range(1, len(lower_path)):
            new_path.append(lower_path[i - 1] + lower_path[i])
        new_path.append(1)
        lower_path = new_path
    return lower_path


print(max(lattice_paths(20)))
