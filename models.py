from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define Rule model to store rule strings and their AST representations
class Rule(db.Model):
    __tablename__ = 'rules'  # Define a custom table name if desired

    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)
    ast = db.Column(db.PickleType, nullable=False)  # Storing the AST as a serialized object

    def __repr__(self):
        return f'<Rule id={self.id} rule_string="{self.rule_string}">'


# Optional: Define UserAttribute model for user-related data
class UserAttribute(db.Model):
    __tablename__ = 'user_attributes'  # Define a custom table name if desired

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=True)  # Age can be nullable if not always required
    department = db.Column(db.String(50), nullable=True)  # Department can also be nullable
    salary = db.Column(db.Float, nullable=True)  # Salary can be nullable
    experience = db.Column(db.Float, nullable=True)  # Experience can be nullable

    def __repr__(self):
        return f'<UserAttribute id={self.id} age={self.age} department="{self.department}">'
