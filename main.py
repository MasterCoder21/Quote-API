from flask import Flask, jsonify, render_template
from flask_restful import reqparse
import random
import json

app = Flask("Quote API")

f = open("quotes.json", "r")
lines = f.read()
ai_quotes = json.loads(lines)


@app.route('/quotes/list', methods=['GET'])
def all1():
    return jsonify(ai_quotes), 200


@app.route('/quotes/all', methods=['GET'])
def all2():
    return jsonify(ai_quotes), 200


@app.route('/quotes/list-all', methods=['GET'])
def all3():
    return jsonify(ai_quotes), 200


@app.route('/quotes/count', methods=['GET'])
def count1():
    parser = reqparse.RequestParser()
    parser.add_argument("num")
    params = parser.parse_args()

    if params['num'] == None:
        return_msg = {"message": "Error: missing argument num"}
        return jsonify(return_msg), 400

    count = int(params["num"])

    if count > len(ai_quotes):
        return_msg = {
            "message":
            f"Error: You can't get more quotes than the number in the database itself.  Number of quotes in the database: {len(ai_quotes)}"
        }
        return jsonify(return_msg), 400

    returned_quotes = []

    i = 0

    while i < count:
        random_quote = random.choice(ai_quotes)
        if random_quote in returned_quotes:
            pass
        else:
            returned_quotes.append(random_quote)
            i += 1

    return jsonify(returned_quotes), 200


@app.route('/quotes/count-list', methods=['GET'])
def count2():
    parser = reqparse.RequestParser()
    parser.add_argument("num")
    params = parser.parse_args()

    if params['num'] == None:
        return_msg = {"message": "Error: missing argument num"}
        return jsonify(return_msg), 400

    count = int(params["num"])

    if count > len(ai_quotes):
        return_msg = {
            "message":
            f"Error: You can't get more quotes than the number in the database itself.  Number of quotes in the database: {len(ai_quotes)}"
        }
        return jsonify(return_msg), 400

    returned_quotes = []

    i = 0

    while i < count:
        random_quote = random.choice(ai_quotes)
        if random_quote in returned_quotes:
            pass
        else:
            returned_quotes.append(random_quote)
            i += 1

    return jsonify(returned_quotes), 200


@app.route('/quotes/num-list', methods=['GET'])
def count3():
    parser = reqparse.RequestParser()
    parser.add_argument("num")
    params = parser.parse_args()

    if params['num'] == None:
        return_msg = {"message": "Error: missing argument num"}
        return jsonify(return_msg), 400

    count = int(params["num"])

    if count > len(ai_quotes):
        return_msg = {
            "message":
            f"Error: You can't get more quotes than the number in the database itself.  Number of quotes in the database: {len(ai_quotes)}"
        }
        return jsonify(return_msg), 400

    returned_quotes = []

    i = 0

    while i < count:
        random_quote = random.choice(ai_quotes)
        if random_quote in returned_quotes:
            pass
        else:
            returned_quotes.append(random_quote)
            i += 1

    return jsonify(returned_quotes), 200


@app.route('/quotes/number-list', methods=['GET'])
def count4():
    parser = reqparse.RequestParser()
    parser.add_argument("num")
    params = parser.parse_args()

    if params['num'] == None:
        return_msg = {"message": "Error: missing argument num"}
        return jsonify(return_msg), 400

    count = int(params["num"])

    if count > len(ai_quotes):
        return_msg = {
            "message":
            f"Error: You can't get more quotes than the number in the database itself.  Number of quotes in the database: {len(ai_quotes)}"
        }
        return jsonify(return_msg), 400

    returned_quotes = []

    i = 0

    while i < count:
        random_quote = random.choice(ai_quotes)
        if random_quote in returned_quotes:
            pass
        else:
            returned_quotes.append(random_quote)
            i += 1

    return jsonify(returned_quotes), 200


@app.route('/', methods=['GET'])
def home():
    return render_template("docs.html")


@app.route('/quotes', methods=['GET'])
def get1(id=0):
    if id == 0:
        return random.choice(ai_quotes), 200
    for quote in ai_quotes:
        if (quote["id"] == id):
            return jsonify(quote), 200
    return_msg = {"message": "Quote not found"}
    return jsonify(return_msg), 404


@app.route('/quotes/', methods=['GET'])
def get2(id=0):
    if id == 0:
        return random.choice(ai_quotes), 200
    for quote in ai_quotes:
        if (quote["id"] == id):
            return jsonify(quote), 200
    return_msg = {"message": "Quote not found"}
    return jsonify(return_msg), 404


