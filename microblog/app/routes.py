from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'Akshit'}
    return '''
<html>
<head>
<title>Home Page-microblog</title>
</head>
<body>
<h1>Hello,'''+user['username']+'''!<h1>
</body>
</html>'''

