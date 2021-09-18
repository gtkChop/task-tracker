import factory
import pytest
import models
import settings
from datetime import datetime


@pytest.fixture(scope="function")
def create_task(session):
    class TaskFactory(factory.alchemy.SQLAlchemyModelFactory):
        """
        A factory class for creating task
        """
        project_name = settings.ProjectNames.odm
        issue_number = factory.faker.Faker('pystr', max_chars=32)
        issue_link = "https://test-123.com"
        summary = factory.faker.Faker('pystr', max_chars=200)
        no_of_hours = factory.faker.Faker('pyfloat', positive=True, min_value=1, max_value=150)
        date = factory.LazyFunction(datetime.now)
        is_active = True

        class Meta:
            model = models.Task
            sqlalchemy_session = session
            sqlalchemy_session_persistence = "flush"

    return TaskFactory
