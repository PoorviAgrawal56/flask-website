#!/usr/bin/env python
#update-doc-searchindex
from flask_website import app
from flask_website.search import update_documentation_index
with app.test_request_context():
    update_documentation_index()
