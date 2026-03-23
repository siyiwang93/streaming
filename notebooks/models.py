import dataclasses
import json 

@dataclasses.dataclass
class Ride:
    PULocationID: int
    DOLocationID: int
    trip_distance: float
    total_amount: float
    tpep_pickup_datetime: int


def ride_serializer(data):
    data_dict = dataclasses.asdict(data)
    json_str = json.dumps(data_dict)
    return json_str.encode('utf-8')


def ride_deserializer(data):
    json_str = data.decode('utf-8')
    data_dict = json.loads(json_str)
    return Ride(**data_dict)