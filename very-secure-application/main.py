from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


@app.route('/')
def hello():
    user = request.args.get('user')
    rendered_template = render_template('hello.html', user=user)
    return render_template_string(rendered_template)
