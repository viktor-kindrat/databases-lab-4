from .general_service import GeneralService
from my_project.music.dao import compositor_dao


class CompositorService(GeneralService):
    _dao = compositor_dao

    def find_compositor_by_name(self, name: str):
        """Finds a Compositor by name using the DAO."""
        return self._dao.find_by_name(name)
