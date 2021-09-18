from core import create_app
import os
import logging.config

logger_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger.ini')
logging.config.fileConfig(logger_config_file)
app, db, migrate = create_app()


if __name__ == "__main__":
    app.run(debug=True)
