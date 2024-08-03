games = [
    "Fortnite", "Grand Theft Auto V", "The Elder Scrolls V: Skyrim",
    "Dark Souls", "Overwatch"
]
# a
long_names = list(filter(lambda game: len(game) > 8, games));
print("Games with names longer than 8 letters:", long_names);
# b
starts_with_F = list(filter(lambda game: game.startswith('F'), games));
print("Games that start with F:", starts_with_F);
# c
two_word_names = list(filter(lambda game: len(game.split()) == 2, games));
print("Games with exactly 2 words in their names:", two_word_names);
# d
contains_V = list(filter(lambda game: 'V' in game, games));
print("Games that contain the letter V:", contains_V);
# e
special_characters = list(filter(lambda game: any(char in game for char in ":!^&*"), games));
print("Games with special characters:", special_characters);
# f
games_with_years = [
    ["Fortnite", 2017], ["Grand Theft Auto V", 2013],
    ["The Elder Scrolls V: Skyrim", 2011], ["Dark Souls", 2011],
    ["Overwatch", 2016]
]
released_after_2014 = list(filter(lambda game: game[1] > 2014, games_with_years));
print("Games released after 2014:", released_after_2014);
