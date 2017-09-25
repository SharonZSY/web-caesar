from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rotate_form = """
<!DOCTYPE html>

<html>
    <head>

        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>  
        <form method = "post">
            <div>
                <label for = "rot">Rotate by:</label>
                <input type = "text" name = "rot" value = "0" />
            </div>
            <textarea type = "text" name = "text">
            </textarea>
            <input type = "submit" value = "Submit Query"/>
        </form>

    </body>
</html>

"""
@app.route("/")
def index():
    return rotate_form

@app.route("/", methods=['POST'])
def encrypt():
    encrypt_rot = int(request.form['rot'])
    encrypt_text = str(request.form['text'])
    content = '{0}'.format(rotate_string(encrypt_text, encrypt_rot))

    return content

app.run()