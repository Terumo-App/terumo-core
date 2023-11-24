from pydantic import BaseModel


class BasicRequest(BaseModel):
    private_key: str
    public_key: str


class SearchRequest(BasicRequest):
    image_id: str
    collection_id: int
