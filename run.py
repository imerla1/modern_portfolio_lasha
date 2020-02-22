from app import create_app
from flask import current_app
app = create_app()
print(app.config['SECRET_KEY'])
app.run(debug=True)
