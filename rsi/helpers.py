from typing import List


def state_name(name: str, selectors: List[str]) -> str:
    if selectors is not None and len(selectors) > 0:
        name += "+" + "+".join(sorted(selectors))

    return name
