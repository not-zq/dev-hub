
from pyodbc import connect

class DatabaseConnection:
    '''
    A simple database connection class that provides methods for fetching data and executing queries.
    Attributes:
        connection_string (str): The connection string used to connect to the database. This can be of the folowing formats:
            - Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=Local;Trusted_Connection=yes;
            - DSN=localhost;Database=Local;Trusted_Connection=yes;
    Methods:
        fetch(query: str): Executes a SELECT query and returns the results as a list of tuples.
        execute(query: str, params: tuple | None = None): Executes a non-SELECT query (e.g., INSERT, UPDATE, DELETE) with optional parameters.
        executemany(query: str, data: list): Executes a non-SELECT query with multiple sets of parameters.
    '''
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def fetch(self, query: str):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall() # Returns a list of tuples, where each tuple represents a row in the result set
    
    def execute(self, query: str, params: tuple | None = None):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()

    def executemany(self, query: str, data: list):
        with connect(self.connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.executemany(query, data)
                connection.commit()
