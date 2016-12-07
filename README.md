# heroku-jupyter

Use this application to deploy [Jupyter Notebook](https://jupyter.org/) to
heroku or CloudFoundry. If a postgres database is available,
[pgcontents](https://github.com/quantopian/pgcontents) is used as notebook
storage.

## Quick start

Jupyter will not start, if the environment variable `JUPYTER_NOTEBOOK_PASSWORD`
was not set.

If you want to customize your app, easiest is to fork this repository.

## Installation instructions

### heroku - automatic deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you forked this repository, you can link it to your heroku app afterwards.

### heroku - manual deployment

Push this repository to your app or fork this repository on github and link your
repository to your heroku app.

Use the [heroku-buildpack-conda](https://github.com/pl31/heroku-buildpack-conda):
```
$ heroku buildpacks:set https://github.com/pl31/heroku-buildpack-conda.git -a <your_app>
```

Jupyter notebook will not start until the environment variable
`JUPYTER_NOTEBOOK_PASSWORD` is set. Use a good password:
```
$ heroku config:set JUPYTER_NOTEBOOK_PASSWORD=<your_passwd> -a <your_app>
```

If you are really sure, that you do not want a password protected notebook
server, you can set `JUPYTER_NOTEBOOK_PASSWORD_DISABLED` to `DangerZone!`.

### CloudFoundry

- Clone this repository
- Create a postgres database service with name `jupyter-db`
- Deploy using `cf push`
- Set `JUPYTER_NOTEBOOK_PASSWORD` using `cf set-env`. Do not forget to restart application.

## Environment variables

- `JUPYTER_NOTEBOOK_PASSWORD`: Set password for notebooks
- `JUPYTER_NOTEBOOK_PASSWORD_DISABLED`: Set to `DangerZone!` to disable password
  protection
- `JUPYTER_NOTEBOOK_ARGS`: Additional command line args passed to
  `jupyter notebook`; e.g. get a more verbose logging using `--debug`

## Python version

If you want to use a special python version, you should set it in your environment.yml:

```
name: root
dependencies:
  - python=2.7
  - ...
```
