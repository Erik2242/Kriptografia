from crypto import Crypto
import json

f = open('config.json')
config = json.load(f)
GENERATING_ALGORITHM = config['number_generating']
KEY = config['key']

crypto = Crypto(GENERATING_ALGORITHM, KEY)

msg1 = "Alma a fa alatt nyari piros alma 123"
enc1 = crypto.encrypt(msg1)
if crypto.decrypt(enc1) == msg1:
    print("The encryption and decryption were correct")

msg1 = "ojeanf919@**##*@  (F? F"
enc1 = crypto.encrypt(msg1)
if crypto.decrypt(enc1) == msg1:
    print("The encryption and decryption were correct")

msg1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce in urna eu ligula viverra accumsan. Sed eget sem magna. Aliquam bibendum auctor ipsum eget feugiat. Proin condimentum, risus ut pharetra tempor, ex"
enc1 = crypto.encrypt(msg1)
if crypto.decrypt(enc1) == msg1:
    print("The encryption and decryption were correct")