# heroku-jupyter

Example how to deploy [Jupyter Notebook](https://jupyter.org/) to heroku. 
Push this repository to your app or fork this repository on github and link your 
repository to your heroku app.

Use the [heroku-buildpack-conda](https://github.com/p-a-c-o/heroku-buildpack-conda):
```
heroku buildpacks:set https://github.com/p-a-c-o/heroku-buildpack-conda.git -a <your_app>
```

To protect your notebooks a random password is used until you set the environment variable `JUPYTER_NOTEBOOK_PASSWORD`:
```
heroku config:set JUPYTER_NOTEBOOK_PASSWORD=<your_passwd> -a <your_app>
```

## pgcontents

To store your notebooks, you can use pgcontents.

First add an "Heroku Postgres" Add-On to your app.

```
pgcontents init --db-url $DATABASE_URL --no-prompt                                                                                    
```                                                                                                                                       
                                       
