from flask import Flask, jsonify, request, abort
from trainingDAO import trainingDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/training')
def getAll():
    #print("results in getall")
    results = trainingDAO.getAll()
    return jsonify(results)

@app.route('/training/<int:id>')
def findById(id):
    foundtraining = trainingDAO.findByID(id)
    return jsonify(foundtraining)

@app.route('/training', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checks 
    training = {
        "course_name": request.json['course_name'],
        "id": request.json['id'],
        "price": request.json['price'],
    }
    values =(training['course_name'],training['id'],training['price'])
    newId = trainingDAO.create(values)
    training['id'] = newId
    return jsonify(training)

@app.route('/training/<int:id>', methods=['PUT'])
def update(id):
    foundtraining = trainingDAO.findByID(id)
    if not foundtraining:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)
    if 'course_name' in reqJson:
        foundtraining['course_ame'] = reqJson['course_name']
    if 'Course ID' in reqJson:
        foundtraining['id'] = reqJson['id']
    if 'price' in reqJson:
        foundtraining['price'] = reqJson['price']
    values = (foundtraining['course_name'],foundtraining['id'],foundtraining['price'],foundtraining['id'])
    trainingDAO.update(values)
    return jsonify(foundtraining)

@app.route('/training/<int:id>' , methods=['DELETE'])
def delete(id):
    trainingDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__' :
    app.run(debug= True)