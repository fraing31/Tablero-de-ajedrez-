from flask import Flask, render_template

app = Flask( __name__ )


@app.route('/', methods=['GET'])
def chess():

    return render_template( "box.html" ) 

@app.route('/<int:num>', methods=['GET'])
def playDiv( num ):

    return render_template( "number.html", num=num )

@app.route('/<int:x>/<int:y>', methods=['GET'])
def playChess( x, y):

    return render_template( "index.html", x=x, y=y )

if __name__ == "__main__":
    app.run( debug=True )