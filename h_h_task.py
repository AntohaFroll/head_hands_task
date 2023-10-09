import random


def generate_sorted_arrays():

    n = int(input())
    arrays = []
    sizes = set()
    for i in range(n):
        size = random.randint(1, n)
        while size in sizes:
            size = random.randint(1, n)
        sizes.add(size)
        array = [random.randint(0, 100) for _ in range(size)]
        if i % 2 == 0:
            array.sort()
        else:
            array.sort(reverse=True)
        arrays.append(array)
    return arrays


sorted_arrays = generate_sorted_arrays()
print(sorted_arrays)
