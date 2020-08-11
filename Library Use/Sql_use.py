from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///:memory:')
sql_df = pd.read_sql('data',con=engine)  #read
df.to_sql('data', engine) #write