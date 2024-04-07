# django-template
- Python version -> `3.10.1`
- Default installed libs and utilities:

| Lib Name          | Used for manage                              | Used for                                   | 
|-------------------|----------------------------------------------|--------------------------------------------|
| poetry            | package version                              | https://python-poetry.org/docs/basic-usage/ |
| python-dotenv     | env variables                                | https://pypi.org/project/python-dotenv/    |
| django            | -                                            | https://www.djangoproject.com/             |
| Faker             | for fake data on the testing env             | https://faker.readthedocs.io/en/master/    |
| pytest            | to generate dynamically testing objects      | https://docs.pytest.org/en/8.0.x/          |
| pytest-factoryboy | to generate dynamically testing objects      | https://pytest-factoryboy.readthedocs.io/  |
| pytest-django     | plugin for pytest with superpowers for django | https://pytest-django.readthedocs.io/      |
| coverage          | to see more detailed reports of tests env    | https://coverage.readthedocs.io/           |

- Steps to configure the project
  1. First config the env variables (specially the PROJECT_NAME var)
  2. Run the bash command to change root config path name (it will do it automatically so just put the first option)
  ```zsh
  chmod +x template_utils.sh # Make file executable
  ./template_utils.sh # Run template util
  ```
  3. Install required libs
  ```zsh
  pip install poetry # Install poetry if you don't have already installed
  poetry install
  ```
  4. Finally, just run the project
  ```zsh
  # You can run it in two ways
  # First, directly with poetry:
  poetry run python manage.py runserver
  # Second, activate the virtualenv and then run inside it
  poetry shell
  python manage.py runserver
  ```
