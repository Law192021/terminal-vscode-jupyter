numbers = list(range(1000))
squares = [n * n for n in numbers]
print(squares[:10])
numbers = list(range(1000))
get_ipython().run_line_magic('timeit', '[n * n for n in numbers]')

def square_loop(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result

get_ipython().run_line_magic('timeit', 'square_loop(numbers)')
