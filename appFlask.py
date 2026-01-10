from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Flask Task 1</h2>
    <p>Use URL like:</p>
    <p><b>/name?user=yourname</b></p>
    """

@app.route("/name")
def show_name():
    user_name = request.args.get("user")

    if not user_name:
        return "<h3>Please provide a name using ?user=YourName</h3>"

    upper_name = user_name.upper()
    length = len(user_name)
    reversed_name = user_name[::-1]

    return f"""
    <h2>Flask Output</h2>
    <p><b>Original Name:</b> {user_name}</p>
    <p><b>Upper Case:</b> {upper_name}</p>
    <p><b>Length:</b> {length}</p>
    <p><b>Reversed:</b> {reversed_name}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)