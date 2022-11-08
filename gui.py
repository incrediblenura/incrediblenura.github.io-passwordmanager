from rich.layout import Layout
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
def GUI():
    layout = Layout()
    layout.split_column(Layout(name="statusbar",size=2),Layout(name="body"))
    layout["body"].split_row(Layout(name="aside"),Layout(name="main", ratio=3))
    table = Table()
    table.add_column(style="green")
    table.add_row("1. Create Password")
    table.add_row("2. Read Password")
    table.add_row("3. Update Password")
    table.add_row("4. Delete Password")
    table.add_row("5. Exit")
    table.add_row("6. Clear Screen")
    panel = Panel(table)
    layout["aside"].split(panel)
    layout["statusbar"].add_split("[blue]Running...[/blue]")
    console = Console()
    console.print(layout)

GUI()