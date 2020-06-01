# twigger
Twitter clone in django

To see this app in action
1) Clone this repo\s\s
2) Open terminal in the project directory\s\s
3) We need to set some environment variables:\s\s
  a) for linux and mac users:\s\s
    open ~/.bashrc or ~/.bash_profile and add these lines\s\s
    export EMAIL_PASS="<Your email app password from google>"\s\s
    export EMAIL_USER="your email account"\s\s
    export SECRET_KEY="<generate your secret key>"\s\s
    export DEBUG_VALUE="True"\s\s
  b)See the section for secret keys for instructions to build secret keys\s\s
4) Run this command \s\s
pip install -r requirements.txt \s\s
5) Now run \s\s
python manage.py runserver\s\s
6) Click the link in the output or navigate to localhost:8000 to find the app running\s\s
\s\s
### How to build secret keys\s\s
#### For Linux and Mac\s\s
1) Open python interactive shell\s\s
2) type the following \s\s
import secrets\s\s
secrets.token_hex(30)\s\s
3) Copy the output and use it as secret key in environment variables\s\s
