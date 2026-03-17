from datetime import datetime
from rich import print

from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(f"[bold green]Текущая дата:[/bold green] {datetime.now().date()}")
    get_employees()
    calculate_salary()