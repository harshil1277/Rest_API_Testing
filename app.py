from flask import Flask, render_template, request, url_for
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    toolname = request.form.get("toolname")
    servicename = request.form.get("servicename")

    # Construct the absolute path to the generate_csv_and_graph.py script
    script_path = os.path.join(os.path.dirname(__file__), "run_integrate.py")

    # Run the Python script with arguments
    try:
        subprocess.run(["python3", script_path, toolname, servicename], check=True)
    except subprocess.CalledProcessError as e:
        print("Error running the script:", e)

    # Path to the generated graph image
    graph_url = "static/output_graph.png"
    
    # Return the index template with the graph URL
    return render_template("index.html", graph_url=graph_url)

if __name__ == "__main__":
    app.run(debug=True)

