class UndergroundSystem:

    def __init__(self):
        self.d_avg = defaultdict(list)
        self.d_cust = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d_cust[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.d_cust[id]
        duration = t - start_time
        self.d_avg[(start_station, stationName)].append(duration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.d_avg[(startStation, endStation)]) / len(self.d_avg[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)