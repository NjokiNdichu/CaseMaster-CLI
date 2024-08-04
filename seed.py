from db.models import SessionLocal, Client, Lawyer, Case

def seed_database():
    with SessionLocal() as session:
        clients = [
            Client(name="John Doe"),
            Client(name="Jane Smith"),
            Client(name="Emily Davis"),
            Client(name="Michael Brown"),
            Client(name="Linda Johnson"),
            Client(name="James Wilson"),
            Client(name="Patricia Taylor"),
            Client(name="Robert Anderson"),
            Client(name="Maria Martinez"),
            Client(name="David Thompson")
        ]
        session.add_all(clients)
        session.commit()

        
        lawyers = [
            Lawyer(name="Alice Johnson"),
            Lawyer(name="Bob Brown"),
            Lawyer(name="Carol White"),
            Lawyer(name="Daniel Black"),
            Lawyer(name="Eva Green"),
            Lawyer(name="Frank Adams"),
            Lawyer(name="Grace Harris"),
            Lawyer(name="Henry Clark"),
            Lawyer(name="Ivy Lewis"),
            Lawyer(name="Jack Walker")
        ]
        session.add_all(lawyers)
        session.commit()

        
        cases = [
            Case(title="Case 1", client_id=clients[0].id, lawyer_id=lawyers[0].id),
            Case(title="Case 2", client_id=clients[1].id, lawyer_id=lawyers[1].id),
            Case(title="Case 3", client_id=clients[2].id, lawyer_id=lawyers[2].id),
            Case(title="Case 4", client_id=clients[3].id, lawyer_id=lawyers[3].id),
            Case(title="Case 5", client_id=clients[4].id, lawyer_id=lawyers[4].id),
            Case(title="Case 6", client_id=clients[5].id, lawyer_id=lawyers[5].id),
            Case(title="Case 7", client_id=clients[6].id, lawyer_id=lawyers[6].id),
            Case(title="Case 8", client_id=clients[7].id, lawyer_id=lawyers[7].id),
            Case(title="Case 9", client_id=clients[8].id, lawyer_id=lawyers[8].id),
            Case(title="Case 10", client_id=clients[9].id, lawyer_id=lawyers[9].id)
        ]
        session.add_all(cases)
        session.commit()

if __name__ == "__main__":
    seed_database()
