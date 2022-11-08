from rich import print as p
import mysql.connector
class DatabaseConnection:
    def __init__(self,url,user,pwd):
        try:
            self.myconn = mysql.connector.connect(host=url,user=user,passwd=pwd)
            self.cursor = self.myconn.cursor()
            p('[green]Database Connected[/green]')
        except Exception as exc:
            p(f"[red]{exc}[/red]")
    def getCursor(self):
        return self.cursor
    def createDatabase(self,dbname: str):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS "+dbname)
            self.cursor.execute("USE pm")
            p('[green]Database created![/green]')
        except Exception as exc:
            p(f'[red]{exc}[/red]')
    def createTable(self,tablename: str):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(password TEXT NOT NULL UNIQUE,app TEXT NOT NULL,url TEXT NOT NULL,sudopd TEXT NOT NULL)")
            p(f'[green][*]Table created!')
        except Exception as exc:
            p(f'[red]{exc}[/red]')