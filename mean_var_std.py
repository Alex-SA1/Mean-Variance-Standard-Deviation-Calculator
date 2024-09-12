import numpy as np


def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list, (3, 3))

    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    calculations['mean'].append(np.mean(matrix, axis=0).tolist())
    calculations['mean'].append(np.mean(matrix, axis=1).tolist())
    calculations['mean'].append(np.mean(np.array(list)).tolist())

    calculations['variance'].append(np.var(matrix, axis=0).tolist())
    calculations['variance'].append(np.var(matrix, axis=1).tolist())
    calculations['variance'].append(np.var(np.array(list)).tolist())

    calculations['standard deviation'].append(np.std(matrix, axis=0).tolist())
    calculations['standard deviation'].append(np.std(matrix, axis=1).tolist())
    calculations['standard deviation'].append(np.std(np.array(list)).tolist())

    calculations['max'].append(np.max(matrix, axis=0).tolist())
    calculations['max'].append(np.max(matrix, axis=1).tolist())
    calculations['max'].append(np.max(np.array(list)).tolist())

    calculations['min'].append(np.min(matrix, axis=0).tolist())
    calculations['min'].append(np.min(matrix, axis=1).tolist())
    calculations['min'].append(np.min(np.array(list)).tolist())

    calculations['sum'].append(np.sum(matrix, axis=0).tolist())
    calculations['sum'].append(np.sum(matrix, axis=1).tolist())
    calculations['sum'].append(np.sum(np.array(list)).tolist())

    return calculations

