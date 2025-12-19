from flask import Flask,jsonify,request

app = Flask(__name__)

## Dataset 
items = [
    {"id":1,"name": "Item 1", "description": " This is item 1"},
    {"id":2,"name": "Item 2", "description": " This is item 2"}
]

'''
 - GET request
 - http://127.0.0.1:5000/items/1
'''
@app.route('/items/<int:item_id>',methods=['GET'])
def find_item_by_id(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None: 
        return jsonify({"error":"item not found"})
    return jsonify(item)


@app.route('/items',methods=['GET'])
def find_all():
    return jsonify(items)


'''
 -  POST request (Create a new resource)
 - http://127.0.0.1:5000/add 
 - request body = 
 {
    "name" : "apple",
    "description" : "apple watch"
 }

 - items[-1][ = get the last item from items[]
 -  "id": items[-1]["id"] + 1 if items else 1 = if items is not empty, use incremental id, if items is empty start with id = 1
 - "name":request.json['name'] = take the name from json request
 - "description":request.json['description'] = take the description from json request

'''
@app.route('/add',methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json: # Request cannot be null, Request has to have 'name' field.
        return jsonify({"error": "no request body or name is missing from request body"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item) # Add item to the hardcoded Dataset
    return jsonify(new_item) # Return in json format the newly added item

'''
 - PUT request (Update a resource)
 - http://127.0.0.1:5000/update/1
 - request body =
 {
    "name" : "samsung",
    "description" : "apple watch"
 }

  - item["name"] = request.json.get('name',item['name']) 
  # Get the name from json request body = (request.json.get('name) and update it to the 'item' dataset, 
  # - if the name does not exist in request body, keep the origional name = item['name]
  


'''
@app.route('/update/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None) # Find the existing item to update
    if item is None:
        return jsonify({"error": "Item not found"})
    item["name"] = request.json.get('name',item['name'])  
    item["description"] = request.json.get('description',item['description'])
    return jsonify(item)


@app.route('/delete/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    item=next((item for item in items if item["id"]==item_id),None) # Find the existing item to update
    if item is None:
        return jsonify({"error": "Item not found"})
    
    items = [item for item in items if item["id"]!=item_id] # Delete operation - Put only those items in the item[] which does not have the request.item_id
    return jsonify({"result": "item deleted"})



if __name__=='__main__':
    app.run(debug=True)
