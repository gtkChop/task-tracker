import os
import pytest
from core import create_app
import settings

TEST_DB = "/Users/swaroop/Documents/task-tracker/{}".format('test_app.db')
settings.DB_URL = 'sqlite:///' + TEST_DB


@pytest.fixture(scope="session")
def test_client(request):

    app, _, migrate = create_app()
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return test_client


@pytest.fixture(scope='session')
def db(request):

    if os.path.exists(TEST_DB):
        os.unlink(TEST_DB)

    app, database, migrate = create_app()

    def teardown():
        database.drop_all()

    database.create_all()

    request.addfinalizer(teardown)
    return database


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session