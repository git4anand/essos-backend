from flask import Flask
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def event_handler():
    import subprocess
    subprocess.call(['./start_server.sh'])
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
