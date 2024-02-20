from flask import Flask
from flask import jsonify

# a change to test building
application = Flask(__name__)


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Continuous Delivery Demo when changes are pushed to gh repo using AWS ElasticBeanStalk and CodePipeline :)"

@application.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
