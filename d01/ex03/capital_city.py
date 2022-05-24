import sys

def get_city(item):
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return capital_cities.get(item)

def get_states(item):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return states.get(item)

def main():
    if len(sys.argv) != 2:
        return
    state = get_states(sys.argv[1])
    if state == None:
        print("Uncnown state")
        return
    city = get_city(state)
    print(city)

if __name__ == "__main__":
    main()