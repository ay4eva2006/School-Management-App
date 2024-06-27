from school_app import school_app

@school_app.route('/')
@school_app.route('/index')
def index():
    return "Hello, World!"
