from flask import Flask, request, render_template, url_for, session, redirect
from exts import db
from models import User, Question, Anwers
import xqdef
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
method = ['GET', 'POST']


@app.route('/', methods=method)
@app.route('/index/', methods=method)
def hello_world():
    qt = Question.query.order_by(db.desc('id')).all()
    return render_template('index.html', content=qt)


@app.route('/login/', methods=method)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        pwd = xqdef.PwdToSha(password)
        user = User.query.filter(User.telephone == telephone , User.password == pwd).first()
        if user:
            session['username'] = user.name
            return redirect(url_for('hello_world'))
        else:
            return render_template('login.html',content='用户名或密码错误')


@app.route('/add_anwers/', methods=['POST'])
def add_anwers():
    s_name = session.get('username')
    if s_name:
        anwer_content = request.form.get('anwer_content')
        question_id = request.form.get('question_id')
        anwer = Anwers(content=anwer_content)
        user = User.query.filter(User.name == s_name).first()
        anwer.author = user
        question = Question.query.filter(Question.id == question_id).first()
        anwer.question = question
        db.session.add(anwer)
        db.session.commit()
        return redirect(url_for('content', list_id=question_id))
    else:
        return render_template('login.html', content='请先登录后在进行评论')


@app.route('/logout/')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.route('/quest/', methods=method)
def quest():
    see = session.get('username')
    if not see:
        return render_template('login.html', content='请先登录后在发布问题')
    else:
        if request.method == 'GET':
            return render_template('question.html')
        else:
            title = request.form.get('q-title')
            content = request.form.get('q-content')
            name_txt = session.get('username')
            userid = User.query.filter(User.name == name_txt).first().id
            question = Question(title=title, content=content, author_id=userid)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('hello_world'))


@app.route('/reg/', methods=method)
def reg():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        name = request.form.get('username')
        telephone = request.form.get('telephone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        userid = User.query.filter(User.telephone == telephone).first()
        if userid:
            return u'手机号已被注册，请更换手机号'
        else:
            if password1 == password2:
                pwd = xqdef.PwdToSha(password1)
                user = User(name=name, telephone=telephone, password=pwd)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('hello_world'))
            else:
                return u'密码不一致请重新输入'


@app.route('/content/<list_id>', methods=method)
def content(list_id):
    if request.method == 'GET':
        question = Question.query.filter(Question.id == list_id).first()
        anwers = Anwers.query.order_by(db.desc('id')).filter(Anwers.question_id == list_id).all()
        return render_template('content.html', qt=question, comment=anwers)


@app.context_processor
def username():
    username = session.get('username')
    username = {'username': username}
    return username


if __name__ == '__main__':
    app.run(host='0.0.0.0')
