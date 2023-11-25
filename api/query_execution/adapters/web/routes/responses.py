from pydantic import BaseModel, Field

class Picture(BaseModel):
    large: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=512',
    )
    medium: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=1000',
    )
    thumbnail: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png?maxSize=2000',
    )


class Name(BaseModel):
    last: str = Field(..., example='image.png')


class ImageResponse(BaseModel):  # define your model
    id: int = Field(..., example=1)
    image_url: str = Field(
        ...,
        example='http://maods.homelab.core/api/abstractimage/1548/thumb.png',
    )
    picture: Picture
    name: Name
    score: float = Field(..., example=0.5)
