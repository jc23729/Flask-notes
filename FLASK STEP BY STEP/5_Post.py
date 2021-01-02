"""Handling POST Requests
By default, a route only responds to GET requests

To accept POST requests, must specify that:"""

@app.route("/my/route", methods=["POST"])
def handle_post_to_my_route():
   ...

#Example Post request but this also shows how to return a form with input 
## the first part will be to extract data 
@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <form method="POST">
        <input name="comment">
        <button>Submit</button>
      </form>
      """
##this 

app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""

    comment = request.form["comment"]

    # TODO: save that into a database!

    return f'<h1>Received "{comment}".</h1>'