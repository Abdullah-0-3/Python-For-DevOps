from flask import Flask, Response, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def hello():
    return Response({'Hello, Dosto! The Server is Up and Running'}, status=200)

@app.route('/cpu')
def monitor_cpu():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or memory utilization detected!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

if __name__ == '__main__':
    print('Starting Flask server...')
    app.run(debug=True)
