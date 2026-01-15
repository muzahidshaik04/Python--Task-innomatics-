from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    matches = []
    error = None
    test_string = ""
    pattern = ""

    if request.method == "POST":
        test_string = request.form.get("test_string")
        pattern = request.form.get("pattern")

        try:
            matches = re.findall(pattern, test_string)
        except re.error as e:
            error = str(e)

    return render_template(
        "index.html",
        matches=matches,
        error=error,
        test_string=test_string,
        pattern=pattern
    )

if __name__ == "__main__":
    app.run(debug=True)
