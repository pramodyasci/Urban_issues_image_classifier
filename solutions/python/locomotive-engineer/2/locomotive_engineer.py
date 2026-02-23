"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*data):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*data]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    one, tw, thr, *last = each_wagons_id
    out = [thr, *missing_wagons, *last, one, tw]
    return out


def add_missing_stops(route: dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    return {**route, "stops": list(stops.values())}
    
    
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    new_dic = {**route, **more_route_information}
    return new_dic


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    out = [list(row) for row in zip(*wagons_rows)]
    return out
    
