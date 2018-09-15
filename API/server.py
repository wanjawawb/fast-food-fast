from flask import render_template
import connexion

# Application instance
app = connexion.App(__name__, specification_dir='./')

# Read swagger.yml
app.add_api('swagger.yml')

# URL for "/" root
@app.route('/')
def home():
    """
    Rsponds browser URL localhost:5000/

    :return:        "home.html"
    """
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
