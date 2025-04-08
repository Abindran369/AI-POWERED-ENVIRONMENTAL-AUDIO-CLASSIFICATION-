from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # Home page with buttons

@app.route("/eda")
def eda():
    return render_template("Project_1.html")  # EDA notebook

@app.route("/feature_extraction")
def feature_extraction():
    return render_template("Project-2.html")  # Feature Extraction notebook

@app.route("/models")
def models():
    return render_template("Project_3.html")  # Models notebook

@app.route("/comparison")
def comparison():
    return render_template("Project_5.html")  # Comparison notebook (changed from comparison.html)

@app.route("/ast_model")
def ast_model():
    return render_template("Project_AST_Model.html")  # New AST Model notebook

@app.route("/visuals")
def visuals():
    return render_template("visuals.html")  # New visualizations page

if __name__ == "__main__":
    app.run(debug=True)