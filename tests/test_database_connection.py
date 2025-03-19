import pytest
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
from sql_query_agency.util.config import Settings

@pytest.mark.asyncio
async def test_database_connection():
    server_params = StdioServerParameters(
        command="docker",
        args=["run", "--rm", "-i", "mcp/postgres:latest", Settings().DATABASE_URL],
    )
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
    except Exception as e:
        pytest.fail(f"Database connection failed with error: {e}")
