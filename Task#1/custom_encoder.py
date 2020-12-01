import json
from models import StudentRoom


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, StudentRoom):
            return {
                obj.room.__class__.__name__: obj.room.__dict__,
                "Students": obj.students,
            }
        return {obj.__class__.__name__: obj.__dict__}