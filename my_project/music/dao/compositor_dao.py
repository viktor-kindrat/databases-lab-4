from __future__ import annotations
from .general_dao import GeneralDAO

from my_project.music.domain import Compositor


class CompositorDAO(GeneralDAO):
    _domain_type = Compositor

    def find_by_name(self, name: str) -> Compositor | None:
        """Find a Compositor by name."""
        return self._session.query(self._domain_type).filter_by(name=name).first()
