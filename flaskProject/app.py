from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    # 返回网页文件
    # return 'Hello World Flask!'
    return render_template('index.html')


from data import *


@app.route('/login', methods=['POST'])
def hello_login():
    # 登录到服务器  获取用户名 然后进行校验 在记录信息 再返回后台页面

    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    # 登录成功后返回后台界面
    return render_template('admin.html', salary_list=salary_list)


@app.route('/delete/<name>/')
def hello_delete(name):
    for salary in salary_list:
        if salary['name'] == name:
            salary_list.remove(salary)
    return render_template('admin.html', salary_list=salary_list)

# @app.route('/delete/<name>/')
# def hello_delete(name):
#     for salary in salary_list:
#         if salary['name'] == name:
#             salary_list.remove(salary)
#     return render_template('admin.html', salary_list=salary_list)


if __name__ == '__main__':
    app.run(debug=True)
