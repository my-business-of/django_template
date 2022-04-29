# django-template
- Python version -> `3.10.1`
- Default installed libs and utilities:

| Lib Name      | Used for manage  | Used for                                | 
|---------------|------------------|-----------------------------------------|
| pipenv        | package versions | https://pypi.org/project/pipenv/        |
| python-dotenv | env variables    | https://pypi.org/project/python-dotenv/ |
| django        | -                | -                                       |

- Steps to configure the project
  1. First config the env variables (specially the PROJECT_NAME var)
  2. Run the bash command to change root config path name (it will do it automatically so just put the first option)
  ```zsh
  chmod +x template_utils.sh # Make file executable
  ./template_utils.sh # Run template util
  ```
  3. Install required libs
  ```zsh
  python -m venv venv # Create virtual env
  source venv/bin/activate # Activate virtual env
  pip install pipenv # Install package manager
  pipenv install # Install all dependencies
  ```
  4. Finally, just run the project
  ```zsh
  python manage.py runserver
  ```
