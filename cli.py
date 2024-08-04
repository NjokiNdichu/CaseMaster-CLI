import click
from helpers import (
    add_case,
    list_cases,
    find_case_by_id,
    delete_case,
    update_case,
    add_client,
    list_clients,
    find_client_by_id,
    delete_client,
    update_client,
    add_lawyer,
    list_lawyers,
    find_lawyer_by_id,
    delete_lawyer,
    update_lawyer
)

@click.group()
def cli():
    """Case Management System CLI"""
    pass

def menu():
    """Display the main menu and handle user input."""
    while True:
        click.echo("Welcome to the Case Management System")
        click.echo("1. Manage Clients")
        click.echo("2. Manage Lawyers")
        click.echo("3. Manage Cases")
        click.echo("4. Exit")

        choice = click.prompt("Please choose an option (1-4)", type=int)
        if choice == 1:
            manage_clients()
        elif choice == 2:
            manage_lawyers()
        elif choice == 3:
            manage_cases()
        elif choice == 4:
            click.echo("Exiting the system. Goodbye!")
            break  
        else:
            click.echo("Invalid choice. Please choose a valid option.")

def manage_clients():
    """Manage clients menu."""
    while True:
        click.echo("Client Management")
        click.echo("1. Add Client")
        click.echo("2. List Clients")
        click.echo("3. Find Client by ID")
        click.echo("4. Delete Client")
        click.echo("5. Update Client")
        click.echo("6. Back to Main Menu")

        choice = click.prompt("Please choose an option (1-6)", type=int)
        if choice == 1:
            name = click.prompt("Enter client name")
            add_client(name)
        elif choice == 2:
            list_clients()
        elif choice == 3:
            client_id = click.prompt("Enter client ID", type=int)
            find_client_by_id(client_id)
        elif choice == 4:
            client_id = click.prompt("Enter client ID to delete", type=int)
            delete_client(client_id)
        elif choice == 5:
            client_id = click.prompt("Enter client ID to update", type=int)
            name = click.prompt("Enter new name (or leave blank to keep current)", default=None)
            update_client(client_id, name)
        elif choice == 6:
            break  
        else:
            click.echo("Invalid choice. Please choose a valid option.")

def manage_lawyers():
    """Manage lawyers menu."""
    while True:
        click.echo("Lawyer Management")
        click.echo("1. Add Lawyer")
        click.echo("2. List Lawyers")
        click.echo("3. Find Lawyer by ID")
        click.echo("4. Delete Lawyer")
        click.echo("5. Update Lawyer")
        click.echo("6. Back to Main Menu")

        choice = click.prompt("Please choose an option (1-6)", type=int)
        if choice == 1:
            name = click.prompt("Enter lawyer name")
            add_lawyer(name)
        elif choice == 2:
            list_lawyers()
        elif choice == 3:
            lawyer_id = click.prompt("Enter lawyer ID", type=int)
            find_lawyer_by_id(lawyer_id)
        elif choice == 4:
            lawyer_id = click.prompt("Enter lawyer ID to delete", type=int)
            delete_lawyer(lawyer_id)
        elif choice == 5:
            lawyer_id = click.prompt("Enter lawyer ID to update", type=int)
            name = click.prompt("Enter new name (or leave blank to keep current)", default=None)
            update_lawyer(lawyer_id, name)
        elif choice == 6:
            break  
        else:
            click.echo("Invalid choice. Please choose a valid option.")

def manage_cases():
    """Manage cases menu."""
    while True:
        click.echo("Case Management")
        click.echo("1. Add Case")
        click.echo("2. List Cases")
        click.echo("3. Find Case by ID")
        click.echo("4. Delete Case")
        click.echo("5. Update Case")
        click.echo("6. Back to Main Menu")

        choice = click.prompt("Please choose an option (1-6)", type=int)
        if choice == 1:
            title = click.prompt("Enter case title")
            client_id = click.prompt("Enter client ID", type=int)
            lawyer_id = click.prompt("Enter lawyer ID", type=int)
            add_case(title, client_id, lawyer_id)
        elif choice == 2:
            list_cases()
        elif choice == 3:
            case_id = click.prompt("Enter case ID", type=int)
            find_case_by_id(case_id)
        elif choice == 4:
            case_id = click.prompt("Enter case ID to delete", type=int)
            delete_case(case_id)
        elif choice == 5:
            case_id = click.prompt("Enter case ID to update", type=int)
            title = click.prompt("Enter new title (or leave blank to keep current)", default=None)
            client_id = click.prompt("Enter new client ID (or leave blank to keep current)", default=None, type=int)
            lawyer_id = click.prompt("Enter new lawyer ID (or leave blank to keep current)", default=None, type=int)
            update_case(case_id, title, client_id, lawyer_id)
        elif choice == 6:
            break  
        else:
            click.echo("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    menu()
