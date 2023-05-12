import cgi, html
r = cgi.FieldStorage()
title = 'Форма авторизации'
form = True
login = html.escape(r.getvalue('login', ''))
password = html.escape(r.getvalue('password', ''))

message = '<br>'
print(login, password)
if login.lower() == 'admin' and password == '123':
    form = False
    title = message = 'Здравствуйте, Admin!'
elif login != '' or password != '':
    message = 'Неверные логин и/или пароль'

print('Content-type: text/html; charset=utf-8')
print()
print('<html><head><title>'+title+'</title></head><body style="text-align: center;">')
print('<h1>Форма авторизации</h1>')
if form:
    print('''
<form name="form" style="margin: 0 auto;" action="/cgi-bin/reg.py" method="post">
    <h2>Авторизация</h2>
    <h3 style="color: red">''' + message +
    '''</h3>
    <label>Логин:</label>
    <input type="text" name="login" />
    <br />
    <br />
    <label>Пароль:</label>
    <input type="password" name="password" />
    <br />
    <br />
    <input type="submit" value="Войти" />
</form>''')
else:
    print('<h2>'+message+'</h2>')
print('</body></html>')