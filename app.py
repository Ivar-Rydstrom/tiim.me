from flask import Flask, render_template, url_for, make_response, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set')
def setCookie():
    response = make_response('set cookie')
    response.set_cookie('framework', 'flask')
    return response


@app.route('/get')
def getCookie():
    framework = request.cookies.get('framework')
    return 'framework: ' + framework




if __name__ == '__main__':
    app.run(debug=True)
