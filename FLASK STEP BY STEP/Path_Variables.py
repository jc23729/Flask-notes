

## we can have access to that value of that variable 
## so you want to wrap it in <...> brackets that turns it into a variable

USERS = {
  "whiskey": "Whiskey The Dog",
  "spike": "Spike The Porcupine",
}  

@app.route('/user/<username>')## <username> is turned into a variable because its wrapped in brackets. 
def show_user_profile(username):
    """Show user profile for user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"

## THIS WOULD GET AN ERROR
@app.route('/r/subreddit')
def show_subreddit():
  return "THIS IS A SUBREDDIT"

## THIS WOULD WORK, BECAUSE IT MATCHES THE PATTERN
##whatever your  variable name is in that path you have to have matching parameter for flask view function
@app.route('/r/subreddit')
def show_subreddit(subreddit):# you would have to pass subreddit variable name, or whatever you put in on top for it to work
  return "THIS IS A SUBREDDIT"

## same pattern same idea
POSTS = {
  1: "I like chicken tenders",
  2: "I hate mayo!",
  3: "Double rainbow all the way",
  4: "YOLO OMG (kill me)"
}

@app.route('/posts/<id>')
def find_post(id):
  post = POSTS[id]
  return f"<p>{post}</>"