travel_log = {"France" : ["Paris", "Lille", "Dijon"],
              "Germany" : ["Stuttgart", "Berlin"],}
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 0
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 0
    },
}

print(travel["Germany"]["cities_visited"][2])