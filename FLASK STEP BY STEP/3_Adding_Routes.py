# Making Responses
# A function that returns web response is called a view

# Response is a string
# Usually, a string of HTML
# So, our function returns an HTML string:
# On requesting http://localhost:5000/hello in browser, function is called:
# Flask lets you “route” a URL to a function
# @app.route('/hello') is a Python “decorator”
# “/hello” in the decorator maps directly to the URL the user requested
# Now we can get to this at http://localhost:5000/hello

@app.route('/hello')## listen for a request to /hello
def say_hello():##when that happens call this function
    """Return simple "Hello" Greeting."""

    html = "<html><body><h1>Hello</h1></body></html>"
    return html

