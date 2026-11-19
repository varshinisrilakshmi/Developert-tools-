def list_operations():
    # Create a list
    numbers = [30, 10, 40, 20]

    print("Original list:", numbers)

    # Traversing the list
    print("Traversing the list:")
    for item in numbers:
        print(item, end=" ")
    print()

    # Insert an element
    numbers.insert(1, 15)
    print("After insert(1, 15):", numbers)

    # Append an element
    numbers.append(50)
    print("After append(50):", numbers)

    # Remove an element
    numbers.remove(40)
    print("After remove(40):", numbers)

    # Sort the list
    numbers.sort()
    print("After sort():", numbers)

    # Reverse the list
    numbers.reverse()
    print("After reverse():", numbers)


list_operations()
