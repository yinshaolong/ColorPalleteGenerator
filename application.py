from flask import Flask, render_template, request
from responseGenerator import response_gen

application = Flask(__name__,
    template_folder="templates",
    #gives static folder path in index.html link without having to specify it
    static_url_path='',
    static_folder='static'
)


#post method allows users to send data over to the server
@application.route('/palette', methods=['POST'])
def prompt_to_palette():
    # sends the information sent to the server as query
    application.logger.info(request.form.get('query'))
    #saves value of body query to query variable
    query = request.form.get('query')
    colors = response_gen(query)
    application.logger.info(colors)
    return {"colors":colors}
@application.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    application.run(debug=True)
