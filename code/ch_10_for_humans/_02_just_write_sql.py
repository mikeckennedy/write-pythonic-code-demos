import records
# noinspection PyProtectedMember
from ch_10_for_humans._02_just_write_sql_support import conn_str

print(conn_str)

db = records.Database(conn_str)
rows = db.query("SELECT * FROM Measurement WHERE value > .9 "
                "ORDER BY value DESC")

for r in rows[:5]:
    print(r)
