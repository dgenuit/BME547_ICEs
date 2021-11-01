from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
db = []

@app.route("/", methods=["GET"])
def status():
    return "server is on"


@app.route("/new_patient", methods=["POST"])
def new_patient():
    in_data = request.get_json()
    error_string, status_code = validate_new_patient_input(in_data)
    if error_string is not True:
        return error_string, status_code
    new_patient= add_db_entry(in_data["name"], in_data["id"], in_data["blood_type"])
    return "Added patient {}".format(new_patient)


#@app.route("/add_test", methods=["POST"])
#def add_tests():
#    in_data = requests.get_json()
#    return "hello"


def add_db_entry(name, id_no, blood_type):
    new_patient = {"name": name, 
                   "id": id_no,
                   "blood_type": blood_type,
                   "tests": []}
    db.append(new_patient)
    return new_patient


def validate_new_patient_input(in_data):
    if type(in_data) is not dict:
        return("The input was not a dictionary")
    expected_keys = {"name": str, "id": int, "blood_type": str, "tests": list}
    for key in expected_keys:
        if key not in in_data:
            return "The Key {} is missing from the input".format(key), 400
        if type(in_data[key]) is expected_keys[key]:
            return "The key {} has the wrong data type".format(key), 400
    return True, 200


def validate_server_input(in_data, expected_keys):
    if type(in_data) is not dict:
        return("The input was not a dictionary")
    for key in expected_keys:
        if key not in in_data:
            return "The Key {} is missing from the input".format(key), 400
        if type(in_data[key]) is expected_keys[key]:
            return "The key {} has the wrong data type".format(key), 400
    return True, 200


#def find_patient(id):
#
#    return patient

#def add_test_result(in_data):
#    patient = find_patient(in_data["id"])
#    patient["tests"].append((in_data["test_name"], in_data["test_data"]))

    
    


if __name__ == "__main__":
    app.run()