import json
from typing import get_origin, get_args

class JsonSerializable:
    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        result = {}
        for key, typ in self.__class__.__annotations__.items():
            value = getattr(self, key)

            if value is None:
                result[key] = None
                continue

            origin = get_origin(typ)
            args = get_args(typ)

            # Handle List[JsonSerializable] or List[primitive]
            if origin == list and args:
                result[key] = [
                    item.to_dict() if isinstance(item, JsonSerializable) else item
                    for item in value
                ]
            elif isinstance(value, JsonSerializable):
                result[key] = value.to_dict()
            else:
                result[key] = value

        return result

    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)

        for key, typ in cls.__annotations__.items():
            value = data.get(key)

            if value is None:
                setattr(obj, key, None)
                continue

            origin = get_origin(typ)
            args = get_args(typ)

            if origin == list and args:
                item_type = args[0]
                if issubclass(item_type, JsonSerializable):
                    value = [item_type.from_dict(item) for item in value]
                setattr(obj, key, value)
            elif issubclass(typ, JsonSerializable):
                setattr(obj, key, typ.from_dict(value))
            else:
                setattr(obj, key, value)

        return obj
