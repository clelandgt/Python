# -*- coding: utf-8 -*-
"""
Problem : Trains
The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.'  That is, a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

The purpose of this problem is to help the railroad provide its customers with information about the routes.  In particular, you will compute the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!  For example, the first problem means to start at city A, then travel directly to city B (a distance of 5), then directly to city C (a distance of 4).
The distance of the route A-B-C.
The distance of the route A-D.
The distance of the route A-D-C.
The distance of the route A-E-B-C-D.
The distance of the route A-E-D.
The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
The length of the shortest route (in terms of distance to travel) from A to C.
The length of the shortest route (in terms of distance to travel) from B to B.
The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.

Test Input:
For the test input, the towns are named using the first few letters of the alphabet from A to D.  A route between two towns (A to B) with a distance of 5 is represented as AB5.
Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
Expected Output:
Output #1: 9
Output #2: 5
Output #3: 13
Output #4: 22
Output #5: NO SUCH ROUTE
Output #6: 2
Output #7: 3
Output #8: 9
Output #9: 9
Output #10: 7
"""
from lib.routes import Routes
from lib.town import Town

OUT_FORMAT = 'Output #%s: %s'
FILE_PATH = 'data/input.txt'


def main():

    a = Town('A')
    b = Town('B')
    c = Town('C')
    d = Town('D')
    e = Town('E')
    routes = Routes(FILE_PATH)

    # 1. The distance of the route A-B-C.
    towns = []
    towns.append(a)
    towns.append(b)
    towns.append(c)
    distance = routes.get_length(towns)
    print OUT_FORMAT %(1, distance)

    # 2. The distance of the route A-D.
    towns = []
    towns.append(a)
    towns.append(d)
    distance= routes.get_length(towns)
    print OUT_FORMAT %(2, distance)

    # 3. The distance of the route A-D-C.
    towns = []
    towns.append(a)
    towns.append(d)
    towns.append(c)
    distance= routes.get_length(towns)
    print OUT_FORMAT %(3, distance)

    # 4. The distance of the route A-E-B-C-D.
    towns = []
    towns.append(a)
    towns.append(e)
    towns.append(b)
    towns.append(c)
    towns.append(d)
    distance= routes.get_length(towns)
    print OUT_FORMAT %(4, distance)

    # 5. The distance of the route A-E-D.
    towns = []
    towns.append(a)
    towns.append(e)
    towns.append(d)
    distance = routes.get_length(towns)
    print OUT_FORMAT % (5, distance)

    # 6. The number of trips starting at C and ending at C with a maximum of 3
    trips_count = routes.trips_count_within_stations_count(c, c, 0, 3)
    print OUT_FORMAT % (6, trips_count)

    # 7. The number of trips starting at A and ending at C with exactly 4 stops.  In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
    trips_count = routes.trips_count_equal_stations_count(a, c, 0, 2)
    print OUT_FORMAT % (7, trips_count)

    # 8. The length of the shortest route (in terms of distance to travel) from A to C.
    short_distance = routes.find_short_trip(a, c)
    print OUT_FORMAT % (8, short_distance)

    # 9. The length of the shortest route (in terms of distance to travel) from B to B.
    short_distance = routes.find_short_trip(b, b)
    print OUT_FORMAT % (9, short_distance)

    # 10. The number of different routes from C to C with a distance of less than 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
    trips_count = routes.trips_count_within_total_distance(c, c, 0, 30)
    print OUT_FORMAT % (10, trips_count)

if __name__ == '__main__':
    main()
