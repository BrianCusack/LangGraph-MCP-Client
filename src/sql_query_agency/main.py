
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from langchain_anthropic import ChatAnthropic
import asyncio
import logging
from sql_query_agency.util.config import Settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

model = ChatAnthropic(model_name = "claude-3-7-sonnet-latest",  
                    temperature=0,
                    timeout=None,
                    max_retries=2,)

# the server needs to pre-built with docker as mcp/postgres:latest
server_params = StdioServerParameters(
    command="docker",
    args=["run", "--rm", "-i", "mcp/postgres:latest", Settings().DATABASE_URL],
)


# Create a client connection to the server
async def main(query: str):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            logging.info("Connection initialized")

            # Get tools
            tools = await load_mcp_tools(session)
            logging.info("Tools loaded")

            # Create and run the agent
            agent = create_react_agent(model, tools)
            logging.info("Agent created")

            # Stream the agent's response
            collector = []
            async for chunk in agent.astream(input={"messages": query}, stream_mode="values"):
                message = chunk["messages"][-1].content
                logging.info(f"Received chunk: {message}")
                collector.append(f'{message}\n')
            
            with open("output.txt", "w") as f:
                f.write(str(collector))


if __name__ == "__main__":

    question = "How many people have savings accounts? get the postgresql database schema first, always plan your execution"

    res = asyncio.run(main(question))
