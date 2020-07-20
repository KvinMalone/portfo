from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)  # name of the flask app is main


# decorator is used to define a function any time it hits  '/'
@app.route('/')
def homepage():
    return render_template('index.html')


# in order to debug, we need to set the flask_envE= development

# when it sees in the url has a '/blog' in it, it will route it to The function blog()
# @app.route('/blog')
# def blog():
#    return 'This is a blog'

# single function to render pages based on the url name using params
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# to be called when people submit information on contact me form
# to caputre the data on contact form in a dict
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
       try:
        data = request.form.to_dict()
        write_to_csv(data)
        return 'form submitted'
       except:
           return 'kuch toh gadbad hai'
    else:
        return 'something went wrong try again later!'


# to capture and store data from dict to a txt file
def write_to_file(data):
    with open("database.txt", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


# to store data in an excel file using csv module
def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])

# we can render html pages based on the route this is like the sml mapping in jenkis/red hat
# to do that we need to import render_templates
# place the html files in a folder called templates
# @app.route('/works.html')
# def works():
#    return render_template('works.html')

# @app.route('/work.html')
# def project_work():
#    return render_template('work.html')


# in order to add css or js files, they need to be in a static folder

# @app.route('/about.html')
# def about():
#    return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#    return render_template('contact.html')

# @app.route('/components.html')
# def components():
#    return render_template('components.html')
