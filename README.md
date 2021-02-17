# Overview
Repo to use to brainstorm ideas for our project for GDA 2021. Not intended to have "perfect" style or anything.

## Specific Notes
Notes specific to different parts of the repo
### Merging School Locations with UDP Gentrification Classifications 
Script is in `scripts/add_school_gentrification.py`. This is meant to be run from inside the `scripts` directory. For example, you should run:
```bash
$ cd scripts
$ python add_school_gentrification.py
```

Produces the file `data/school_gentrification.gpkg`. This can be read using `Python` and `geopandas` as follows:
```python
import geopandas as gpd

school_gentrification_codes = gpd.read_file("data/school_gentrification.gpkg")
```
