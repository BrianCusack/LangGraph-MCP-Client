import pytest
from langchain_anthropic import ChatAnthropic

from sql_query_agency.util.config import Settings

settings = Settings()

@pytest.mark.asyncio
async def test_chat_anthropic_query():
    model = ChatAnthropic(
        model_name=settings.CLAUDE_MODEL,
        temperature=0,
        timeout=None,
        max_retries=2,
    )
    try:
        # Pass a valid string instead of a dictionary
        response = await model.apredict("Hello, Claude!")
        assert response is not None, "Model did not return a response"
    except Exception as e:
        pytest.fail(f"ChatAnthropic query failed with error: {e}")
