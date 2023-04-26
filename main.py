from abc import ABC, abstractmethod
import json
import csv
import io
import matplotlib.pyplot as plt
import pandas as pd
class CovidDataService:
    def get_countries_data(self, countries):
        pass

    def get_countries_historic_data(self, countries, start_date, end_date):
        pass


class ConvertData(ABC):
    @abstractmethod
    def convert_data(self, json_data):
        pass


class ConvertDataPlotterCSV(ConvertData):
    def convert_data(self, json_data):

        data = json.loads(json_data)

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow(data[0].keys())

        for item in data:
            writer.writerow(item.values())

        csv_contents = output.getvalue().strip()
        return csv_contents

class CSVPlotter:
    def plot_data(self, csv_data):
        df = pd.read_csv(io.StringIO(csv_data))
        df.plot()
        plt.show()


service = CovidDataService()
converter = ConvertDataPlotterCSV()
plotter = CSVPlotter()
service.get_countries_data(['Spain'])
json_data = """[  {    "country": "Spain",    "date": "2022-04-25",    "new_cases": 8408,    "new_deaths": 87,    "total_cases": 3858280,    "total_deaths": 80370  },  {    "country": "France",    "date": "2022-04-25",    "new_cases": 24523,    "new_deaths": 267,    "total_cases": 6794896,    "total_deaths": 105547  },  {    "country": "Germany",    "date": "2022-04-25",    "new_cases": 11974,    "new_deaths": 137,    "total_cases": 3865868,    "total_deaths": 93960  }]"""
csv_data = converter.convert_data(json_data)
plotter.plot_data(csv_data)
