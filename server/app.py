from flask import Flask, make_response, jsonify, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return make_response(
        '<h1>Welcome to the Flask web application!</h1>',
        200
    )

@app.route('/article/<int:article_id>')
def get_article(article_id):
    page_views = session.get('page_views', 0)  # Default value is set to 0 if 'page_views' key is not found

    if page_views <= 3:
        session['page_views'] = page_views + 1
        article_json = {
            'title': 'Sample Article',
            'content': 'This is a sample article for demonstration purposes.'
        }
        return article_json, 200
    else:
        return make_response(
            jsonify({
                'message': 'Maximum pageview limit reached'
            }),
            401
        )

if __name__ == '__main__':
    app.run(debug=True)