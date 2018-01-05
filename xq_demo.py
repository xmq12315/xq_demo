from flask import Flask, request, render_template, url_for, session, redirect
from exts import db
from models import User, Question, Anwers
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
method = ['GET', 'POST']


@app.route('/', methods=method)
@app.route('/index/', methods=method)
def hello_world():
    qt = Question.query.all()
    return render_template('index.html', content=qt)


@app.route('/login/', methods=method)
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone and User.password == password).first()
        if user:
            session['username'] = user.name
            return redirect(url_for('hello_world'))
        else:
            return u'用户名或密码错误'


@app.route('/add_anwers/', methods=method[1])
def anwers():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    anwer=Anwers(content=content)
    s_name=session.get('username')
    user=User.query.filter(User.name==s_name).first()
    anwer.author=user
    question=Question.query.filter(Question.id==question_id).first()
    anwer.question=question
    db.session.add(anwer)
    db.session.commit()
    return redirect(url_for('content',question_id=question_id))


@app.route('/logout/')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.route('/quest/', methods=method)
def quest():
    see = session.get('username')
    if not see:
        return redirect(url_for('login'))
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
        print('get')
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
                user = User(name=name, telephone=telephone, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('hello_world'))
            else:
                return u'密码不一致请重新输入'


@app.route('/content/<list_id>', methods=method)
def content(list_id):
    if request.method == 'GET':
        question = Question.query.filter(Question.id == list_id).first()
        print(question.author.name)
        return render_template('content.html', qt=question)


@app.context_processor
def username():
    username = session.get('username')
    username = {'username': username}
    return username


if __name__ == '__main__':
    app.run(debug=True)
