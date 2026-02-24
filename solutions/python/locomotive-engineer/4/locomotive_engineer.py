"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    new_list = []
    for index in args:
        new_list.append(index)
    return new_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    go_to_last_one,go_to_last_two,go_to_first, *other_list = each_wagons_id
    other_list.append(go_to_last_one)
    other_list.append(go_to_last_two)
    missing_wagons = missing_wagons + other_list
    missing_wagons.insert(0,go_to_first)
    

    
    return missing_wagons
    


def add_missing_stops(*args,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    

    value_to_list = []
    if len(args) > 1:
        for idx in args[1].values():
            value_to_list.append(idx)
        args[0]['stops'] = value_to_list
    
        return args[0]
    if len(args) == 1:
        for idx in kwargs.values():
            value_to_list.append(idx)
        args[0]['stops'] = value_to_list
        return args[0]
        
    
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    results = {**route, **more_route_information}
    return results


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    transpose = zip(*wagons_rows)
    results = []
    for idx in transpose:
        results.append(list(idx))
        
    return results
