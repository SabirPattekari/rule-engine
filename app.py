from flask import Flask, request, jsonify, render_template
from models import db, Rule
from ast_utils import parse_rule, evaluate_node
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids unnecessary warnings
db.init_app(app)

# Ensure database exists
with app.app_context():
    if not os.path.exists('database.db'):
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule():
    # Ensure JSON payload is received
    if not request.is_json:
        return jsonify({"error": "Invalid request format. Please send JSON data."}), 415

    data = request.get_json()

    if 'rule_string' not in data:
        return jsonify({"error": "Missing 'rule_string' in request"}), 400

    rule_string = data['rule_string']

    try:
        ast = parse_rule(rule_string)
        new_rule = Rule(rule_string=rule_string, ast=ast)
        db.session.add(new_rule)
        db.session.commit()
        return jsonify({"message": "Rule created successfully!", "rule_id": new_rule.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    # Ensure JSON payload is received
    if not request.is_json:
        return jsonify({"error": "Invalid request format. Please send JSON data."}), 415

    data = request.get_json()

    if 'rule_id' not in data or 'data' not in data:
        return jsonify({"error": "Missing 'rule_id' or 'data' in request"}), 400

    rule_id = data['rule_id']
    user_data = data['data']

    rule = Rule.query.get(rule_id)
    if not rule:
        return jsonify({"message": "Rule not found!"}), 404

    try:
        result = evaluate_node(rule.ast, user_data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
