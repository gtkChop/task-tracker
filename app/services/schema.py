from jsonschema import Draft7Validator, FormatChecker, ValidationError
from dateutil.parser import parse
import errors
import validators
import settings

class TaskSchema:

    task_create_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "project_name": {
                "type": "string",
                "minLength": 1,
                "maxLength": 10
            },
            "issue_number": {
                "type": "string",
            },
            "issue_link": {
                "type": "string",
            },
            "summary": {
                "type": "string",
                "minLength": 1,
                "maxLength": 1000
            },
            "no_of_hours": {
                "type": "number",
                "minimum": 0.1,
                "maximum": 150
            },
            "is_active": {
                "type": "boolean"
            },
            "date": {
                "type": "string",
                "format": "date-time"
            }
        },
        "required": ["project_name", "summary", "no_of_hours", "is_active", "date"]

    }
    json_schema_validator = Draft7Validator(task_create_schema, format_checker=FormatChecker())

    @staticmethod
    def validate_data(data_dict):

        try:
            TaskSchema.json_schema_validator.validate(data_dict)
        except ValidationError as e:
            raise errors.ValidationError(e)

        # link validator
        if data_dict.get('issue_link', None) and not validators.url(data_dict.get('issue_link')):
            raise errors.ValidationError("Not a valid issue_link")

        # Project validator
        if data_dict.get('project_name', '') not in [prj.value for prj in list(settings.ProjectNames)]:
            raise errors.ValidationError('Not a valid project name')

        # date parser check
        try:
            parse(data_dict.get('date', 'na'))
        except Exception as e:
            raise errors.ValidationError('Not a valid date')

        return True

    @staticmethod
    def validate(func):

        def wrap(*args, **kwargs):
            data_dict = args[0]
            TaskSchema.validate(data_dict)
            return func(*args, **kwargs)

        return wrap