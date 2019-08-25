from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return """
Awesome Caculator!<br/>
<form action="/caculate" method="POST">
  <input type="text" name="formula" />
  <input type="submit" value="submit" />
</form>
"""

@app.route('/caculate', methods=['POST'])
def caculate():
    result = str(eval(request.values['formula']))
    return f'Answer will be {result}<br/>' + """
Awesome Caculator!<br/>
<form action="/caculate" method="POST">
  <input type="text" name="formula" />
  <input type="submit" value="submit" />
</form>
"""    