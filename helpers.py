from db.models import SessionLocal, Client, Lawyer, Case

def add_client(name):
    """Add a new client."""
    with SessionLocal() as session:
        new_client = Client(name=name)
        session.add(new_client)
        session.commit()
        print(f"Added client: {name}")

def list_clients():
    """List all clients."""
    with SessionLocal() as session:
        clients = session.query(Client).all()
        for client in clients:
            print(f"ID: {client.id}, Name: {client.name}")

def find_client_by_id(client_id):
    """Find a client by ID."""
    with SessionLocal() as session:
        client = session.query(Client).get(client_id)
        if client:
            print(f"ID: {client.id}, Name: {client.name}")
        else:
            print(f"Client with ID {client_id} not found.")

def delete_client(client_id):
    """Delete a client."""
    with SessionLocal() as session:
        client = session.query(Client).get(client_id)
        if client:
            session.delete(client)
            session.commit()
            print(f"Deleted client with ID: {client_id}")
        else:
            print(f"Client with ID {client_id} not found.")

def update_client(client_id, name=None):
    """Update a client."""
    with SessionLocal() as session:
        client = session.query(Client).get(client_id)
        if client:
            if name:
                client.name = name
            session.commit()
            print(f"Updated client: ID: {client.id}, Name: {client.name}")
        else:
            print(f"Client with ID {client_id} not found.")

def add_lawyer(name):
    """Add a new lawyer."""
    with SessionLocal() as session:
        new_lawyer = Lawyer(name=name)
        session.add(new_lawyer)
        session.commit()
        print(f"Added lawyer: {name}")

def list_lawyers():
    """List all lawyers."""
    with SessionLocal() as session:
        lawyers = session.query(Lawyer).all()
        for lawyer in lawyers:
            print(f"ID: {lawyer.id}, Name: {lawyer.name}")

def find_lawyer_by_id(lawyer_id):
    """Find a lawyer by ID."""
    with SessionLocal() as session:
        lawyer = session.query(Lawyer).get(lawyer_id)
        if lawyer:
            print(f"ID: {lawyer.id}, Name: {lawyer.name}")
        else:
            print(f"Lawyer with ID {lawyer_id} not found.")

def delete_lawyer(lawyer_id):
    """Delete a lawyer."""
    with SessionLocal() as session:
        lawyer = session.query(Lawyer).get(lawyer_id)
        if lawyer:
            session.delete(lawyer)
            session.commit()
            print(f"Deleted lawyer with ID: {lawyer_id}")
        else:
            print(f"Lawyer with ID {lawyer_id} not found.")

def update_lawyer(lawyer_id, name=None):
    """Update a lawyer."""
    with SessionLocal() as session:
        lawyer = session.query(Lawyer).get(lawyer_id)
        if lawyer:
            if name:
                lawyer.name = name
            session.commit()
            print(f"Updated lawyer: ID: {lawyer.id}, Name: {lawyer.name}")
        else:
            print(f"Lawyer with ID {lawyer_id} not found.")

def add_case(title, client_id, lawyer_id):
    """Add a new case."""
    with SessionLocal() as session:
        new_case = Case(title=title, client_id=client_id, lawyer_id=lawyer_id)
        session.add(new_case)
        session.commit()
        print(f"Added case: {title}")

def list_cases():
    """List all cases."""
    with SessionLocal() as session:
        cases = session.query(Case).all()
        for case in cases:
            print(f"ID: {case.id}, Title: {case.title}, Client ID: {case.client_id}, Lawyer ID: {case.lawyer_id}")

def find_case_by_id(case_id):
    """Find a case by ID."""
    with SessionLocal() as session:
        case = session.query(Case).get(case_id)
        if case:
            print(f"ID: {case.id}, Title: {case.title}, Description: {case.description}, Client ID: {case.client_id}, Lawyer ID: {case.lawyer_id}")
        else:
            print(f"Case with ID {case_id} not found.")

def delete_case(case_id):
    """Delete a case."""
    with SessionLocal() as session:
        case = session.query(Case).get(case_id)
        if case:
            session.delete(case)
            session.commit()
            print(f"Deleted case with ID: {case_id}")
        else:
            print(f"Case with ID {case_id} not found.")

def update_case(case_id, title=None, description=None, client_id=None, lawyer_id=None):
    """Update a case."""
    with SessionLocal() as session:
        case = session.query(Case).get(case_id)
        if case:
            if title:
                case.title = title
            if description:
                case.description = description
            if client_id is not None:
                case.client_id = client_id
            if lawyer_id is not None:
                case.lawyer_id = lawyer_id
            session.commit()
            print(f"Updated case: ID: {case.id}, Title: {case.title}")
        else:
            print(f"Case with ID {case_id} not found.")


def exit_program():
    """Exit the program."""
    print("Exiting the program.")
    exit()
