import csv
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Ride:
    error: str
    taxi_id: int
    pick_up_time: datetime
    drop_of_time: datetime
    passenger_count: int
    trip_distance: float
    tolls_amount: float


def parse_file(csv_file: str):
    with open(csv_file) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        rides = []
        for row in csv_reader:
            ride = Ride(
                error="",
                taxi_id=row['TaxiID'],
                pick_up_time=datetime.strptime(row['lpep_pickup_datetime'], '%Y-%m-%d %H:%M:%S'),
                drop_of_time=datetime.strptime(row['lpep_dropoff_datetime'], '%Y-%m-%d %H:%M:%S'),
                passenger_count=int(row["passenger_count"]),
                trip_distance=float(row["trip_distance"]),
                tolls_amount=float(row["total_amount"])
            )
            rides.append(ride)
        return rides


