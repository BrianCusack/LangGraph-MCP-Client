# Langgraph-MCP Client for Postgresql Example

This repository demonstrates a very low level example of how to interact with an MCP server as a docker image, connected to a PostgreSQL database for LangGraph agents.

[model context protocol](https://modelcontextprotocol.io/introduction)
>MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [PostgreSQL Database](https://www.postgresql.org/) - running and populated
- [MCP Servers](https://github.com/modelcontextprotocol/servers)

---

## Flow and tools
- We use a postgresql database that the Postgresl MCP Server is aware of through the config
- `from langchain_mcp_adapters.tools import load_mcp_tools` creates the mcp tool 
- `create_react_agent` is a fast agent templater
- we output the stream to file 

## Project Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-repo/Langchain-MCP.git
cd Langgraph-mcp-client directory
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

## MCP Server Setup

1. Clone the repo [MCP Servers](https://github.com/modelcontextprotocol/servers) to a separate directory
2. Run - `docker build -t mcp/postgres -f src/postgres/Dockerfile .` to build and tag the image


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

## TODO:
- Output formating 
- Multi agent 

## Troubleshooting

- **Database Connection**: Verify the `.env` file contains the correct database credentials.
- **UV Package Errors**: Ensure the UV CLI is installed globally and the `uv sync` command completes without errors.

---

## Contributing

Feel free to open issues or submit pull requests to improve this repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
