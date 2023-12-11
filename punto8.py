# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:43:38 2023

@author: Nicolas Marr
"""

import numpy as np
import cvxpy as cp
import graphneitor as gn

ITERACIONES = 6000000
def goemans_williamson_max_cut(adjacency_matrix):
    n = len(adjacency_matrix)

    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0, cp.diag(X) == 1]
    objective = cp.Maximize(0.25 * cp.trace(adjacency_matrix @ X))
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)

    best_cut_size = 0
    bestcut = None

    # Repeat the rounding process multiple times
    for _ in range(ITERACIONES):
        # Generate a random vector
        random_vector = np.random.randn(n, 1)

        # Form a diagonal matrix from the random vector
        diagonal_matrix = np.diag(np.squeeze(random_vector))

        # Calculate the rounded solution
        rounded_solution = np.sign(diagonal_matrix @ X.value @ diagonal_matrix)

        # Calculate the cut size of the rounded solution
        cut_size = np.sum(adjacency_matrix * rounded_solution)

        # Update the best cut if the current one is better
        if cut_size > best_cut_size:
            best_cut_size = cut_size
            best_cut = rounded_solution

    return best_cut, best_cut_size


adjacency_matrix = np.array(gn.cargar())

cut, cut_size = goemans_williamson_max_cut(adjacency_matrix)
print("Best cut:", cut)
print("Best cut size:", cut_size)