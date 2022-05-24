import sys

def find_key(d, item):
    for i, j in d.items():
        if j == item:
            return i
    return None

def get_city(item):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return find_key(capital_cities, item)

def get_state(item):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return find_key(states, item)

def main():
    if len(sys.argv) != 2:
        return
    
    city = get_city(sys.argv[1])
    if city == None:
        print("Uncnown capital city")
        return
    state = get_state(city)
    print(state)

if __name__ == "__main__":
    main()