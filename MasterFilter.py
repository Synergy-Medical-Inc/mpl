from Filters import *
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="test1-312816-ccd9308ee8ad.json"
client = sm.SecretManagerServiceClient()
secrets = f"projects/481475670378/secrets/sql-query3/versions/1"
response = client.access_secret_version(request={"name": secrets})
payload = response.payload.data.decode("UTF-8")
#Daily filter

# combines the multiple data frames and from scan unlimited

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('/pyproj', "*df*.csv"))))

# preforms the SQL query
sql_connect = sql.connect('/SqlData/daily.db')
cursor = sql_connect.cursor()
df.to_sql("master_prod", sql_connect, if_exists="replace")
results = cursor.execute(payload).fetchall()

# prints master list in python and as a csv
master_prod = pd.read_sql_query(payload,sql_connect)
print(master_prod)
master_prod.to_csv('/pyproj/mpl/Test4.csv', index=False)
print(master_prod)


