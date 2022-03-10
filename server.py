from flask import Flask
from flask import request
from flask import Response

def define_routes(app):
    
    @app.route('/test/<id>')
    def index(id):
        assert request.view_args['id'] == id
        return "Hello %s" % id

    @app.route('/post', methods = ['POST', 'GET'])
    def post_method():
        # if request.method == 'POST'...

        # returning 200
        return '', 200

    @app.route('/test', methods = ['GET'])
    def test_method():
        return ('the_response_text', 404, {
            'header1': 123,
            'header2': "hey"
        })

def main():
    app = Flask(__name__)
    define_routes(app)
    app.run(host="0.0.0.0", port = 8080)

if __name__ == '__main__':
    main()

