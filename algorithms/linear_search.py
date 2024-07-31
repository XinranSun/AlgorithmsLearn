def linear_search(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index : {index}")
    else:
        print("Not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
verify(linear_search(numbers, 2))
