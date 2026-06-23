from src.gis.county_finder import CountyLayerFinder

BUTLER_COUNTY_SERVER_URL = "https://geo.co.butler.pa.us/server/rest"


def main():
    finder = CountyLayerFinder(BUTLER_COUNTY_SERVER_URL)

    layers = finder.find_stormwater_layers()

    print(f"\nFound {len(layers)} matching GIS layers\n")

    for layer in layers:
        print(
            f"[{layer['category']}] "
            f"{layer['layer']}\n"
            f"    {layer['url']}\n"
        )


if __name__ == "__main__":
    main()