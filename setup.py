from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def first_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def portfolio(page_name):
    return render_template(page_name)


def write_to_database(data):
    with open('database.txt', mode='a') as database:
        email = data['e-mail']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data['e-mail']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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


# above is simplified method
# now theres a problem with home.html and index.html
# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')  # what is the link in the browser
# def works():
#     return render_template('works.html')


# @app.route('/about.html')
# def about_me():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# dont need this
# @app.route('/components.html')
# def components():
#   return render_template('components.html')
