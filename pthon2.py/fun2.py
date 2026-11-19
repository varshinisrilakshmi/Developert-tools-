def set_operations():
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    print("Set A:", A)
    print("Set B:", B)
    print("Union:", A | B)
    print("Intersection:", A & B)
    print("Difference (A - B):", A - B)
    print("Is 3 in A?", 3 in A)
    print("Is 7 in A?", 7 in A)
    A.add(7)
    print("After add(7):", A)
    A.remove(2)
    print("After remove(2):", A)
    A.discard(10)
    print("After discard(10):", A)
set_operations()
