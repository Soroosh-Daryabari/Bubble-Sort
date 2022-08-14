def bubble_sort(List):
    n = len(List) - 1
    is_swapped = False
    for i in range(n):
        for j in range(n):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                is_swapped = True
        if not is_swapped:
            break
    return List


myList = [-3, 53, 54, 26, 93, 17, 77,
          31, 44, 55, 8978, 521, 254,
          654, 32, 41, 5, 54, 56, 20
          ]
bubble_sort(myList)
print(myList)
