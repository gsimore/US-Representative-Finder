from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def find_representative():
    message = ''
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        if zipcode:
            # TODO: Look up representative by zipcode and return summary
            pass
        else:
            message = "Please enter a zipcode"

    return render_template('find_my_rep.html', message=message)
