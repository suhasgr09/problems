"""Example runner for the package dispatcher."""

from package_dispatcher import sort


def main() -> None:
    examples = [
        (10, 10, 10, 5),        # Small and light
        (100, 100, 100, 10),    # Bulky (volume = 1,000,000) but light
        (150, 10, 10, 5),       # Bulky (dimension >= 150) but light
        (10, 10, 10, 25),       # Small but heavy
        (100, 100, 100, 20),    # Bulky and heavy
        (200, 50, 50, 30),      # Bulky (dimension >= 150) and heavy
        (99, 100, 100, 19),     # Just under both thresholds
    ]

    print("=" * 60)
    print(f"{'Width':>6} {'Height':>6} {'Length':>6} {'Mass':>6}  -> {'Stack'}")
    print("=" * 60)
    for width, height, length, mass in examples:
        result = sort(width, height, length, mass)
        print(f"{width:>6} {height:>6} {length:>6} {mass:>6}  -> {result}")
    print("=" * 60)


if __name__ == "__main__":
    main()
