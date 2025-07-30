# Sample usage

from rwanda_locations_api.locs.locs import (
    get_provinces,
    get_districts_from_province,
    get_sectors_from_district,
    get_cells_from_sector,
    get_villages_from_cell,
    get_all_children
)
provinces = get_provinces()
print(provinces)
# districts = get_districts_from_province('Kigali')
# print(districts)
