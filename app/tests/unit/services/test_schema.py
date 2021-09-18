from services.schema import TaskSchema
import pytest
import errors
from unittest import mock

@mock.patch('services.schema.TaskSchema.json_schema_validator.validate')
def test_task_create_schema_calls(mock_schema_validator, create_task):
    """
    check if validators are called accordingly
    :param mock_schema_validator:
    :param create_task:
    :return:
    """
    task = create_task(issue_link="https://test-123.com")
    data_dict = task.as_dict()
    TaskSchema.validate_data(data_dict)
    mock_schema_validator.assert_called_once_with(data_dict)

def test_task_create_schema_correct_data(create_task):
    """
    Correct data check schema
    :param create_task:
    :return:
    """
    task = create_task(issue_link="https://test-123.com")
    data_dict = task.as_dict()
    TaskSchema.validate_data(data_dict)


def test_task_create_schema_validations(create_task):
    """
    test all validations
    :param create_task:
    :return:
    """

    # Check issue links
    task = create_task(issue_link="")
    data_dict = task.as_dict()
    TaskSchema.validate_data(data_dict)

    task = create_task(issue_link="adasdasd")
    data_dict = task.as_dict()
    with pytest.raises(errors.ValidationError) as e:
        assert TaskSchema.validate_data(data_dict)
        assert 'Not a valid issue_link' in e.message


    # Check not a valid date
    task = create_task(issue_link="https://test-123.com")
    data_dict = task.as_dict()
    data_dict['date'] = ''
    with pytest.raises(errors.ValidationError) as e:
        assert TaskSchema.validate_data(data_dict)

    # Check not a valid project name
    task = create_task(issue_link="https://test-123.com")
    data_dict = task.as_dict()
    assert TaskSchema.validate_data(data_dict)
    data_dict['project_name'] = 'test'
    with pytest.raises(errors.ValidationError) as e:
        assert TaskSchema.validate_data(data_dict)


    # number of hours validation
    task = create_task(issue_link="https://test-123.com")
    data_dict = task.as_dict()
    data_dict['no_of_hours'] = 'ad'
    with pytest.raises(errors.ValidationError) as e:
        assert TaskSchema.validate_data(data_dict)

    data_dict['no_of_hours'] = 1000 # exceeded hours
    with pytest.raises(errors.ValidationError) as e:
        assert TaskSchema.validate_data(data_dict)