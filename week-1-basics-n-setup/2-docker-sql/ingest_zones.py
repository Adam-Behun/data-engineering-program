# Script inputting zones data into postgres database

import pandas as pd
from sqlalchemy import create_engine

df_zones = pd.read_csv('taxi_zone_lookup.csv')
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

print(pd.io.sql.get_schema(df_zones, name='zones', con=engine))

df_zones.head().to_sql(name='zones', con=engine, if_exists='replace')

df_zones.to_sql(name='zones', con=engine, if_exists='append')
