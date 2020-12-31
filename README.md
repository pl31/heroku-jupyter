# heroku-jupyter

*В настоящее время ни одна из конфигураций не работает должным образом.
Я не могу понять рабочий environment.yml.
К сожалению, старые конфигурации не работают, поскольку устарели
пакеты были удалены из пакета repositories.*

* Вместо использования анаконды было бы более стабильно создать
контейнер докеров для запуска в Heroku. См. Пример
[heroku-debian-jupyter](https://github.com/pl31/heroku-debian-jupyter),
но по-прежнему нет поддержки кнопки развертывания heroku из heroku*

Используйте это приложение для развертывания[Jupyter Notebook](https://jupyter.org/) to
heroku or CloudFoundry. Если доступна база данных postgres,
[pgcontents](https://github.com/quantopian/pgcontents) используется как ноутбук
место хранения.

## Quick start

Jupyter не запустится, если переменная окружения `JUPYTER_NOTEBOOK_PASSWORD`
не было установлено.

Если вы хотите настроить свое приложение, проще всего создать форк этого репозитория.

## Installation instructions

### heroku - automatic deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Если вы форкнули этот репозиторий, вы можете впоследствии связать его со своим приложением heroku.

### heroku - manual deployment

Загрузите этот репозиторий в свое приложение или создайте форк этого репозитория на github и свяжите свой
репозиторий в ваше приложение heroku.

Использовать [heroku-buildpack-conda](https://github.com/pl31/heroku-buildpack-conda):
```
$ heroku buildpacks:set https://github.com/pl31/heroku-buildpack-conda.git -a <your_app>
```

Блокнот Jupyter не запустится, пока не будет указана переменная среды
`JUPYTER_NOTEBOOK_PASSWORD` установлен. Используйте хороший пароль:
```
$ heroku config:set JUPYTER_NOTEBOOK_PASSWORD=<your_passwd> -a <your_app>
```

Если вы действительно уверены, что вам не нужен защищенный паролем блокнот
сервер, вы можете установить `JUPYTER_NOTEBOOK_PASSWORD_DISABLED` to `DangerZone!`.

### CloudFoundry

- Клонировать этот репозиторий
- Создайте службу базы данных postgres с именем `jupyter-db`
- Развернуть с помощью `cf push`
- Набор `JUPYTER_NOTEBOOK_PASSWORD` с помощью`cf set-env`. Не забудьте перезапустить приложение.

## Environment variables

- `JUPYTER_NOTEBOOK_PASSWORD`: Установить пароль для записных книжек
- `JUPYTER_NOTEBOOK_PASSWORD_DISABLED`: Set to `DangerZone!` to disable password
  protection
- `JUPYTER_NOTEBOOK_ARGS`: Дополнительные аргументы командной строки переданы в
  `jupyter notebook`; e.g. получить более подробный журнал, используя `--debug`

## Python version

Если вы хотите использовать специальную версию Python, вы должны установить ее в своем environment.yml:

```
name: root
dependencies:
  - python=2.7
  - ...
```

## Environments

*Экспериментальная функция - в работе*

- Параметризация среды по умолчанию с помощью ENVIRONMENT_YML
- Добавить дополнительное ядро ​​в установку jupyter(Python2 и Python3 в параллели)
- Разрешить изменения и экспериментальные функции без повреждения конфигурации по умолчанию

| Deployment | Features | Description |
| ---------- | -------- | ----------- |
| [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?env[ENVIRONMENT_YML]=environments/default.yml) | Python3, IPython5 | Default Environment
| [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?env[ENVIRONMENT_YML]=environments/latest.yml) | Python3 | Latest, no version binding
| [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?env[ENVIRONMENT_YML]=environments/multi_kernel.yml&env[ADDITIONAL_ENVIRONMENT_YML]=environments/kernel/python2/python2.yml) | Python3, IPython5 + Python2 | Default Environment + Python2
