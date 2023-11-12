from patterns import csv_utils
from patterns import web_report
from patterns import print_report
from patterns.ReportGenerator import ReportGenerator

CSV_FILE = "taxi-data.csv"



def main(strategy):
    rides = csv_utils.parse_file(CSV_FILE) # Type: List[Ride]

    # Factory Method
    if strategy == "web":
        generator = ReportGenerator(web_report)
        
    else:
        generator = ReportGenerator(print_report)

    report_str = generator.create_content(rides) # Type: str
    generator.create_file(report_str) # -> Generate File


if __name__ == '__main__':
    web_strategy = "web"
    print_strategy = "text"
    main(web_strategy)
