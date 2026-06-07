
from yaml import safe_load
def read_yaml(file_path: str) -> dict:
    with open(file_path, "r", encoding = "utf-8") as file: 
        return safe_load(file)

def read_sql(file_path: str) -> str:
    with open(file_path, "r", encoding = "utf-8") as file: 
        return file.read()
