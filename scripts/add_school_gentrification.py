#!/usr/bin/python3
import geopandas as gpd
import pandas as pd

schools_df = pd.read_csv('../data/Map_of_Oakland_Public_Schools.csv')
schools_df['pos'] = schools_df['ADDRESS'].str.rfind('(')
schools_df['COORDINATES'] = schools_df.apply(lambda r: r['ADDRESS'][r['pos']:], axis=1)
schools_df['COORDINATES'] = schools_df['COORDINATES'].replace(" ", "").str.strip('(').str.strip(')')
schools_df['LAT'] = schools_df['COORDINATES'].str.split(',').str[0]
schools_df['LON'] = schools_df['COORDINATES'].str.split(',').str[1]
del schools_df['COORDINATES']
del schools_df['pos']

schools_gdf = gpd.GeoDataFrame(schools_df, geometry=gpd.points_from_xy(schools_df['LON'], schools_df['LAT']))

gent_gdf = gpd.read_file('../data/sanfrancisco.gpkg')

schools_gdf = schools_gdf.set_crs(gent_gdf.crs)

schools_gent = gpd.sjoin(schools_gdf, gent_gdf, how='left', op='intersects')

schools_gent.to_file("../data/school_gentrification.gpkg", driver="GPKG")
