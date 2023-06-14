import pandas as pd
import numpy as np
import json
import pickle
import warnings
warnings.filterwarnings("ignore")
import config

class Flight_Fare():

    def __init__(self,airline,source_city,departure_time,stops,arrival_time,destination_city,
                 class_,duration,days_left):

        self.airline          = airline
        self.source_city      = source_city
        self.departure_time   = departure_time
        self.stops            = stops
        self.arrival_time     = arrival_time
        self.destination_city = destination_city
        self.class_           = class_
        self.duration         = duration
        self.days_left        = days_left

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.load_model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.load_json = json.load(f)

    def get_predicted_price(self):

        self.load_model()

        test_array = np.zeros(len(self.load_json["columns"]))


        test_array[0] = self.load_json["airline"][self.airline]
        test_array[1] = self.load_json["source_city"][self.source_city]
        test_array[2] = self.load_json["departure_time"][self.departure_time]
        test_array[3] = self.load_json["stops"][self.stops]
        test_array[4] = self.load_json["arrival_time"][self.arrival_time]
        test_array[5] = self.load_json["destination_city"][self.destination_city]
        test_array[6] = self.load_json["class_"][self.class_]
        test_array[7] = self.duration
        test_array[8] = self.days_left

        price = round(self.load_model.predict([test_array])[0])

        return price