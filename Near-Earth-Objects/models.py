import math
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    def __init__(self, designation, name, diameter, hazardous):
        self.designation = designation
        self.name = name
        self.diameter = diameter
        if not self.diameter:
            self.diameter = float("nan")
        self.hazardous = hazardous
        self.approaches = []

    @property
    def fullname(self):
        if self.name:
            return f"{self.designation} ({self.name})"
        return f"{self.designation}"

    def __str__(self):
        if not math.isnan(self.diameter):
            if self.hazardous:
                return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and is potentially hazardous."
            else:
                return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and is not potentially hazardous."
        else:
            if self.hazardous:
                return f"NEO {self.fullname}, is potentially hazardous."
            else:
                return f"NEO {self.fullname}, is not' potentially hazardous."

    def serialize(self):
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    def __init__(self, designation, time, distance, velocity, neo=None):
        self.designation = designation
        self.time = time
        if self.time:
            self.time = cd_to_datetime(self.time)
        self.distance = distance
        self.velocity = velocity
        self.neo = neo

    def __str__(self):
        return f"At {datetime_to_str(self.time)}, '{self.neo.fullname}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of \
                {self.velocity:.2f} km/s."

    def serialize(self):
        return {
            "datetime_utc": datetime_to_str(self.time),
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }
