# -*- coding: utf-8 -*-

from stations import Station
from town import Town

TOWNS_NAME_LIST = "ABCDE"
NO_ROUTE = "NO SUCH ROUTE"

class Routes:
    route_table = {}

    def __init__(self, file_path):
        assert self.read_file(file_path)


    def read_file(self, file_path):

        try:
            file = open(file_path)
            line = file.readline()

            # delete the "Graph" and split string by ','
            line = line.replace("Graph: ", " ")
            items = line.split(',')

            # generate route table
            for item in TOWNS_NAME_LIST:
                self.route_table[Town(item)] = None

            # decode items into route_table
            for item in items:
                if item[1] in TOWNS_NAME_LIST:
                    if item[2] in TOWNS_NAME_LIST:
                        # generate stations
                        station = Station(Town(item[1]), Town(item[2]), int(item[3]))

                        # put stations into route_table
                        if self.route_table[Town(item[1])] == None:
                            self.route_table[Town(item[1])] = station
                        else:
                            station_temp = self.route_table[Town(item[1])]
                            while station_temp.next_station:
                                station_temp = station_temp.next_station
                            station_temp.next_station = station
                    else:
                        return False
                else:
                    return False

        except Exception, e:
            print e,
            return False

        return True

    # search and return the distance of a standing only lead to another station
    def get_distance_to_next_station(self, next_town, station):
        if station.destination == next_town:
            return station.distance
        else:
            if station.next_station:
                return self.get_distance_to_next_station(next_town, station.next_station)
            else:
                return False

    # calculate distance of the route.
    def get_length(self, towns):

        distance = 0

        try:
            counter = 0
            for town in towns:
                if counter+1 <= len(towns)-1:
                    next_town = towns[counter+1]

                    stations = self.route_table[town]
                    result = self.get_distance_to_next_station(next_town, stations)

                    if result:
                        distance += result
                    else:
                        return NO_ROUTE
                    counter += 1
                else:
                    pass

        except IndexError, e:
            print e
            return distance

        return distance

    # get count of trips within stations count limit.
    def trips_count_within_stations_count(self, town_start, town_end, stations_counter, stations_max):
        routes = 0

        # Check town_start adn town_end exists in route table
        if town_start in self.route_table and town_end in self.route_table:
            stations_counter += 1

            if stations_counter > stations_max:
                return 0

            # mark this town was visited
            town_start.visited = True

            # retrieve current station
            current_station = self.route_table[town_start]
            while current_station:
                if current_station.destination == town_end:
                    routes += 1
                elif not current_station.destination.visited:
                    routes += self.trips_count_within_stations_count(current_station.destination,
                                                                    town_end, stations_counter, stations_max)
                    stations_counter -= 1

                current_station = current_station.next_station

        else:
            return NO_ROUTEfd

        town_start.visited = False
        return routes

    # get count of trips whose stations_count=station_const.
    def trips_count_equal_stations_count(self, town_start, town_end, stations_counter, stations_const):
        routes = 0

        # Check town_start adn town_end exists in route table
        if town_start in self.route_table and town_end in self.route_table:
            stations_counter += 1

            if stations_counter == stations_const:
                return 0

            # mark this town was visited
            town_start.visited = True

            # retrieve current station
            current_station = self.route_table[town_start]
            while current_station:
                if current_station.destination == town_end:
                    routes += 1
                elif not current_station.destination.visited:
                    routes += self.trips_count_within_stations_count(current_station.destination,
                                                                    town_end, stations_counter, stations_const)
                    stations_counter -= 1

                current_station = current_station.next_station

        else:
            return NO_ROUTE

        town_start.visited = False
        return routes

    # get count of trips within distance limit.
    def trips_count_within_total_distance(self, town_start, town_end, distance, max_distance):
        routes = 0

        if town_start in self.route_table and town_end in self.route_table:
            station = self.route_table[town_start]

            while station:
                distance += station.distance

                if distance <= max_distance:
                    if station.destination == town_end:
                        routes += 1
                        routes += self.trips_count_within_total_distance(station.destination,
                                            town_end, distance, max_distance)
                        station = station.next_station
                        continue
                    else:
                        routes += self.trips_count_within_total_distance(station.destination,
                                            town_end, distance, max_distance)
                        distance -= station.distance

                else:
                    distance -= station.distance
                station = station.next_station
        else:
            return NO_ROUTE
        return routes

    # find shortest trip between two towns
    def find_short_trip(self, town_start, town_end, distance=1, shortest_route=0):
        if town_start in self.route_table and town_end in self.route_table:

            town_start.visited = True
            station = self.route_table[town_start]
            while station:
                distance += station.distance

                if station.destination == town_end:
                    if shortest_route == 0 or distance < shortest_route:
                        shortest_route = distance
                    town_start.visited = False
                    return shortest_route

                elif not station.destination.visited:
                    distance -= station.distance
                    station = station.next_station
                    if station is not None:
                        return self.find_short_trip(station.destination, town_end, distance, shortest_route)
                    else:
                        return shortest_route

        else:
            return NO_ROUTE