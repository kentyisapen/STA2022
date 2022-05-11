from asyncore import file_dispatcher
from flask import Flask, render_template, request
from sympy import sieve
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', message="電卓(自然数と加減乗除のみ)")


@app.route('/result', methods=["GET"])
def result_get():
    field = request.args.get("field", "")
    pat = r'(([1-9]\d*)(\+|\*|\-|\/))+([1-9]\d*)'
    hantei = re.fullmatch(pat, field)
    if hantei == None:
        mes = "計算不可能だよ！！！（もしくは悪意のあるコードかな？）"
    else:
        mes = eval(field)  # 正規表現フィルタしたとはいえ、セキュリティ学科にあるまじき行為
    return render_template('result.html', message="{} の計算結果は、{}".format(field, mes))


if __name__ == '__main__':
    app.run()
