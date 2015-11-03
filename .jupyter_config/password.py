import os
import uuid
import IPython.lib

c = get_config()
c.NotebookApp.password = IPython.lib.passwd(
    os.getenv('JUPYTER_NOTEBOOK_PASSWORD', default=str(uuid.uuid4())))
