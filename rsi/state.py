from PIL import Image
from typing import List, Tuple, Dict
from .helpers import state_name


class State(object):
    def __init__(self, name: str, selectors: List[str], size: Tuple[int, int], directions: int = 1):
        self.name = name  # type: str
        self.selectors = selectors or []  # type: List[str]
        self.full_name = state_name(self.name, self.selectors)  # type: str
        self.flags = {}  # type: Dict[str, Any]
        self.size = size  # type: Tuple[int, int]
        self.directions = directions  # type: int

        self.delays = [[] for i in range(self.directions)]  # type: List[List[float]]
        self.icons = [[] for i in range(self.directions)]  # type: List[List[Image]]
