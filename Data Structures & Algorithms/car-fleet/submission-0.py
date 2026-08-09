class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)

        slowest_fleet_cars = 0
        fleets = 0

        for pos,speed in cars:
            time_to_destination = (target - pos) / speed

            if time_to_destination > slowest_fleet_cars:
                fleets += 1
                slowest_fleet_cars = time_to_destination
        
        return fleets
        