# CaseMaster CLI

**CaseMaster CLI** is a command-line tool designed for managing legal cases, clients, and lawyers. It provides an intuitive menu system for performing essential CRUD operations and navigating through the application. This project is ideal for legal professionals who need a straightforward interface for case management.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Installation](#installation)
4. [Dependencies](#dependencies)
5. [Usage](#usage)
6. [Tools Used](#tools-used)
7. [Contributing](#contributing)

## Project Description

**CaseMaster CLI** allows users to manage clients, lawyers, and cases through a command-line interface. It supports operations such as adding, listing, finding by ID, deleting, and updating records. The application features a main menu that facilitates navigation and maintains an active session until the user decides to exit.

## Features

- **Client Management**: Add, list, find by ID, delete, and update clients.
- **Lawyer Management**: Add, list, find by ID, delete, and update lawyers.
- **Case Management**: Add, list, find by ID, delete, and update cases.
- **Navigation**: Main menu with options to manage clients, lawyers, cases, or exit.

## Installation

To get started with **CaseMaster CLI**, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/casemaster-cli.git
   cd casemaster-cli
   ```
2. **Set Up the Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt

   ```

4. **Initialize Alembic:**
   Alembic is used for managing database migrations. To set up alembic, use the following command:

   ```bash
   alembic init alembic
   ```

   This command creates an `alembic` directory with migration scripts and an `alembic.ini` configuration file.

5. **Configure Alembic:**
   Edit `alembic.ini` to set the correct database URL:

   ```ini
   [alembic]
   # path to migration scripts
   script_location = alembic

   [logger_alembic]
   level = INFO

   [sqlalchemy]
   url = sqlite:///./contactmanagement.db
   ```

6. **Create Initial Migration:**
   Generate the initial migration script based on your models:

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

7. **Apply Migrations:**
   Apply the migrations to your database:
   ```bash
   alembic upgrade head
   ```

## Dependencies

- Click: For creating the CLI interface.
- SQLAlchemy: For ORM and database operations.
- Alembic: For database migrations.
- SQLite3: For the database engine.
  Dependencies are listed in requirements.txt and can be installed with:

      ```bash
      pip install -r requirements.txt
      ```

## Usage

To run the CLI:

```bash
python cli.py
```

## Tools Used

- **Python**: Programming language used for development.
- **SQLAlchemy**: ORM for database interactions.
- **Click**: Library for creating the CLI.
- **Alembic**: Tool for managing database migrations.
- **SQLite3**: Database for storing records.

## Contributing

Contributions to CaseMaster CLI are welcome! Please follow these steps:

1. **Fork the Repository.**
2. **Create a New Branch:**
   ```bash
   git checkout -b feature-branch
   ```
3. **Make Your Changes.**
4. **Commit and Push:**
   ```bash
   git commit -m 'Add new feature'
   git push origin feature-branch
   ```
5. **Create a Pull Request.**

## License
CaseMaster CLI is licensed under the MIT License. See `LICENSE` for details.
