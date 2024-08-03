cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"];
# a
sorted_by_length = sorted(cities, key=lambda city: len(city));
print("Cities sorted by length:", sorted_by_length);
# b
sorted_by_last_letter = sorted(cities, key=lambda city: city[-1]);
print("Cities sorted by last letter:", sorted_by_last_letter);
# c
sorted_reversed = sorted(cities, key=lambda city: city[::-1]);
print("Cities sorted in reverse order:", sorted_reversed);
# d
cities_with_info = [
    ["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"], ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
];
sorted_by_distance = sorted(cities_with_info, key=lambda city: city[1], reverse=True);
print("Cities sorted by distance (largest to smallest):", sorted_by_distance);
sorted_by_continent = sorted(cities_with_info, key=lambda city: city[2]);
print("Cities sorted by continent:", sorted_by_continent);
sorted_by_continent_then_distance = sorted(cities_with_info, key=lambda city: (city[2], city[1]));
print("Cities sorted by continent then distance:", sorted_by_continent_then_distance);
