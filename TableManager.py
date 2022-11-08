from db import DatabaseConnection
from rich import print as p
from rich.table import Table
from rich.console import Console
#"""
#Comments
#"""
class TableManager:
    def __init__(self):
        self.con = DatabaseConnection(url="localhost",user="root",pwd="")
        self.curs = self.con.getCursor()
        self.curs.execute("USE pm")
    
    def insertData(self,items):
        try:
            query = '\',\''.join(items)
            # p("INSERT INTO passwordtable VALUES('"+query+"')")
            self.curs.execute("INSERT INTO passwordtable VALUES('"+query+"')")
            self.curs.execute("COMMIT")
            p('[green]'+str(self.curs.rowcount)+' rows inserted[/green]')
        except Exception as e:
            p(f"[red]{e}[/red]")
    
    def selectData(self):
        try:
            self.curs.execute("SELECT * FROM passwordtable")
            table = Table(title="Password Manager")
            table.add_column('Password')
            table.add_column('App')
            table.add_column('Url')
            table.add_column('Real Password')
            result = self.curs.fetchall()
            for x in result:
                # print(list(x))
                table.add_row(x[0],x[1],x[2],x[3])
            console = Console()
            console.print(table)
        except Exception as exep:
            p(f'[red][!]{exep}[/red]')
    
    def deleteData(self,pd):
        try:
            # p(f'[blue]DELETE FROM passwordtable WHERE password = \'{pd}\'[/blue]')
            self.curs.execute("DELETE FROM passwordtable WHERE password = '"+pd+"'")
            p(f'[green]'+str(self.curs.rowcount)+' rows deleteted.[/green]')
        except Exception as exep:
            p(f'[red]{exep}[/red]')