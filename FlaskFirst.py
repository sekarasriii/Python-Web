from flask import Flask #Mengimpor class Flask dari library Flask

app = Flask (__name__) #nama flask

@app.route("/") #domain dari route contoh : krs.umy.ac.id/Beranda
def hello_world():
    return "<div>Hello, World!</div"
@app.route('/salam')
def hello():
    return "Assalamualaikum!"

if __name__ == "__main__":
    app.run(debug=True)