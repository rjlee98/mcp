from mcp.server.fastmcp import FastMCP

# Create a MCP server
mcp = FastMCP("server")

@mcp.tool()
def create_folder(folder_name: str) -> str:
    """
    D:/test/ 아래 폴더를 생성합니다.

    Parameters
    ----------
    folder_name : str
        생성할 폴더 이름

    Returns
    ---------
    str
       생성 결과 메시지
    """       
    import os

    folder_path = os.path.join("D:\\test", folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        return f"{folder_name} 폴더가 생성되었습니다."
    else:
        return f"{folder_name} 폴더가 이미 존재합니다."

@mcp.tool()
def delete_folder(folder_name: str) -> str:
    """
    D:/test/ 아래 폴더를 삭제합니다.

    Parameters
    ----------
    folder_name : str
        삭제할 폴더 이름

    Returns
    ----------
    str
       삭제 결과 메시지
   """    
    import os

    folder_path = os.path.join("D:\\test", folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        return f"{folder_name} 폴더가 삭제되었습니다."
    else:
        return f"{folder_name} 폴더가 존재하지 않습니다."

@mcp.tool()
def list_folder() -> list:
    """
    D:\test\ 아래 폴더 목록을 반환합니다.

    Returns
    ----------
    list
        폴더 목록
    """
    import os

    folder_path = "D:\\test"
    folders = [
        f
        for f in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, f))

    ]
    return folders

    
# 서버 실행하기

if __name__ == "__main__":
    mcp.run()