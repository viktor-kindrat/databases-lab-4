from .general_dao import GeneralDAO
from my_project.music.domain import Album
from sqlalchemy.orm import Session


class AlbumDAO(GeneralDAO):
    _domain_type = Album

    def find_by_name(self, name: str) -> Album | None:
        return self._session.query(self._domain_type).filter_by(name=name).first()
