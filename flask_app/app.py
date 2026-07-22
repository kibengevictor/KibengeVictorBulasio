from flask import Flask, render_template

#__name__ is a special variable in Python that represents the name of the current module. When a module is run directly, __name__ is set to "__main__". When it is imported, __name__ is set to the module's name. This allows Flask to know whether to run the application or not.
app = Flask(__name__)

#decorator maps the URL '/' to the hello() function. When a user visits the root URL of the application, the hello() function will be executed.
@app.route('/')

#function to display text welcome to flask

def hello():
    return '<h1>Welcome to Flask!</h1>'

#route to about page
@app.route('/about')

def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'

#dynamic route to my story to display a story about a user
@app.route('/my-story/<username>')

def my_story(username):
    return f'<h1>{username}\'s Story</h1><p>This is the story of {username}\'s life.</p>'

#dynamic route for profile basing on name and id
@app.route('/profile/<username>/<user_id>')

def profile(username, user_id):
    #data passed from python to template
    return render_template('profile.html', username=username, user_id=user_id)


#route to contact page
@app.route('/contact')

def contact():
    return '<h1>Contact Page</h1><p>You can contact me at john@example.com</p>'


#ensures that the Flask application runs only when the script is executed directly, not when it is imported as a module in another script. This is a common practice in Python to allow code to be reusable and modular.
if __name__ == '__main__':
    app.run(debug=True)  #debug=True enables debug mode, which provides detailed error messages and automatically reloads the server when code changes are detected. This is useful during development but should be turned off in production for security reasons.