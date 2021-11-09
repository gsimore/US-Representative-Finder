from flask import Flask, render_template, request
from utilities.representative_lookup import lookup_representatives, ZipcodeNotFound, DistrictNotFound

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def find_representative():
    reps = []
    message = ''
    zipcode = None
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        if zipcode:
            try:
                reps = lookup_representatives(zipcode)
            except ZipcodeNotFound:
                message = f"The zipcode {zipcode} could not be found."
            except DistrictNotFound:
                message = f"No district could be found for the zipcode {zipcode}."
        else:
            message = "Please enter a zipcode"

    return render_template('find_my_rep.html', message=message, reps=reps, zipcode=zipcode)


if __name__ == '__main__':
    app.run(debug=True)
