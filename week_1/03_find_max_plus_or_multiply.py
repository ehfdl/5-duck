def find_max_plus_or_multiply(array):
    number = 0
    for x in array:
        if number <= 1:
            number += x
        else:
            if x <= 1:
                number += x
            else:
                number *= x

    return number


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))