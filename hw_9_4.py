fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"];
# a
reversed_fruits = list(map(lambda fruit: fruit[::-1], fruits));
print("Reversed fruits:", reversed_fruits);
# b
first_letters = list(map(lambda fruit: fruit[0], fruits));
print("First letters of each fruit:", first_letters);
# c.
uppercase_fruits = list(map(lambda fruit: fruit.upper(), fruits));
print("Uppercase fruits:", uppercase_fruits);
# d
length_of_fruits = list(map(lambda fruit: len(fruit), fruits));
print("Length of each fruit's name:", length_of_fruits);
# e
modified_fruits = list(map(lambda fruit: fruit + '!' if fruit.endswith('s') else fruit, fruits));
print("Modified fruits with exclamation for 's' ending:", modified_fruits);
# f
calories_data = {
    "Apple": 52, "Banana": 89, "Orange": 47, "Mango": 60,
    "Strawberry": 32, "Pineapple": 50, "Grapes": 69, "Watermelon": 30
};
fruits_with_calories = list(map(lambda fruit: [fruit, calories_data[fruit]], fruits));
print("Fruits with calories:", fruits_with_calories);
