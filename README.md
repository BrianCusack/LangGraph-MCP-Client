# Langchain-MCP

This repository demonstrates how to use a UV package to interact with an MCP server as a docker image, connected to a PostgreSQL database. Follow the steps below to set up and use this repository.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [A PostgreSQL Database](https://www.postgresql.org/)
- [MCP Postgresql Server](https://github.com/modelcontextprotocol/servers)

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/Langchain-MCP.git
cd Langchain-MCP
```

### 2. Create a `.env` File
Create a `.env` file in the root of the repository with the following variables:
```
DB_HOST=<your-database-host>
DB_PORT=<your-database-port>
DB_USER=<your-database-username>
DB_PASSWORD=<your-database-password>
DB_NAME=<your-database-name>
```

Replace the placeholders with your actual database and MCP server connection details.

### 3. Install UV Package
Install the UV package globally if you haven't already:

[Astral uv](https://docs.astral.sh/uv/)

---

## Usage Instructions

### 1. Sync the UV Package
Run the following command to sync the UV package:
```bash
uv sync
```

This command ensures that the UV package is properly configured with the MCP server and database.

### 2. Run the Query Agent
Start the query agent using the following command:
```bash
uv run queryagent
```

This will execute the query agent, which interacts with the MCP server and database.

---

## Troubleshooting

- **Database Connection**: Verify the `.env` file contains the correct database credentials.
- **UV Package Errors**: Ensure the UV CLI is installed globally and the `uv sync` command completes without errors.

---

## Contributing

Feel free to open issues or submit pull requests to improve this repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
