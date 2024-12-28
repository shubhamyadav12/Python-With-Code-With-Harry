from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Favorite Movies")

table.add_column("S.No", justify="right", style="cyan", no_wrap=True)
table.add_column("Movie Name", style="magenta")
table.add_column("Year", justify="right", style="green")

table.add_row("1", "The Shawshank Redemption", "1994")
table.add_row("2", "The Godfather", "1972")
table.add_row("3", "The Dark Knight", "2008")
table.add_row("4", "The Savera hua", "1994")
table.add_row("5", "The Gadar", "1972")
table.add_row("6", "The rain night", "2008")

console.print(table)