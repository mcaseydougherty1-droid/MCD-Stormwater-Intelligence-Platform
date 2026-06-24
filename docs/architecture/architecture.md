MCD-Stormwater-Intelligence-Platform/

├── app/
│   ├── main.py
│   ├── pages/
│   └── components/

├── src/
│   └── mcd/
│       ├── gis/
│       │   ├── client.py
│       │   ├── pagination.py
│       │   ├── discovery.py
│       │   ├── catalog.py
│       │   ├── classifier.py
│       │   ├── county_finder.py
│       │   └── parcel_downloader.py
│       │
│       ├── intelligence/
│       │   ├── parcel_scoring.py
│       │   ├── hoa_detection.py
│       │   ├── bmp_detection.py
│       │   └── opportunity_scoring.py
│       │
│       ├── database/
│       │   ├── connection.py
│       │   ├── models.py
│       │   ├── migrations.py
│       │   └── repositories.py
│       │
│       ├── crm/
│       │   ├── contacts.py
│       │   ├── accounts.py
│       │   └── pipeline.py
│       │
│       ├── inspections/
│       │   ├── schedule.py
│       │   ├── forms.py
│       │   └── history.py
│       │
│       ├── proposals/
│       │   ├── generator.py
│       │   ├── pricing.py
│       │   └── templates.py
│       │
│       ├── routing/
│       │   ├── optimizer.py
│       │   └── routes.py
│       │
│       ├── reports/
│       │   ├── excel.py
│       │   ├── pdf.py
│       │   └── dashboards.py
│       │
│       └── utils/
│           ├── logging.py
│           └── paths.py

├── scripts/
│   ├── discover_butler_county.py
│   ├── download_adams_parcels.py
│   └── run_pipeline.py

├── tests/
│   ├── test_gis_client.py
│   ├── test_discovery.py
│   └── test_classifier.py

├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/

├── docs/
│   ├── architecture.md
│   ├── database_schema.md
│   ├── gis_engine.md
│   └── roadmap.md

├── config/
│   └── counties.yaml

├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore