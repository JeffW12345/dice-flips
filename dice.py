def calc_num_changes(list_of_changes, diff):
    num_changes = 0
    diff = abs(diff)
    for element in list_of_changes:
        if element >= diff:
            num_changes += 1
            return num_changes
        if element < diff:
            diff -= element
            num_changes += 1
    return -1


def get_changes(first_set, second_set, diff):
    list_of_changes = []
    index = 0
    # Second set has a bigger total
    if diff > 0:
        # Amount that can be deducted
        for num in first_set:
            list_of_changes.append(6 - num)
        # Amount that can be added
        for numb in second_set:
            list_of_changes.append(numb - 1)
        list_of_changes.sort(reverse=True)
        return calc_num_changes(list_of_changes, diff)
    # First set has a bigger total
    else:
        # Amount that can be added
        for num in first_set:
            list_of_changes.append(num - 1)
        # Amount that can be deducted
        for numb in second_set:
            list_of_changes.append(6 - numb)
        list_of_changes.sort(reverse=True)
        return calc_num_changes(list_of_changes, diff)


def solution(A, B):
    first_set = A
    second_set = B
    sum_of_first = sum(first_set)
    sum_of_second = sum(second_set)
    diff = sum_of_second - sum_of_first  # If positive, need to reduce second and/or increase first.
    if diff == 0:
        return 0
    # Need to reduce second set total and increase first
    if diff > 0:
        first_set.sort()
        second_set.sort(reverse=True)
        return get_changes(first_set, second_set, diff)
    # Need to increase second set total
    if diff < 0:
        first_set.sort(reverse=True)
        second_set.sort()
        return get_changes(first_set, second_set, diff)



A = [5, 4, 1, 2, 6, 5]
B = [2]
print(solution(A, B)) # Expected answer 6

A = [5]
B = [1, 1, 6]
print(solution(A, B))  # Expected answer 1

A = [1, 2, 3, 4, 3, 2, 1]
B = [6]
print(solution(A, B))  # Expected answer - 1
