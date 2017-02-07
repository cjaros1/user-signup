#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import cgi

def validate_email(email):
    isValidated=False

    return isValidated

def validate_password(password):
    isValidated=False

    return isValidated

def validate_password_confirm(password_confirm,password):
    isValidated=False

    return isValidated

def vailidate_username(username):
    isValidated=False

    return isValidated

def validate_form(username, password,password_confirm,email):
    isValidated=False

    return isValidated

def build_page():
    header="<h2>User Signup</h2>"
    username_input = "<label>Username:</label><input name='username' type='text' ></input>"
    password_input="<label>Password:</label><input type='password' name='password'></input>"
    password_confirm="<label>Confirm Password:</label><input type='password' name='password_confirm'></input>"
    email_input="<label>Email Address (optional)</label><input type='text' name=email></input>"
    submit="<input type='submit'>"
    form="<form method=post>"+username_input +"<br>"+ password_input + "<br>"+password_confirm+"<br>"+email_input+"<br>"+submit+"</form>"
    content=header+form
    return content



class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=build_page()
        self.response.write(content)

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        password_confirm=self.request.get("password_confirm")
        email=self.request.get("email")
        user_error=""
        password_error=""
        password_confirm_error=""
        email_error=""

        vailidate_username(username)
        validate_password(password)
        validate_password_confirm(password_confirm,password)
        validate_form(username, password, password_confirm, email)


        content=build_page()
        self.response.write(content)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
