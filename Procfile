web: gunicorn runp-heroku:bergruz
init: python db_create.py && pybabel compile -d bergruz/translations
upgrade: python db_upgrade.py && pybabel compile -d bergruz/translations