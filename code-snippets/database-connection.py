
from pyodbc import connect
from pandas import DataFrame

class DatabaseConnection:
    '''
    A simple pyodbc wrapper to connect to a single database, providing methods to fetch data and execute queries.
    Attributes:
        connection_string (str): The connection string used to connect to the database. This can be of the folowing formats:
            - Driver={driver};Server={server};Database={database};Trusted_Connection=yes;
            - Driver={driver};Server={server};Database={database};UID={user};PWD={pwd};
            - Driver={driver};Host={host};HTTPPath={http_path};UID=token;PWD={token};
            - DSN={dsn};Database={database};Trusted_Connection=yes;

    Methods:
        query(query: str, params: tuple | None = None): Executes a SELECT query with optional parameters and returns the results as a DataFrame.
        execute(query: str, params: tuple | None = None): Executes a non-SELECT query (e.g., INSERT, UPDATE, DELETE) with optional parameters.
        executemany(query: str, data: list[tuple]): Executes a non-SELECT query with multiple sets of parameters.
    '''
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def query(self, query: str, params: tuple | None = None) -> DataFrame:
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params or ())
                return DataFrame.from_records(cursor.fetchall(), columns = [column[0] for column in cursor.description])
    
    def execute(self, query: str, params: tuple | None = None):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params or ())
            connection.commit()

    def executemany(self, query: str, data: list[tuple]):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(query, data)
                connection.commit()
 

if __name__== "__main__":

    LOCAL_DB = DatabaseConnection(connection_string=(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=Local;"
        "Trusted_Connection=yes;"
    ))

    print(LOCAL_DB.query("SELECT TOP (1) * FROM SpotifyExtendedStreamingHistory"))
