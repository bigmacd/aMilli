# Python, AWS Lambda, Cron, Gmail

## A quick and easy primer on running some python code on AWS Lambda on a Cron schedule

### First Setup the Virtual Environment
```bash
python -m venv env
```

### And Activate it
```bash
bin/env/activate
```

### Add all the necessary modules
```bash
pip install <module> -t ./
```

### Capture the python environment
```bash
pip freeze > requirements.txt
```

### Capture the whole environment
```bash
pip install -r requirements -t ./
```

### Zip everything up (MAC version)
```bash
zip -r aMilli.zip * -x env/\* -x bin/\* -x __pycache__/\* -x "*.vscode*" "*.git*"
```
This command excludes the venv's env and bin directories, any pycache directories, IDE and git directories.  You may have others you wish to exclude.


### Upload the zip file using the AWS Lambda Console

![Upload Zip](https://i.imgur.com/FrzgzLg.png)
Notice the Handler is set to the main function in the powerball.py file.

### Add the Environment Variables (for sending via your Gmail Account)

![Add Environment Variables](https://i.imgur.com/4Q0wbJU.png)
Of course, this image does not reveal the actual data.  You will see the reference to these environment variables in the powerball.py code.  They are passed to the Gmail code for sending the email.

### Set up the Cron action by adding a Cloudwatch Trigger

![Cloudwatch Trigger](https://i.imgur.com/88h69dF.png)
Powerball numbers are picked on Wednesday and Saturday evenings.  So we wait a little while (until Thursday and Sunday) to scrap the numbers from a web-site.

