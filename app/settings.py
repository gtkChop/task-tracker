import enum

DB_URL="postgresql://app:app@localhost:5432/app"

class ProjectNames(enum.Enum):
    odm = "ODM"
    losd = "LOSD"
    pret = "PRET-A-LLOD"
    iati = "IATI"
    stand_up = "Stand-Up"
