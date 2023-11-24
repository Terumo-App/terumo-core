from pydantic import BaseModel, Field


class ImageResponse(BaseModel):  # define your model
    image_id: int = Field(..., example=1)
    collection_id: int = Field(..., example=25242)
    originalFilename: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    instanceFilename: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    path: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    thumb: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    preview: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    distance: float = Field(..., example=0.5)
