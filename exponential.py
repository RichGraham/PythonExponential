import math

def eval_exp(x, n_terms=100):
    terms = []
    for i in range(n_terms):
        terms.append( x**i / math.factorial(i))

    result = 0.0
    for i in range(n_terms):
        result += terms[i]
    return result

if __name__ == '__main__':
    result = eval_exp(1.0)
    print(result)
