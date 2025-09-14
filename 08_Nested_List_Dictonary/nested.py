# let's create a dictornary 

travel = {
    "India": "visited",
    "USA": "not visited"
    }

# if we want to access india value
print(travel["India"])

# Now let's add a list of cities in india and usa and add it
# A nested list in a dictionary

travel = {
    "India": ["Delhi", "Mumbai", "Chennai"],
    "USA": ["New York", "Los Angeles", "San Francisco"]
    }

# if we want to access india cities
print(travel["India"])



# Now Let's add the name of the cities and visited or not visited in a nested dictionary

travel = {
    
    "India": {
        "cities_visited": ["Delhi", "Mumbai", "Chennai"],
        "total_visited": 3,
    },
    
    "USA": {
        "cities_visited": ["New York", "Los Angeles", "San Francisco"],
        "total_visited": 3,
    }
    
    }

# how to access the nested dictionary
print(travel["India"]["cities_visited"])

