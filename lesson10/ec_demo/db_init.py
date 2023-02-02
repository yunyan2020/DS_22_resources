from db import DB

db = DB("people.db")

create_person_table_query = """
CREATE TABLE IF NOT EXISTS people(
  id INTEGEr PRIMARY KEY,
  name Text,
  title Text,
  tel Text,
  mail Text
)
"""

db.call_db(create_person_table_query)