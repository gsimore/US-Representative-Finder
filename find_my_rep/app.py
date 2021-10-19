from flask import Flask, render_template, request
from utilities.representative_lookup import lookup_representatives
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def find_representative():
    reps = []
    message = ''
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        if zipcode:
            reps = lookup_representatives(zipcode)
        else:
            message = "Please enter a zipcode"

    return render_template('find_my_rep.html', message=message, reps=reps)


if __name__ == '__main__':
    app.run(debug=True)
