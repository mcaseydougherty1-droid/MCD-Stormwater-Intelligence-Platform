from mcd.gis.county_finder import CountyLayerFinder

BUTLER_COUNTY_SERVER_URL = "https://geo.co.butler.pa.us/server/rest"


def main() -> None:
    finder = CountyLayerFinder(BUTLER_COUNTY_SERVER_URL)

    layers = finder.find_relevant_layers()

    print(f"\nFound {len(layers)} relevant GIS layers\n")

    for layer in layers:
        print(
            f"[{layer['category']}] "
            f"{layer['layer']} "
            f"({layer['service']} / {layer['service_type']})"
        )
        print(f"    {layer['url']}\n")


if __name__ == "__main__":
    main()