from pydantic import BaseModel


class CollectionRequest(BaseModel):
    primary_key: str
    public_key: str


class CollectionCretionRequest(BaseModel):
    primary_key: str
    public_key: str
    collection_name: str
