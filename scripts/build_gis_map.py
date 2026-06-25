import pandas as pd

from mcd.mapping.bmp_mapper import prepare_bmp_map_points
from mcd.mapping.interactive_map import build_html_map
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    bmp_inventory_path = PROCESSED_DATA_DIR / "adams_bmp_inventory.csv"
    output_path = EXPORTS_DIR / "adams_interactive_map.html"

    bmp_inventory = pd.read_csv(bmp_inventory_path)
    points = prepare_bmp_map_points(bmp_inventory)

    build_html_map(points, output_path)

    print(f"BMP inventory records: {len(bmp_inventory)}")
    print(f"Map points with coordinates: {len(points)}")
    print(f"Saved map to {output_path}")


if __name__ == "__main__":
    main()
