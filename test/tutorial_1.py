from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="tutorial_1")

@mcp.tool()
def echo(message: str) -> str:
    '''
    입력받은 메시지를 그대로 반환화는 도구입니다.
    '''
    return message + " 라는 메시지가 입력되었습니다. 안 찍어 볼 수 없죠! Hello World!"

if __name__ == "__main__":
    mcp.run()