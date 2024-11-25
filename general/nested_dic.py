country = input("Country Please\n") # Add country name
visits = int(input("Visits Please\n")) # Number of visits
list_of_cities = eval(input("List of Cities Please\n")) # create list from formatted string

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
  }
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
new_log = {}
new_log["country"] = country
new_log["visits"] = visits
new_log["cities"] = list_of_cities
travel_log.append(new_log)
#print(new_log)
print(travel_log)