import sys

def get_cities():
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    return capital_cities

def get_states():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    return states

def get_key(d, v):
    for i, j in d.items():
        if v.lower() == j.lower():
            return i
    return None

def get_val(d, k):
    for i, j in d.items():
        if k.lower() == i.lower():
            return j
    return None

def main():
    if len(sys.argv) != 2:
        return
    elems = sys.argv[1].split(",")
    for i in range(len(elems)):
        item = elems[i].strip()
        state_val = get_val(get_states(), item)
        if state_val == None:
            city_val = get_key(get_cities(), item)
            if city_val == None:
                print(item, "is neither a capital city nor a state")
            else:
                state = get_key(get_states(), city_val)
                print(item, "is the capital of", state)
        else:
            city = get_val(get_cities(), state_val)
            print(city, "is the capital of", item)

if __name__ == "__main__":
    main()