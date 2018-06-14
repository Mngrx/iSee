import pyrebase
import os
from time import gmtime, strftime, sleep

config = {
    "apiKey": "AIzaSyCjboFbctXyrNxeSx8Loea4A6EKk2wciAs",
    "authDomain": "isee-52052.firebaseapp.com",
    "databaseURL": "https://isee-52052.firebaseio.com",
    'projectId': "isee-52052",
    "storageBucket": "isee-52052.appspot.com",
    'messagingSenderId': "639057919948"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = 'embarcado@gmail.com'
password = 'lindeza'

user = auth.sign_in_with_email_and_password(email, password)

storage = firebase.storage()

nomeFoto = strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".jpg"
comando = "fswebcam -r 1280x720 --no-banner "+nomeFoto
#chama função para tirar foto
os.system(comando)
#envia foto para firebase
t = storage.child(
    "images/"+nomeFoto).put(nomeFoto, user['idToken']
                                    )


