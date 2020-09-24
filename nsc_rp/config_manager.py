from spray_mode import *

class MetaSingleton( type): 
    _instance = {}
    
    def __call__( cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super( MetaSingleton, cls).__call__( *args, **kwargs)
        return cls._instance[cls]

class ConfigManager(metaclass = MetaSingleton):
    
    def __init__(self):
        self.FILE_NAME_CONFIG = "config.txt"
        self.config_dict = {
            "detect_spray_duration_sec": 2.5,
            "detect_distance_meter": 1.0,
            "auto_cycle_min": 1,
            "auto_spray_duration_sec": 10,
            "spray_mode": SprayMode.MANUAL
        }
        self.read()

    def read(self):
        with open(self.FILE_NAME_CONFIG, mode="r") as file:
            while True:
                sentence = file.readline()
                if sentence:
                    pair = sentence.split(":")
                    if pair[0] in self.config_dict:
                        self.config_dict[pair[0]] = pair[1].replace("\n", "")
                else:
                    break

    def get_value(self, attribute_):
        if attribute_ in self.config_dict:
            return self.config_dict[attribute_]
        else:
            return None

    def set_value(self, attribute_, value_):
        if attribute_ in self.config_dict:
            self.config_dict[attribute_] = value_
        self.write()

    def write(self):
        with open(self.FILE_NAME_CONFIG, 'w') as file:
            for key in self.config_dict :
                file.write(key + ":" + str(self.config_dict[key]) + "\n")            