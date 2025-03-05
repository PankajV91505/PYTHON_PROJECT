import sqlite3
from rich import print
from rich.console import Console
from rich.table import Table

# Initialize console
console = Console()

# Database setup
DB_NAME = "expenses.db"

def setup_db():
    """Creates the database table if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                date TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def add_expense(category, amount, description=""):
    """Adds a new expense entry to the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
                       (category, amount, description))
        conn.commit()
        console.print(f"[green] Expense added: {category} - ₹{amount}[/green]")

def view_expenses():
    """Displays all recorded expenses in a table."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, category, amount, description, date FROM expenses ORDER BY date DESC")
        rows = cursor.fetchall()

    if not rows:
        console.print("[yellow]No expenses recorded yet.[/yellow]")
        return

    table = Table(title=" Expense Tracker", show_lines=True)
    table.add_column("ID", justify="center")
    table.add_column("Category", style="cyan")
    table.add_column("Amount (₹)", justify="right", style="bold green")
    table.add_column("Description", style="yellow")
    table.add_column("Date", justify="right")

    for row in rows:
        table.add_row(*map(str, row))

    console.print(table)

def delete_expense(expense_id):
    """Deletes an expense entry by its ID."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        if cursor.rowcount:
            console.print(f"[red] Deleted expense ID {expense_id}[/red]")
            conn.commit()
        else:
            console.print("[yellow] No such expense found.[/yellow]")

def analyze_expenses():
    """Displays total expenses by category."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC")
        rows = cursor.fetchall()

    if not rows:
        console.print("[yellow]No expenses to analyze.[/yellow]")
        return

    table = Table(title=" Expense Analysis")
    table.add_column("Category", style="cyan")
    table.add_column("Total Spent (₹)", justify="right", style="bold green")

    for row in rows:
        table.add_row(row[0], f"₹{row[1]:.2f}")

    console.print(table)

def main():
    """Main interactive menu."""
    setup_db()
    while True:
        console.print("\n[bold cyan]Expense Tracker Menu[/bold cyan]")
        console.print("1️ Add Expense")
        console.print("2️ View Expenses")
        console.print("3️ Delete Expense")
        console.print("4️ Analyze Expenses")
        console.print("5️ Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            category = input("Enter category: ").strip()
            amount = input("Enter amount (₹): ").strip()
            description = input("Enter description (optional): ").strip()
            if amount.replace('.', '', 1).isdigit():
                add_expense(category, float(amount), description)
            else:
                console.print("[red]Invalid amount. Please enter a number.[/red]")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_id = input("Enter expense ID to delete: ").strip()
            if expense_id.isdigit():
                delete_expense(int(expense_id))
            else:
                console.print("[red]Invalid ID. Must be a number.[/red]")

        elif choice == "4":
            analyze_expenses()

        elif choice == "5":
            console.print("[blue] Exiting Expense Tracker. Goodbye![/blue]")
            break

        else:
            console.print("[red] Invalid choice. Try again.[/red]")

if __name__ == "__main__":
    main()
