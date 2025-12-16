# 1) Activate virtual environment
Terminal (/Users/ankur/backup/delta/sn/datascience/workspace/18 - getting started with flask) > conda activate venv/

# 2) Run application
Terminal (/Users/ankur/backup/delta/sn/datascience/workspace/18 - getting started with flask) > python app.py

# 3) Application endpoints

### 3A) Inline HTML  = 
- http://127.0.0.1:5000/inlinehtml
- For URL = /
- This uses inline HTML
- Get request


### 3B) Forwards the request to an existing page
- http://127.0.0.1:5000/forward_request
- For URL = /index
- Uses render_template("index.html") which redirects the control to 'templates/index.html"
- Get request


### 3C) Form Load and Form Submit
- http://127.0.0.1:5000/formLoad
- For URL = /formLoad and /formSubmit
- Get and Post request
- Get to load the reqeust
- Post request when the page is submitted
- Also used Templates to print 'name' from the textfield


### 3D) Parameter passed in the URL
- http://127.0.0.1:5000/variable_in_url/93 
- Parameter in the URL (here = 93)
- Get request


### 3E) Data Binding using Key Value pairs
- http://127.0.0.1:5000/data_binding_key_value_pair/51
- Passing data(in the form of key-value pair) from app.py and used in data_binding_key_value_pair.html
- Get request

### 3F) Data Binding using JSON , For Loop in HTML template
- http://127.0.0.1:5000/data_binding_json/51
- Passing data(in the form of JSON) from app.py and used in data_binding_json.html
- Also shows the use of For Loop in the html template (data_binding_json.html)
- Get request


## 3G) If statement in HTML template  
- http://127.0.0.1:5000/if_in_html_template/51
- If statement in HTML template

## 3H) Redirect to another URL  
- http://127.0.0.1:5000/redirect_to_another_url
- Enter marks of different subjects on the above URL
- When page is submitted, it redirects to 
- URL = http://127.0.0.1:5000/data_binding_json/<average_of_all_subects_value>