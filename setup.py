from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def portfolio(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data['e-mail']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'oooops, please fix it'
