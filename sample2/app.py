from flask import Flask, render_template, request
from sympy import sieve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', message="数字を入力してください。")


@app.route('/result', methods=["GET"])
def result_get():
    field = request.args.get("field", "", type=int)
    if field in sieve:
        hantei = "素数です。"
    else:
        hantei = "素数ではありません。"
    return render_template('result.html', message="{}は{}".format(field, hantei))


@app.route('/result', methods=["POST"])
def result_post():
    field = request.form.get("field", type=int)
    if field % 2 == 1:
        hantei = "奇数です。"
    else:
        hantei = "偶数です。"
    return render_template('result.html', message="{}は{}".format(field, hantei))


if __name__ == '__main__':
    app.run()
