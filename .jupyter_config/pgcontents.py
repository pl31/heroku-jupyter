import os
from pgcontents import PostgresContentsManager

c = get_config()

# Tell IPython to use PostgresContentsManager for all storage.
c.NotebookApp.contents_manager_class = PostgresContentsManager

# get connection string from environment
c.PostgresContentsManager.db_url = os.getenv('DATABASE_URL')
