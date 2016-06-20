import os

db_file = os.path.join(os.path.dirname(__file__), 'demo_db.sqlite')
conn_str = 'sqlite:///' + db_file
