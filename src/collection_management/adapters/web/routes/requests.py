from pydantic import BaseModel


class CollectionRequest(BaseModel):
    private_key: str
    public_key: str


class CollectionCretionRequest(BaseModel):
    private_key: str
    public_key: str
    collection_name: str
