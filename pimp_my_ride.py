from typing import Optional

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
        for y in range(x + 1, len(trips)):
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


def find_best_price_recur(compatibilities: list,
                          compat_index: int,
                          max_price: int,
                          best_compat: Optional[list]) -> list:
    print()
    print(f"{compat_index + 1}/{len(compatibilities)}")
    if compat_index >= len(compatibilities):
        # L'index est superieur à la taille de la liste on arrête la récursion
        print("Stop recur")
        return best_compat
    else:
        # On prend la compat de la recursion courante
        cur_compat = compatibilities[compat_index]
        print(cur_compat)
        # On calcul son prix
        x_price = get_trip_prices(cur_compat)
        next_index = compat_index + 1
        if x_price > max_price:
            # Si le prix est supérieur au max on change le max_price et la best_compat pour la prochaine récursion
            return find_best_price_recur(compatibilities=compatibilities,
                                         compat_index=next_index,
                                         max_price=x_price,
                                         best_compat=cur_compat)
        else:
            # Si elle n'est pas supérieur on utilise les précédents max_price et best_compat pour la prochaine récursion
            return find_best_price_recur(compatibilities=compatibilities,
                                         compat_index=next_index,
                                         max_price=max_price,
                                         best_compat=best_compat)


def find_best_price_lst(trips: list) -> list:
    # compatibilities = find_compatibilities(trips)
    # On créé un nouveau list de dict de la forme [{"price":<prix de la compat>, "compat":<la compat>}]
    compat_price = [
        {"compat": compat, "price": get_trip_prices(compat)}
        for compat
        in find_compatibilities(trips)
    ]
    # On récupère le dict avec le max("price")
    max_compat_price = max(compat_price, key=lambda x: x["price"])
    # On retourne uniquement l'élément compat du max dict
    return max_compat_price["compat"]


def main():
    trips_well_parsed = parse_trips(trips_to_Parse)
    best_capitalist_combo = find_best_price(trips_well_parsed)
    print("We're gonna make money with: ", best_capitalist_combo)

    compatibilities = find_compatibilities(trips_well_parsed)

    best_capitalist_combo_recur = find_best_price_recur(compatibilities=compatibilities,
                                                        compat_index=0,
                                                        max_price=-1000000,
                                                        best_compat=None)
    print("We're gonna make money with (recur): ", best_capitalist_combo_recur)

    best_capitalist_combo_lst = find_best_price_lst(trips_well_parsed)
    print("We're gonna make money with (lst): ", best_capitalist_combo_lst)

main()