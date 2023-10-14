from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/services')
def services():
  return render_template('services.html')


@app.route('/request_quote')
def request_quote():
  return render_template('request_quote.html')


@app.route('/about_us')
def about_us():
  return render_template('about_us.html')


@app.route('/testimonials')
def testimonials():
  return render_template('testimonials.html')


@app.route('/contact_us')
def contact_us():
  return render_template('contact_us.html')


# Dummy data to simulate form submission
quotes = []


@app.route('/')
def index():
  return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
  # Get form data
  name = request.form['name']
  email = request.form['email']
  phone = request.form['phone']
  moving_date = request.form['moving_date']
  origin = request.form['origin']
  destination = request.form['destination']
  special_requests = request.form['special_requests']

  # Server-side validation
  email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  phone_pattern = r'^\d{10}$'
  errors = []

  if not name:
    errors.append('Name is required')
  if not re.match(email_pattern, email):
    errors.append('Invalid email format')
  if not re.match(phone_pattern, phone):
    errors.append('Invalid phone number format')
  if not moving_date:
    errors.append('Moving date is required')

  if errors:
    return render_template('home.html', errors=errors)
  else:
    # Store the data or send it to your backend
    quotes.append({
        'name': name,
        'email': email,
        'phone': phone,
        'moving_date': moving_date,
        'origin': origin,
        'destination': destination,
        'special_requests': special_requests
    })
    return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
  return render_template('thank_you.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
