from patterns.csv_utils import Ride


def create_file(content: str):
    with open("financial-report.txt", "w") as file:
        file.write(content)


# LSP - Liskov Substitution Principle
def close_table_headers():
    return "\n"


def create_headers(title: str):
    return "\t \t \t" + title + "\t \t \t\n\n"


def create_table_headers():
    return "\t TaxiID\t Pickup time\t Dropoff time\t Passenger count\t Trip Distance\t Total amount"


def add_ride(ride):
    return "".join([
        "\n",
        "\t" + ride.taxi_id,
        "\t" + ride.pick_up_time.isoformat(),
        "\t" + ride.drop_of_time.isoformat(),
        "\t" + str(ride.passenger_count),
        "\t" + str(ride.trip_distance),
        "\t" + _format_amount(ride.tolls_amount),
    ])


def _format_amount(amount):
    if amount < 0:
        return "(" + str(amount) + ")"
    return str(amount)
