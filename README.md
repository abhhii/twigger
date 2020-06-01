# twigger
Twitter clone in django

Quickly checkout the app at this link:
https://twiggerapp.herokuapp.com/

Profile pics are not shown at heroku since heroku deletes any extra files added by the users

To see this app in action
1) Clone this repo\s\s
2) Open terminal in the project directory  
3) We need to set some environment variables:  
  a) for linux and mac users:  
    open ~/.bashrc or ~/.bash_profile and add these lines  
    export EMAIL_PASS="<Your email app password from google>"  
    export EMAIL_USER="your email account"  
    export SECRET_KEY="<generate your secret key>"  
    export DEBUG_VALUE="True"  
  b)See the section for secret keys for instructions to build secret keys  
4) Run this command   
pip install -r requirements.txt  
5) Now run  
python manage.py runserver  
6) Click the link in the output or navigate to localhost:8000 to find the app running  

### How to build secret keys  
#### For Linux and Mac  
1) Open python interactive shell  
2) type the following  
import secrets  
secrets.token_hex(30)  
3) Copy the output and use it as secret key in environment variables  
