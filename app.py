from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///delight.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Delight(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(500),nullable=False)
    message = db.Column(db.String(1000),nullable=False)
    
    
    def __repr__(self) :
        return f"<Delight {self.name}"
    
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
     users = Delight.query.all()
     return render_template('index.html' )
 
@app.route('/submit',methods=['GET','POST'])
def submit():
    name = request.form['name'] 
    email = request.form['email']
    message = request.form['message']
    
    
    new_user = Delight(name=name, email=email , message = message )
    
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/')
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)