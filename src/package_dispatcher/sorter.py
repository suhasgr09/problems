"""Core package sorting logic."""


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch a package to the correct stack based on dimensions and mass.

    Args:
        width: Width in cm
        height: Height in cm
        length: Length in cm
        mass: Mass in kg

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED"
    """
    bulky = (
        width * height * length >= 1_000_000
        or any(dim >= 150 for dim in (width, height, length))
    )
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
