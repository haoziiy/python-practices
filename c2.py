# coding=utf-8
from flask import Flask

# 定义一个应用
app = Flask(__name__)

# 装饰器，route作用:路径映射
@app.route('/')
@app.route('/index/')
def index():
    return 'HELLO'

@app.route('/profile/<int:uid>/')
def profile(uid):
    return 'profile:' + str(uid)

if __name__ == '__main__':
    app.run(debug=True) # 开发者模式