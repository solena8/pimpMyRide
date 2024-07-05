trip_to_parse = "Perdita 8 10 8"


def parse_trip(trip: str) -> dict:
    prospect = {}
    trip = trip.split()
    prospect["client"] = trip[0]
    prospect["start"] = int(trip[1])
    prospect["duration"] = int(trip[2])
    prospect["price"] = int(trip[3])
    return prospect

# print(parse_trip(trip_to_parse))


trips_to_Parse = [
    "Roger 0 5 10",
    "Pongo 3 7 14",
    "Perdita 8 10 8",
    "Anita 16 3 7",
]


def parse_trips(trips: list) -> list:
    return list(map(parse_trip, trips))

# print(parse_trips(trips_to_Parse))


def get_trip_prices(trips: list) -> int:
    sum_prices = 0
    for trip in trips:
        sum_prices += trip["price"]
    return sum_prices

# print(get_trip_prices(parse_trips(trips_to_Parse)))


def check_compatibility(trip_a: dict, trip_b: dict) -> bool:
    # Return condition
    return trip_a["start"] + trip_a["duration"] <= trip_b["start"] \
            or trip_b["start"] + trip_b["duration"] <= trip_a["start"]
    # if (trip_a["start"] + trip_a["duration"] <= trip_b["start"]
    #         or trip_b["start"] + trip_b["duration"] <= trip_a["start"]):
    #     return True
    # return False
    #     compatibility = True
    # return compatibility

# print(check_compatibility({"client": 'Pongo', "start": 3, "duration": 7, "price": 14},
#                                        {"client": 'Anita', "start": 16, "duration": 3, "price": 7}))


def find_compatibilities(trips: list) -> list:
    compatibility_array = []
    for x in range(len(trips)):
        compatibility_array.append([trips[x]])
        for y in range(x+1, len(trips)):
            if check_compatibility(trips[x], trips[y]):
                compatibility_array.append([trips[x], trips[y]])
    return compatibility_array

# print(find_compatibilities(parse_trips(trips_to_Parse)))


def find_best_price(trips: list) -> list:
    compatibilities = find_compatibilities(trips)
    max_price = 0
    best_combo = []
    # iter list
    for x in range(len(compatibilities)):
        x_price = get_trip_prices(compatibilities[x])
        if x_price > max_price:
            max_price = x_price
            best_combo = compatibilities[x]
    return best_combo


trips_well_parsed = parse_trips(trips_to_Parse)
best_capitalist_combo = find_best_price(trips_well_parsed)

print("We're gonna make money with: ", best_capitalist_combo)
