numbers = [10, 40, 20, 50, 30]
print("Initial List:", numbers)

numbers.append(60)
print("After append:", numbers)


numbers.insert(2, 25)
print("After insert:", numbers)


numbers.extend([70, 80])
print("After extend:", numbers)


numbers.remove(40)
print("After remove:", numbers)


numbers.pop(3)
print("After pop:", numbers)

numbers.pop()
print("After pop last:", numbers)


del numbers[0]
print("After del:", numbers)


temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)


numbers[1] = 100
print("After modification:", numbers)


numbers.sort()
print("Sorted (Ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted (Descending):", numbers)

numbers.reverse()
print("Reversed List:", numbers)
