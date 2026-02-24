"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    ls = []
    for index in args:
        ls.append(index)
    return ls


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    f1,f2,f3, *ls = each_wagons_id
    ls.append(f1)
    ls.append(f2)
    missing_wagons = missing_wagons + ls
    missing_wagons.insert(0,f3)
    

    
    return missing_wagons
    


def add_missing_stops(*args,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    

    ls = []
    if len(args) > 1:
        for i in args[1].values():
            ls.append(i)
        args[0]['stops'] = ls
    
        return args[0]
    else:
        for i in kwargs.values():
            ls.append(i)
        args[0]['stops'] = ls
        return args[0]
        
    
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combind = {**route, **more_route_information}
    return combind


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    transpose = zip(*wagons_rows)
    ls = []
    for i in transpose:
        ls.append(list(i))
        
    return ls
