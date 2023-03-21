from utils.constants import Align
from typing import Tuple

def align(x: int, y: int, width: int, height: int, anchor: Align) -> Tuple[int, int]:
    return x - width / 2  * anchor.value[0], y - height / 2 * anchor.value[1]