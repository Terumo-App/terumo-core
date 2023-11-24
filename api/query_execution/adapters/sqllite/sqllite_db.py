import uuid

from query_execution.domain.image.image_entity import ImageEntity
from sqlalchemy import Column, Integer, String, Uuid, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from query_execution.domain.image.sql_db_interface import SQLDBInterface

DB_PATH = 'sqlite:///image_database.db'

base = declarative_base()


class ImageDAO(base):
    __tablename__ = 'images'

    id = Column(Uuid, primary_key=True)
    filename = Column(String)
    filepath = Column(String)


class SQLLiteDBImp(SQLDBInterface):
    def __init__(self):
        self.engine = create_engine(DB_PATH, echo=True)
        self.session = None
        self.setup()

    def setup(self):
        base.metadata.create_all(bind=self.engine)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def get_image_path(self, image_id: str) -> str:
        image_data = (
            self.session.query(ImageDAO)
            .filter_by(id=uuid.UUID(image_id))
            .first()
        )

        if not image_data:
            return Exception('Image not found in SQL Lite')

        return {
            'id': image_data.id,
            'filename': image_data.filename,
            'filepath': image_data.filepath,
        }

    def save_image(self, file_name: str, image_location: str) -> ImageEntity:
        image_id = uuid.uuid4()
        image_data = ImageDAO(
            id=image_id, filename=file_name, filepath=image_location
        )
        self.session.add(image_data)
        self.session.commit()
        return ImageEntity(image_id=image_data.id, collection_id=None)
