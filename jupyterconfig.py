import os
import uuid
import IPython.lib

c = get_config()

### Password protection ###
c.NotebookApp.password = IPython.lib.passwd(
    os.getenv('JUPYTER_NOTEBOOK_PASSWORD', default=str(uuid.uuid4())))

import pgcontents

### PostresContentsManager ###
database_url = os.getenv('DATABASE_URL', None)
if database_url:
    # Tell IPython to use PostgresContentsManager for all storage.
    c.NotebookApp.contents_manager_class = pgcontents.PostgresContentsManager
    
    # Set the url for the database used to store files.  See
    # http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#postgresql
    # for more info on db url formatting.
    c.PostgresContentsManager.db_url = database_url
    
    # PGContents associates each running notebook server with a user, allowing
    # multiple users to connect to the same database without trampling each other's
    # notebooks. By default, we use the result of result of getpass.getuser(), but
    # a username can be specified manually like so:
    c.PostgresContentsManager.user_id = 'heroku'
    
    # Set a maximum file size, if desired.
    #c.PostgresContentsManager.max_file_size_bytes = 1000000 # 1MB File cap
