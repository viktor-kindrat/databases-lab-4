from typing import Optional, Dict, Any
from my_project.music.service import album_service
from my_project.label.controller.general_controller import GeneralController


class AlbumController(GeneralController):
    _service = album_service

    def get_album_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        album = self._service.find_album_by_name(name)
        return album.put_into_dto() if album else None
