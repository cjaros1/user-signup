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
import re
import cgi

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

email_error=""
username_error=""
password_error=""
password_confirm_error=""


def validate_email(email):
    valid_email=False
    valid_email= not email or EMAIL_RE.match(email)
    return valid_email

def validate_password(password, password_confirm):
    valid_password=False
    valid_password= password and password_confirm and password == password_confirm and PASS_RE.match(password)
    return valid_password


def vailidate_username(username):
    valid_username=False
    valid_username= username and USER_RE.match(username)
    return valid_username

def set_email_error(email):
    global email_error
    if not email:
        return
    elif not EMAIL_RE.match(email):
        email_error="Error: That is not a valid email. (example: john@aol.com)"
    else:
        email_error=""
    return

def set_password_error(password):
    global password_error
    if not password:
        password_error="Error: Please enter a password (3-20 characters)"
    elif not PASS_RE.match(password):
        password_error="Error: That is not a valid password. Password must be 3-20 characters."
    else:
        password_error=""
    return

def set_password_confirm_error(password,password_confirm):
    global password_confirm_error
    if not password_confirm:
        password_confirm_error="Error: Please confirm your password"
        return
    elif password_confirm != password:
        password_confirm_error="Error: Passwords do not match."
    else:
        password_confirm_error=""
    return

def set_username_error(username):
    global username_error
    if not username:
        username_error="Error: Please enter a username (3-20 alphanumeric characters)"
    elif not USER_RE.match(username):
        username_error="Error: That is not a valid username. Username must be 3-20 alphanumeric characters."
    else:
        username_error=""
    return

def get_username_error():
    return username_error

def get_email_error():
    return email_error

def get_password_error():
    return password_error

def get_password_confirm_error():
    return password_confirm_error

def build_signup_page(email_error,password_error,password_confirm_error,username_error):
    style="<style> label.error{ color: red } </style>"
    header="<h2>User Signup</h2>"
    username_input = "<label>Username:</label><input name='username' type='text' ></input><label class='error'><strong> "+get_username_error()+"</strong></label>"
    password_input="<label>Password:</label><input type='password' name='password'></input><label class='error'><strong> "+get_password_error()+"</strong></label>"
    password_confirm_input="<label>Confirm Password:</label><input type='password' name='password_confirm'></input><label class='error'><strong> "+get_password_confirm_error()+"</strong></label>"
    email_input="<label>Email Address (optional)</label><input type='text' name=email></input><label class='error'><strong> "+get_email_error()+"</strong></label>"
    submit="<input type='submit'>"
    form="<form method=post>"+username_input +"<br>"+ password_input + "<br>"+password_confirm_input+"<br>"+email_input+"<br>"+submit+"</form>"
    content=style+header+form
    return content

def build_welcome_page(username,email):
    header="<h2>Welcome <em>"+username+"</em></h2>"
    email_header=""
    if email:
        email_header="<p>Your email address: <em>"+email+"</em> has been registered."
    content=header+email_header
    return content

class MainHandler(webapp2.RequestHandler):



    def get(self):
        content=build_signup_page("","","","")
        self.response.write(content)

    def post(self):
        username=self.request.get("username")
        password=self.request.get("password")
        password_confirm=self.request.get("password_confirm")
        email=self.request.get("email")


        if vailidate_username(username) and validate_password(password,password_confirm) and validate_email(email):
            content=build_welcome_page(username,email)
            self.response.write(content)
        else:
            set_username_error(username)
            set_email_error(email)
            set_password_error(password)
            set_password_confirm_error(password,password_confirm)
            username_error=get_username_error()
            password_error=get_password_error
            password_confirm_error=get_password_confirm_error
            email_error=get_email_error
            content=build_signup_page(email_error,password_error,password_confirm_error,username_error)
            self.response.write(content)




app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
