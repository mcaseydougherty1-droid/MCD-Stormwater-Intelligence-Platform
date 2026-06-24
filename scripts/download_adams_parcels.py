from mcd.gis.parcel_downloader import download_adams_township_parcels


def main() -> None:
    parcels = download_adams_township_parcels()

    print(f"Downloaded {len(parcels)} Adams Township parcels")
    print("Saved to data/raw/adams_township_parcels.csv")
    print("Saved to data/raw/adams_township_parcels.json")


if __name__ == "__main__":
    main()