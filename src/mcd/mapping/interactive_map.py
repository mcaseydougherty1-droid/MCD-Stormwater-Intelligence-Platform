from pathlib import Path

import pandas as pd


def build_html_map(points: pd.DataFrame, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []

    for _, row in points.iterrows():
        rows.append(
            f"""
            <tr>
                <td>{row.get("Owner", "")}</td>
                <td>{row.get("PIN", "")}</td>
                <td>{row.get("Property_Address", "")}</td>
                <td>{row.get("BMP_Type", "")}</td>
                <td>{row.get("Latitude", "")}</td>
                <td>{row.get("Longitude", "")}</td>
                <td>{row.get("Estimated_Annual_Cost", "")}</td>
            </tr>
            """
        )

    html = f"""
    <html>
    <head>
        <title>MCD Adams Township Stormwater Asset Map</title>
    </head>
    <body>
        <h1>MCD Adams Township Stormwater Asset Map</h1>
        <p>This first map export lists BMP assets with available coordinates. Interactive GIS visualization will be added in a later release.</p>
        <table border="1" cellpadding="6" cellspacing="0">
            <tr>
                <th>Owner</th>
                <th>PIN</th>
                <th>Address</th>
                <th>BMP Type</th>
                <th>Latitude</th>
                <th>Longitude</th>
                <th>Estimated Annual Cost</th>
            </tr>
            {''.join(rows)}
        </table>
    </body>
    </html>
    """

    output_path.write_text(html, encoding="utf-8")

    return output_path
