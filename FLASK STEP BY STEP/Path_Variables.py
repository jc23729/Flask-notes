USERS = {
  "whiskey": "Whiskey The Dog",
  "spike": "Spike The Porcupine",
}  

@app.route('/user/<username>')
def show_user_profile(username):
    """Show user profile for user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"