@app.route('/quotes/<int:id>', methods=['GET'])
def get3(id=0):
    if id == 0:
        return random.choice(ai_quotes), 200
    for quote in ai_quotes:
        if (quote["id"] == id):
            return jsonify(quote), 200
    return_msg = {"message": "Quote not found"}
    return jsonify(return_msg), 404


@app.route('/quotes/add', methods=['GET'])
def post1(id=0):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()

    if params['author'] == None or params['quote'] == None:
        return_msg = {
            "message": "Error: arguments(s) missing: author and/or quote"
        }
        return jsonify(return_msg), 400

    if id == 0:
        last_quote = ai_quotes[len(ai_quotes) - 1]
        last_id = last_quote["id"]
        last_id = int(last_id)
    quote = {
        "id": last_id + 1,
        "author": params["author"],
        "quote": params["quote"]
    }

    ai_quotes.append(quote)
    with open("quotes.json", "w") as f:
        json.dump(ai_quotes, f)

    return jsonify(quote), 201


@app.route('/quotes/post', methods=['GET'])
def post2(id=0):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()

    if params['author'] == None or params['quote'] == None:
        return_msg = {
            "message": "Error: arguments(s) missing: author and/or quote"
        }
        return jsonify(return_msg), 400

    if id == 0:
        last_quote = ai_quotes[len(ai_quotes) - 1]
        last_id = last_quote["id"]
        last_id = int(last_id)
    quote = {
        "id": last_id + 1,
        "author": params["author"],
        "quote": params["quote"]
    }
    ai_quotes.append(quote)
    with open("quotes.json", "w") as f:
        json.dump(ai_quotes, f)

    return jsonify(quote), 201


@app.route('/quotes/update', methods=['GET'])
def put():
    return_msg = {"message": "Error: missing field id"}
    return jsonify(return_msg), 400


@app.route('/quotes/update/<int:id>', methods=['GET'])
def put1(id=None):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    if id == None:
        return_msg = {"message": "Error: missing field id"}
        return jsonify(return_msg), 400
    elif params['author'] == None or params['quote'] == None:
        return_msg = {
            "message": "Error: arguments(s) missing: author and/or quote"
        }
        return jsonify(return_msg), 400
    else:
        for quote in ai_quotes:
            if (id == quote["id"]):
                quote = {
                    "id": id,
                    "author": params["author"],
                    "quote": params["quote"]
                }

                ai_quotes[int(id)] = quote

                with open("quotes.json", "w") as f:
                    json.dump(ai_quotes, f)

                return jsonify(quote), 201


@app.route('/quotes/put/<int:id>', methods=['GET'])
def put2(id=None):
    parser = reqparse.RequestParser()
    parser.add_argument("author")
    parser.add_argument("quote")
    params = parser.parse_args()
    if id == None:
        return_msg = {"message": "Error: missing field id"}
        return jsonify(return_msg), 400
    elif params['author'] == None or params['quote'] == None:
        return_msg = {
            "message": "Error: arguments(s) missing: author and/or quote"
        }
        return jsonify(return_msg), 400
    else:
        for quote in ai_quotes:
            if (id == quote["id"]):
                quote = {
                    "id": id,
                    "author": params["author"],
                    "quote": params["quote"]
                }

                ai_quotes[int(id)] = quote

                with open("quotes.json", "w") as f:
                    json.dump(ai_quotes, f)

                return jsonify(quote), 201


@app.route('/quotes/del', methods=['GET'])
def delete():
    return_msg = {"message": "Error: missing field id"}
    return jsonify(return_msg), 400


@app.route('/quotes/del/<int:id>', methods=['GET'])
def delete1(id=None):
    if id == None:
        return_msg = {"message": "Error: missing field id"}
        return jsonify(return_msg), 400
    else:
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
        with open("quotes.json", "w") as f:
          json.dump(ai_quotes, f)
        return_msg = {"message": f"Quote with id {id} has been deleted."}
        return jsonify(return_msg), 200


@app.route('/quotes/delete/<int:id>', methods=['GET'])
def delete2(id):
    if id == None:
        return_msg = {"message": "Error: missing field id"}
        return jsonify(return_msg), 400
    else:
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
        return_msg = {"message": f"Quote with id {id} has been deleted."}
        return jsonify(return_msg), 200


@app.route('/quotes/remove/<int:id>', methods=['GET'])
def delete3(id):
    if id == None:
        return_msg = {"message": "Error: missing field id"}
        return jsonify(return_msg), 400
    else:
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
        return_msg = {"message": f"Quote with id {id} has been deleted."}
        return jsonify(return_msg), 200


error_404_templates = ['404.html', '404-2.html']


@app.errorhandler(404)
def not_found(e):
    return render_template(random.choice(error_404_templates))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
