from mcd.db.database import engine, test_connection
from mcd.db.schema import Base


def main() -> None:
    version = test_connection()
    print("Database connection successful")
    print(version)

import mcd.db.models.property
import mcd.db.models.owner
import mcd.db.models.bmp
import mcd.db.models.contact
import mcd.db.models.inspection
import mcd.db.models.crm
import mcd.db.models.proposal 

Base.metadata.create_all(bind=engine)
print("Database tables created")


if __name__ == "__main__":
    main()
