def remove_elements_from_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista


lista = [3, 5, 7, 9, 11, 13]
listb = [7, 11]
print(f"from {lista} remove {listb}:", remove_elements_from_list(lista, listb))
data = [item for item in lista if item not in listb]
print(f"from {lista} remove {listb}:", data)


def sum_of_list(param_list):
    total = 0
    for item in param_list:
        total += item
    return total


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(f"sum of {list1}", sum_of_list(list1))


def get_even_numbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result


begin = 4
end = 15
print(f"begin={begin},end={end},even numbers:", get_even_numbers(begin, end))
data = [item for item in range(begin, end) if item % 2 == 0]
print(f"begin={begin},end={end},even numbers:", data)
# def is_prime(number):
#     if number in (1, 2):
#         return True
#     for idx in range(2, number):
#         if number % idx == 0:
#             return False
#     return True


# def print_primes(begin, end):
#     for number in range(begin, end+1):
#         if is_prime(number):
#             print(f"{number} is prime number")


# begin = 11
# end = 25

# print_primes(begin, end)


# def sum_of_square(n):
#     result = 0
#     for number in range(1, n+1):
#         result += number*number
#     return result


# print("sum of square 3:", sum_of_square(3))
