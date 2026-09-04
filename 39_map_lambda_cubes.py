numbers = list(map(int, input("Enter numbers: ").split()))

cubes = list(map(lambda x: x * x * x, numbers))

print("Cubes =", cubes)
