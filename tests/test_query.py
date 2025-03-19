import pytest
from sql_query_agency.main import async_main

@pytest.mark.asyncio
async def test_query_processing():
    query = "SELECT * FROM users;"
    try:
        await async_main(query)
    except Exception as e:
        pytest.fail(f"Query processing failed with error: {e}")
