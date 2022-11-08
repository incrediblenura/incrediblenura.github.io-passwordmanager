from rich import print as p
from db import DatabaseConnection
mydb = None
def setup():
    try:
        mydb = DatabaseConnection("localhost","root","")
        mydb.createDatabase("pm")
        mydb.createTable("passwordtable")
    except Exception as e:
        p(f'[red]{e}[/red]')