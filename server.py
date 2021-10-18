from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "server is on"


@app.route("/info", methods=["GET"])
def info():
    my_output = "this server is for BME547"
    return my_output

#@app.route("/hdl/<hdl_value>", methdods=["POST"])
#def hdl_server_analysis(hedl_value):
#   out_put = hdl_analysis(hdl_value)
#   return output

@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello {}".format(input_name)



if __name__ == "__main__":
    app.run()