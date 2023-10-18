from pydantic import BaseModel


class BasicRequest(BaseModel):
    private_key: str
    public_key: str


class CollectionCretionRequest(BasicRequest):
    collection_name: str

class ImageRequest(BasicRequest):
    collection_id: int
