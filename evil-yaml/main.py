from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/')
def hello():
    return """
Awesome YAML validator!<br/>
<textarea rows="4" cols="50" name="yaml" form="validateform"></textarea>
<form action="/validate" id="validateform" method="POST">
  <input type="submit" value="submit" />
</form>
"""

@app.route('/validate', methods=['POST'])
def validate():
    yaml_load = lambda x: yaml.load(x, Loader=yaml.Loader)
    result = yaml_load(request.values['yaml'])
    return f'Your YAML will be compile to: <br/> {result}' + """<br/>
Awesome YAML validator!<br/>
<textarea rows="4" cols="50" name="yaml" form="validateform"></textarea>
<form action="/validate" id="validateform" method="POST">
  <input type="submit" value="submit" />
</form>
"""