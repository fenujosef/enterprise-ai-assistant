from contextlib import AsyncExitStack

from mcp import ClientSessionGroup, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPServerManager:

    def __init__(
        self,
        servers: dict[str, StdioServerParameters],
    ):
        self.servers = servers
        self.group = ClientSessionGroup()


    async def connect_all(self):
        for server_params in self.servers.values():

            await self.group.connect_to_server(
                server_params
            )


    async def list_tools(self):
        return self.group.tools


    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ):
        available_tools = self.group.tools

        if tool_name not in available_tools:
            return f"Tool '{tool_name}' is not available."
        
        return await self.group.call_tool(
            tool_name,
            arguments=arguments,
        )


    async def close(self):
        await self.group.__aexit__(
            None,
            None,
            None
        )


# Custom MCP Manager
# class MCPClientManager:

#     def __init__(self, server_params: StdioServerParameters):
#         self.server_params = server_params
#         self.exit_stack = AsyncExitStack()
#         self.session = None

#     def __init__(
#         self,
#         servers: dict[str, StdioServerParameters],
#     ):
#         self.servers = servers
#         self.sessions = {}
#         self.exit_stack = AsyncExitStack()


#     # async def connect(self):
#     #     read, write = await self.exit_stack.enter_async_context(
#     #         stdio_client(self.server_params)
#     #     )

#     #     self.session = await self.exit_stack.enter_async_context(
#     #         ClientSession(read, write)
#     #     )

#     #     await self.session.initialize()

#     async def connect_all(self):

#         for name, server_params in self.servers.items():

#             read, write = await self.exit_stack.enter_async_context(
#                 stdio_client(server_params)
#             )

#             session = await self.exit_stack.enter_async_context(
#                 ClientSession(read, write)
#             )

#             await session.initialize()

#             self.sessions[name] = session


#     # async def list_tools(self):
#     #     if self.session is None:
#     #         raise RuntimeError("MCP client is not connected.")

#     #     result = await self.session.list_tools()

#     #     return result.tools

#     async def list_tools(self):

#         all_tools = []

#         for server_name, session in self.sessions.items():

#             result = await session.list_tools()

#             for tool in result.tools:

#                 all_tools.append(
#                     {
#                         "name": f"mcp.{server_name}.{tool.name}",
#                         "server": server_name,
#                         "tool": tool,
#                         "description": tool.description or "",
#                         "input_schema": tool.input_schema,
#                     }
#                 )

#         return all_tools

#     # async def call_tool(
#     #         self,
#     #         tool_name: str, 
#     #         arguments: dict,
#     # ):
#     #     if self.session is None:
#     #         raise RuntimeError("MCP client is not connected.")

#     #     return await self.session.call_tool(
#     #         tool_name,
#     #         arguments=arguments,
#     #     )

#     async def call_tool(
#         self,
#         server_name: str,
#         tool_name: str,
#         arguments: dict,
#     ):

#         session = self.sessions.get(server_name)

#         if session is None:
#             raise RuntimeError(
#                 f"MCP server '{server_name}' is not connected."
#             )

#         return await session.call_tool(
#             tool_name,
#             arguments=arguments,
#         )



#     async def close(self):
#         await self.exit_stack.aclose()
#         self.sessions.clear()