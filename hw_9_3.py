import random
numbers = [random.randint(-50, 50) for _ in range(20)];
print("Original numbers:", numbers);
# a
cubed_numbers = list(map(lambda x: x ** 3, numbers));
print("Cubed numbers:", cubed_numbers);
# b
def change_units_digit_to_2(x):
    if x < 0:
        return int(str(x)[:-1] + '2');
    elif x == 0:
        return 2
    else:
        return int(str(x)[:-1] + '2');
changed_units_digit = list(map(change_units_digit_to_2, numbers));
print("Changed units digit to 2:", changed_units_digit);
# c
fahrenheit_numbers = list(map(lambda x: (x * 9/5) + 32, numbers));
print("Numbers in Fahrenheit:", fahrenheit_numbers);
# d
positive_negative = list(map(lambda x: "positive" if x > 0 else ("negative" if x < 0 else x), numbers));
print("Positive or negative:", positive_negative);
# e
min_num = min(numbers);
max_num = max(numbers);
min_max_numbers = list(map(lambda x: "min" if x == min_num else ("max" if x == max_num else x), numbers));
print("Min and Max replaced:", min_max_numbers);
# f
reversed_digits = list(map(lambda x: int(str(x)[::-1]) if x >= 0 else int('-' + str(x)[:0:-1]), numbers));
print("Reversed digits:", reversed_digits);
# g
absolute_values = list(map(lambda x: abs(x) if x >= 0 else -abs(x), numbers));
print("Absolute values flipped:", absolute_values);
# h
income_expenses = [[10000, 7000], [300, 5000], [2000, 8000]];
balance = list(map(lambda x: x[0] - x[1], income_expenses));
print("Monthly balance:", balance);
