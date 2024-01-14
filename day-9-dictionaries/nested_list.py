example = {"names" : ["Bob", "green", "White"]}

countries = ["France", 'Germany', "Italy"]

example["countries"] = countries

print(example)

# We can have values all collections that we want - list, dict, tuple

# Dict inside dict:

travel_log = {
    "France" : {"visited_cities" : ["France", 'Germany', "Italy"], "total_countries": 1222},
    "Germany" : {"visited_cities" : ["France", 'Germany', "Italy"], "total_countries": 475},
}

# Nesting Dict in a  List:

travel_log = [ # list
    { # dictionary
        "country": "France",
        "visited_cities" : ["France", 'Germany', "Italy"], # list
        "total_countries": 1222
    },
    {
        "country": "Germany",
        "visited_cities" : ["France", 'Germany', "Italy"],
        "total_countries": 475
    }
]

