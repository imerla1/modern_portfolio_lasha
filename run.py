from app import create_app
from flask import current_app
app = create_app()

app.run(debug=True)
