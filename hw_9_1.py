import random
numbers = [random.randint(1, 100) for _ in range(50)];
# a.
greater_than_50 = list(filter(lambda x: x > 50, numbers));
print("Numbers greater than 50:", greater_than_50);
# b.
divisible_by_7 = list(filter(lambda x: x % 7 == 0, numbers));
print("Numbers divisible by 7:", divisible_by_7);
# c.
double_digit_numbers = list(filter(lambda x: 10 <= x <= 99, numbers));
print("Double digit numbers:", double_digit_numbers);
# d.
same_digits = list(filter(lambda x: 10 <= x < 100 and (x // 10) == (x % 10), numbers));
print("Numbers with same digits:", same_digits);
# e.
sum_digits_9 = list(filter(lambda x: sum(map(int, str(x))) == 9, numbers));
print("Numbers with sum of digits 9:", sum_digits_9);
# f.
average = sum(numbers) / len(numbers);
greater_than_avg = list(filter(lambda x: x > average, numbers));
print("Numbers greater than average:", greater_than_avg);
# g.
max_number = max(numbers);
greater_than_half_max = list(filter(lambda x: x > (max_number / 2), numbers));
print("Numbers greater than half of max number:", greater_than_half_max);
# h.
sorted_numbers = sorted(numbers);
median = (sorted_numbers[24] + sorted_numbers[25]) / 2 if len(numbers) % 2 == 0 else sorted_numbers[len(numbers) // 2];
greater_than_median = list(filter(lambda x: x > median, numbers));
print("Numbers greater than median:", greater_than_median);
# i.
user_numbers = [int(input("Enter a number: ")) for _ in range(5)];
not_in_original = list(filter(lambda x: x not in numbers, user_numbers));
print("User numbers not in original list:", not_in_original);
# j.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = list(filter(lambda x: is_prime(x), numbers));
print("Prime numbers:", prime_numbers);
