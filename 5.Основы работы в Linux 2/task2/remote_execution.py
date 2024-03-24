import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=0, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    cmd = f'prlimit --nproc=1:1 python -c "{code}"'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    try:
        outputs, errors = proc.communicate(timeout=timeout)
        return f"Результат: {outputs.decode()}"
    except subprocess.TimeoutExpired:
        proc.kill()
        return "Исполнение кода не уложилось в данное время"


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        result = run_python_code_in_subproccess(code, timeout)
        return result
    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)