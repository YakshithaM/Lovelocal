def count_digit_one(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divisor = i * 10
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
        i *= 10

    return count

# Test cases
n1 = 13
output1 = count_digit_one(n1)
print(output1)

n2 = 0
output2 = count_digit_one(n2)
print(output2)
