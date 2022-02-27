########## toy.py ##########

import localsolver

with localsolver.LocalSolver() as ls:
    f = open('input\\file1.txt', 'r')
    weights = [int(i) for i in f.readline().split()]
    values = [int(i) for i in f.readline().split()]
    f.close()
    print(f"input:{weights} and {values}")
    knapsack_bound = 102

    #
    # Declares the optimization model
    #
    model = ls.model

    # 0-1 decisions
    x = [model.bool() for i in range(8)]

    # weight constraint
    knapsack_weight = model.sum(weights[i] * x[i] for i in range(8))
    model.constraint(knapsack_weight <= knapsack_bound)

    # maximize value
    knapsack_value = model.sum(values[i] * x[i] for i in range(8))
    model.maximize(knapsack_value)

    model.close()

    #
    # Parameterizes the solver
    #
    ls.param.time_limit = 10

    ls.solve()