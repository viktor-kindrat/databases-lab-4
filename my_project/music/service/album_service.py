from .general_service import GeneralService
from my_project.music.dao import album_dao


class AlbumService(GeneralService):
    _dao = album_dao

    def find_album_by_name(self, name: str):
        return self._dao.find_by_name(name)
