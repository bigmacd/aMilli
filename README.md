python -m venv env
bin/env/activate
pip install <module> -t ./
pip freeze > requirements.txt


zip -r aMilli.zip * -x env/\* -x bin/\* -x __pycache__/\* -x "*.vscode*"


pip install -r requirements -t ./


