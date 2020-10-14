
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blog import mail

def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, iext = os.path.splitext(form_image.filename)
    image_fn = random_hex + iext
    image_path = os.path.join(current_app.root_path, 'static/profiles', image_fn)
    output_image_size = (150, 150)
    image = Image.open(form_image)
    image.thumbnail(output_image_size)
    image.save(image_path)
    return image_fn

def send_reset_password_email(user):
    token = user.generate_reset_token()
    message = Message(
        'Reset Password Request', 
        sender='ebrahimrahimilaziri@gmail.com', 
        recipients=[user.email]
    )
    message.body = f'''Visit bellow link to reset your password:
{url_for('user.reset_token', token=token, _external=True)}.
If you did not request for a password reset leave it as it is, nothing will change. 
    '''
    mail.send(message)

