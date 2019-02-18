# -*- coding: utf-8 -*-
from An_login import manager,app
from orm import db
import views

# db.drop_all()
# db.create_all()
app.run(debug=True, port=5001)
