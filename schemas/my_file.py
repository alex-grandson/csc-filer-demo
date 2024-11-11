from pydantic import BaseModel


class MyFile(BaseModel):
    """
    Common class to work with files
    """
    name: str
    type: str
    """
    "directory" / "file"
    """
