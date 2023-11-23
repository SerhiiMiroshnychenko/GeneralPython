def my_sqrt(x):
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__ == "__main__":
    print(my_sqrt(4))
    print(my_sqrt(16))
    print(my_sqrt(18))
