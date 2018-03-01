import copy

def switch(solution, i, j):
    inter = solution[i]
    solution2 = copy.deepcopy(solution)
    solution2[i] = solution[j]
    solution2[j] = inter
    return solution2

def hill_climbing(solution, data):
    l = range(len(data['n_vehicles']))
    index_l = [(i, j) for i in l for j in l]

    best_score = model.score(solution)
    best_solution = solution
    for i, j in index_l:
        new_solution = switch(solution, i, j)
        new_score = model.score(new_solution, data)
        if new_score > best_score:
            best_score = new_score
            best_solution = new_solution

    return best_solution

