from flask import Flask, render_template, redirect, url_for
import subprocess
import webbrowser
from threading import Timer
import os

# Initialize Flask application
app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route('/')
def index():
    # Render the index.html page
    print("Hello World")
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    # Render the About Us page
    return render_template('about_us.html')


@app.route('/run_visualizer')
def run_visualizer():
    try:
        os.system('streamlit run visualizations/main_visualizer.py')
        return redirect("http://localhost:8501", code=302)
    except Exception as e:
        return f"Error running visualizer: {e}"


@app.route('/risk_mitigation')
def risk_mitigation():
    try:
        os.system('streamlit run visualizations/risk_mitigation.py')
        return redirect("http://localhost:8502", code=302)
    except Exception as e:
        return f"Error running risk mitigation page: {e}"


def open_browser():
    # Automatically open the index page in the browser
    try:
        webbrowser.open_new("http://localhost:5000/")
    except Exception as e:
        print(f"Error opening browser: {e}")


if __name__ == "__main__":
    Timer(2, open_browser).start()
    app.run(debug=True)