# Rwanda Locations API

A Python package and FastAPI-based API providing comprehensive administrative location data for Rwanda — from provinces down to villages.

---

## Features

- Access Rwanda’s administrative hierarchy:
  - Provinces
  - Districts
  - Sectors
  - Cells
  - Villages
- Easy-to-use Python package for integration in your projects.
- Ready-to-use FastAPI endpoints for quick REST API deployment.
- Location names are case-insensitive for better usability.

---

## Installation

```bash
pip install rwanda-locations-api

```

## Usage

```
from rwanda_locations_api.locs.data import get_provinces, get_districts, get_sectors, get_cells, get_villages

# Get all provinces
provinces = get_provinces()
print(provinces)

# Get districts in a province
districts = get_districts("Kigali")
print(districts)

# Get sectors in a district
sectors = get_sectors("Kigali", "Gasabo")
print(sectors)

# Get cells in a sector
cells = get_cells("Kigali", "Gasabo", "Kimironko")
print(cells)

# Get villages in a cell
villages = get_villages("Kigali", "Gasabo", "Kimironko", "Nyarutarama")
print(villages)

```

## As a FastAPI service

```
uvicorn main:app --reload

```

#### Available end-points

```

GET /provinces

GET /districts/{province}

GET /sectors/{province}/{district}

GET /cells/{province}/{district}/{sector}

GET /villages/{province}/{district}/{sector}/{cell}
```

## Development

```
git clone https://github.com/itbienvenu/rwanda-location-api.git
cd rwanda-location-api

```
##### Create virtual environment and install dependencies

```
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt

```

#### Then run FASTAPI server

```
uvicorn main:app --reload

```


## Contributing 

Contributions, issues, and feature requests are welcome!
Feel free to check issues or submit a pull request.


# Author
MWIMULE Bienvenu\
<b>GitHub</b>: @itbienvenu\
<b>Email</b>: mwimulebienvenu05@gmail.com
