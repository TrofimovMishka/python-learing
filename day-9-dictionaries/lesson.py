country = "Brazil"
visits = 2
list_of_cities = ["Sao Paulo", "Rio de Janeiro"]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# to be added to the travel_log.
def add_new_country(country, visits, list_of_cities):
    dict_to_append = {}

    dict_to_append["country"] = country
    dict_to_append["visits"] = visits
    dict_to_append["cities"] = list_of_cities

    travel_log.append(dict_to_append)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
