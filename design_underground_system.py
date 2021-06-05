"""
An underground railway system is keeping track of customer travel times between different stations.
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened
directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from
endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then
checks out at time t2, then t1 < t2. All events happen in chronological order.



Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","
checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],
["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],
["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" ->
                                                              "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo",
                                                              (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" ->
                                                              "Waterloo", (10 + 12 + 14) / 3 = 12
"""
from collections import defaultdict


# Time: O(1)
# Space: O(N^2) + O(C) - N is the number of stations and C is the number of customers in the system
class UndergroundSystem:
    def __init__(self):
        self.customer_info = {}
        self.destination = defaultdict(list)

    def check_in(self, id, station_name, t):
        self.customer_info[id] = [station_name, t]

    def check_out(self, id, station_name, t):
        start_station, start_time = self.customer_info[id]
        key = f"{start_station}:{station_name}"
        value = t - start_time
        if key not in self.destination:
            self.destination[key] = [value, 1]
        else:
            avg, count = self.destination[key]
            self.destination[key] = [(avg * count + value) / (count + 1), count + 1]

    def get_avg_time(self, start_station, end_station):
        return self.destination[f"{start_station}:{end_station}"][0]


if __name__ == "__main__":
    subway = UndergroundSystem()
    subway.check_in(45, "Leyton", 3)
    subway.check_in(32, "Paradise", 8)
    subway.check_in(27, "Leyton", 10)
    subway.check_out(45, "Waterloo", 15)
    subway.check_out(45, "Waterloo", 20)
    subway.check_out(32, "Cambridge", 22)
    subway.get_avg_time("Paradise", "Cambridge")
    subway.get_avg_time("Leyton", "Waterloo")
    subway.check_in(10, "Leyton", 24)
    subway.get_avg_time("Leyton", "Waterloo")
    subway.check_out(10, "Waterloo", 38)
    subway.get_avg_time("Leyton", "Waterloo")
