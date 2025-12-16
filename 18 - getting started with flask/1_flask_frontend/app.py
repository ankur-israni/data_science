#render_template is used to redirect to another page.
from flask import Flask,render_template, request,redirect,url_for

app = Flask(__name__)

## 3A) -------- Inline HTML  -------- 
# http://127.0.0.1:5000/inlinehtml
# This method has inline HTML
# GET request
@app.route("/inlinehtml")
def inlinehtml():
        return "<html><h1>3A - This page uses inline html in app.py</h1></html>"

## 3B) -------- Forward to an existing page -------- 
# http://127.0.0.1:5000/forward_request
# This method forwars the request to an existing HTML page
# render_template("index.html") will redirect to 'templates/index.html"
# GET request (default when not specified)
@app.route("/forward_request",methods=['GET'])
def forward():
        return  render_template("forward_request.html")

## 3C) -------- Form Load and Form Submit -------- 
# Get request
# http://127.0.0.1:5000/formLoad
@app.route("/formLoad",methods=['GET','POST'])
def formLoad():
        if request.method=='GET':
            return  render_template("form_load_and_submit.html") # On Page Load

# Post request
@app.route("/formSubmit",methods=['GET','POST'])
def formSubmit():
        if request.method=='POST': # Triggered when the page is Submitted (i.e. Submit button pressed on form.html)
            name = request.form['name'] # Get the value in 'name' textfield
            return f'Hello {name}' # Templating
        return  render_template("form_load_and_submit.html") # Triggered when the page is loaded


## 3D -------- Parameter in URL  -------- 
# Get reqeust
# http://127.0.0.1:5000/variable_in_url/93 
# <score> is the parameter
# <score> has to be of type 'int' otherwise it will give a typecasting error
@app.route("/parameter_in_url/<int:score>")
def variable_in_url(score):
        return "<h2>3D - The marks you scored are are: </h2>"+str(score)


## 3E -------- Data Binding using Key Value Pair-------- 
# Get request
# http://127.0.0.1:5000/data_binding_key_value_pair/51
@app.route("/data_binding_key_value_pair/<int:score>")
def data_binding_key_value_pair(score):
        exam_results_value=""
        if score>=40:
                exam_results_value="PASSED"
        else: 
                exam_results_value="FAILED"
        return render_template("data_binding_key_value_pair.html",exam_results_key=exam_results_value)


## 3F -------- Data Binding using JSON and For Loop in HTML template-------- 
# Get request
# score = e.g. 51 = what you pass in the URL
# exam_results = PASSED / FAILED
# final_result_in_json = combination of (1) score and (2) exam_results
# http://127.0.0.1:5000/data_binding_json/51
@app.route("/data_binding_json/<int:score>")
def data_binding_json(score):
        exam_results_value=""
        if score>=40:
                exam_results="PASSED"
        else: 
                exam_results="FAILED"

        json_exam_results_value = {"score":score,"exam_results":exam_results}      

        # 'json_exam_results_key' is stored as a Dictionary and can be retrieved using 'json_exam_results_key.items()' in 'data_binding_json.html' 
        return render_template("data_binding_json.html",json_exam_results_key=json_exam_results_value)

## 3G -------- if statement in HTML template -------- 
# Get request
# score = e.g. 51 = what you pass in the URL
# exam_results = PASSED / FAILED
# final_result_in_json = combination of (1) score and (2) exam_results
# http://127.0.0.1:5000/if_in_html_template/51
@app.route("/if_in_html_template/<int:score>")
def if_in_html_template(score):
        return render_template("if_statement_in_template.html",results=score)


## 3H -------- Redirect to another URL -------- 
# Get and Post request
# Page Load (GET) = http://127.0.0.1:5000/redirect_to_another_url
# Page Submit (POST) = http://127.0.0.1:5000/redirect_to_another_url
#   - Redirected to URL = http://127.0.0.1:5000/data_binding_json/<average_of_all_subjects_value>
@app.route("/redirect_to_another_url",methods=['POST','GET'])
def redirect_to_another_url():
        if request.method=='POST':
                average_score_of_all_subjects_key = 0
                science=float(request.form['science']) # Read from 'science' text field from 
                maths=float(request.form['maths']) # Read from 'maths' text field from 
                arts=float(request.form['arts']) # Read from 'arts' text field from 
                data_science=float(request.form['data_science']) # Read from 'science' text field from 

                average_score_of_all_subjects_value = (science+maths+data_science+arts)/4

                # This makes a call to URL = http://127.0.0.1:5000/data_binding_json/<average_score_of_all_subjects_value>
                return redirect(url_for('data_binding_json',score=average_score_of_all_subjects_value))
        elif request.method=='GET':
                return render_template("redirect_to_another_url.html")
 

if __name__=="__main__":
    app.run(debug=True)