from flask import Flask, render_template, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualizer')
def run_visualizer():
    subprocess.Popen(['streamlit', 'run', 'visualizations/main_visualizer.py'])
    return redirect('/')

@app.route('/setup_database')
def setup_database():
    subprocess.Popen(['python', 'database/db_setup.py'])
    return "Database setup initiated. Please check the logs."

if __name__ == "__main__":
    app.run(debug=True)
