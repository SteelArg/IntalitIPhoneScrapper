import json


class JSONSerializerMeta(type):
    def __new__(cls, name, bases, namespaces):
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, json_data):
            data = json_data
            if not isinstance(json_data, dict):
                data = json.loads(str(json_data))
            return cls(**data)

        namespaces["from_json"] = from_json
        namespaces["to_json"] = to_json

        return super().__new__(cls, name, bases, namespaces)


class JSONSerializer(metaclass=JSONSerializerMeta):
    pass
