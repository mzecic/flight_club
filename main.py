#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import ast
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

flight_data.get_lowest_price()
updated_flights = flight_data.flights
data_manager.update_csv(updated_flights)

