# inventory-service
Inventory Service APIs with Python FAST API

## Development Setup

This project uses a Python virtual environment and a Makefile to simplify setup and running the application.

### Prerequisites

- Python 3.7+
- `make` utility (commonly available on Linux/macOS)

## Poetry Installation

You can install [Poetry](https://python-poetry.org/) (a Python dependency management tool) using one of the following methods:

**Recommended (Official Script):**
```sh
curl -sSL https://install.python-poetry.org | python3 -
```

**Or, using apt (for Ubuntu/Debian):**
```sh
sudo apt install python3-poetry
```

**Verify the installation:**
```sh
poetry --version
```

## Initialize the Project with Poetry

After installing Poetry, run the following command **once** to initialize the project and set up the basic configuration:

```sh
poetry init --name "inventory-service" --dependency fastapi --dependency uvicorn --python "^3.12"
```

This will create a `pyproject.toml` file with the specified project name, dependencies, and Python version.

## Install Project Dependencies

To add all required dependencies for this project, run:

```sh
poetry add fastapi uvicorn[standard] sqlalchemy pydantic pydantic-settings passlib[bcrypt] python-dotenv
```

This command will:
- Add FastAPI and Uvicorn (with standard extras) for the web API.
- Add SQLAlchemy for database ORM.
- Add Pydantic and Pydantic Settings for data validation and settings management.
- Add Passlib with bcrypt for password hashing.
- Add python-dotenv for environment variable management.

All dependencies will be recorded in your `pyproject.toml` and installed in Poetry's virtual environment.

## Makefile Commands

The following commands use [Poetry](https://python-poetry.org/) to manage dependencies and run your application.

| Command         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `make install`  | Installs all dependencies using Poetry as specified in `pyproject.toml`.     |
| `make run`      | Runs the application inside Poetry's virtual environment.                    |
| `make shell`    | Opens a shell with the Poetry environment activated.                         |

#### Example Usage

```sh
# Install dependencies
make install

# Run the application
make run

# Open a Poetry shell (for running commands interactively)
make shell
```

---

Feel free to further customize these instructions based on your project's needs!
