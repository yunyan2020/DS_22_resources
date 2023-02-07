import pyodbc

db_server = "localhost\SQLEXPRESS"
# db_server = "LAPTOP-800N131K\SQLEXPRESS"
db_name = "python_lesson11_todo"
db_driver = "ODBC Driver 17 for SQL Server"

connection_string = f"""
DRIVER={db_driver};
SERVER={db_server};
DATABASE={db_name};
trusted_connection=yes;
"""


class DB:    
    def call_db(self, query, *args):
        data = None
        conn = pyodbc.connect(connection_string)
        cur  = conn.cursor()
        if "SELECT" in query:
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.close()
        else:
            conn.execute(query,args)
        conn.commit()
        conn.close()
        return data
        pass

    def init_db(self):
        init_db_query = """
        DROP TABLE todo;
        CREATE TABLE  todo(
          id INTEGER PRIMARY KEY IDENTITY(1,1) NOT NULL,
          title VARCHAR(255) NOT NULL,
          description VARCHAR(255) NOT NULL
        )
        """
        insert_query = """
        INSERT INTO todo (title,description) VALUES ('Do  this','Dont do  that when doing this')
        """
        conn = pyodbc.connect(connection_string)
        conn.execute(init_db_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        # self.call_db(init_db_query)
        # self.call_db(insert_query)

if __name__ == "__main__":
  db = DB()
  db.init_db()

