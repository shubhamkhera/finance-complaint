from dataclasses import dataclass
from datetime import datetime
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

@dataclass #it allows us to declare a class without an init function
class EnvironmentVariable:
    mongo_db_url = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()