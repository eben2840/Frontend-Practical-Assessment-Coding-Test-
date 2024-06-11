import os
from email.message import EmailMessage
import re
import ssl
import smtplib
import csv
import random
import string
import os
import datetime
from urllib import response
# from datetime import datetime
import urllib.request, urllib.parse
from sqlalchemy import func 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct 
from flask import Flask, redirect, render_template, send_file, url_for,request,jsonify,get_flashed_messages, send_from_directory,make_response
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify, send_from_directory
)
from flask_cors import CORS
import json
import time
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import secrets



app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SECRET_KEY'] ="thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'
app.config['UPLOAD_FOLDER'] = 'uploads/pdfs' 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = 'uploads' 


# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

# mailserver=os.environ.get("presto_mail_server")
# mailport=os.environ.get("presto_mail_port")
# mailpassword=os.environ.get("presto_mail_password")

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))






class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    email= db.Column(db.String())
    role= db.Column(db.String())
    unique_code = db.Column(db.String(12)) 
    code= db.Column(db.String())
    phone= db.Column(db.String())
    image_file = db.Column(db.String())
    password = db.Column(db.String())
    confirm_password = db.Column(db.String(128))
    role =db.Column(db.String())
    def __repr__(self):
        return f"Person('{self.id}', {self.name}')"

    
    

    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String())
    cat = db.Column(db.String())
    desc = db.Column(db.String())
    variant = db.Column(db.String())
    price = db.Column(db.String())
    size = db.Column(db.String())
    image_file = db.Column(db.String(255))
    role =db.Column(db.String())
    def __repr__(self):
        return f"User('{self.id}'"
    
 



# @app.route('/weekly-work', methods=['GET'])
# def get_weekly_work():
#     weekly_work = calculate_weekly_work()
#     return jsonify({'weekly_work_hours': weekly_work})

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
# @app.route('/backup_database', methods=['GET'])
# def backup_database():
#     source_db_path = 'test.db'  # Replace with the actual path to your SQLite database file.
#     backup_db_path = 'your_database_backup.db'  # Replace with the desired path for the backup file.

#     try:
#         shutil.copy2(source_db_path, backup_db_path)
#         return jsonify({'message': 'Database backup successful'})
#     except Exception as e:
#         return jsonify({'error': str(e)})



# # Connect to the SQLite database
# conn = sqlite3.connect('test.db')

# # SQL query to select data from your table
# query = "SELECT * FROM Person"

# # Read data into a DataFrame
# df = pd.read_sql_query(query, conn)

# # Close the database connection
# conn.close()

# # Export the data to an Excel file (output.xlsx)
# df.to_excel('output.xlsx', index=False)

# print("Data has been exported to output.xlsx.")


# email_sender = 'pay@prestoghana.com'
 
 
 
# @app.route("/sendsms", methods=["POST"])
# def send_sms():
#     if request.method == "POST":
#         data = [{
#         'name': '',  
#         'sender_id': '',
#         'mesaage': '',
#     }]
#     return jsonify (data)



# @app.route('/send_email', methods=['POST'])
# def send_email():
#     if request.method == 'POST':
#         email_receiver = [request.form['email'],'prestoghana@gmail.com', 'ebenmills200@gmail.com']
        
#         subject = '"Does what i do really matter?"'
#         # html_content = render_template('try.html') 
#         html_content = """
#         <!DOCTYPE html>
# <html>
# <head>
#     <style>
#     @font-face {
#         font-family: 'Plus Jakarta';
#         src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
#              url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
#         font-weight: 100 900; /* Adjust font weights based on available weights */
#         font-style: normal;
#     }

#     body {
#         font-family: 'Plus Jakarta', sans-serif;
#     }
# </style>

# </head>
# <body>
#  <div class="container">
 
    
#             <h4 class="h1 hero-title">Central University Campus Ministry</h4>
#     <p>Hello there!. 
#     <br/> We are grateful for your patience, your data has been retreived successfully.
#     <br/> Have an amazing day.</p>

#     <h1>
#     </div>
# </body>
# </html>
#         """


#         em = EmailMessage()
#         em['From'] = f"Presto Mail <{email_sender}>"
#         em['To'] = email_receiver
#         em['Subject'] = subject
#         em.set_content('')  
#         em.add_alternative(html_content, subtype='html')

#         context = ssl.create_default_context()

#         with smtplib.SMTP_SSL(mailserver, 465, context=context, ) as smtp:
#             smtp.login(email_sender, mailpassword)
#             smtp.sendmail(email_sender, email_receiver, em.as_string())
    
# #         return redirect(url_for('userbase'))
# new=Committee(name=form.name.data, 
#                   description=form.description.data,
#                   )


radio = 'yboateng057@gmail.com'
email_password = 'hsgtqiervnkabcma'
radio_display_name = 'GVS Support Team'

# users_data = [
#     {'email': 'user1@example.com', 'date': '2022-01-01', 'activity': 'Activity 1', 'implementation': 'Implementation 1', 'tag': 'Tag 1', 'challenges': 'Challenges 1', 'future': 'Future 1'},
# ]

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email_receiver = request.form['email']
        subject = 'Welcome to GVSGROUP'
        
        
        
        
        
        # HTML content of the email
        
        # Handle the case where the user object is not found or doesn't have an ID
            # print("Broo you dont have access")
# users = User.query.order_by(User.id.desc()).all()   
        users=User.query.order_by(User.id.desc()).all()
        html_content = render_template('printout.html',users=users)
        
        # return render_template("emailsender.html",users=users)


        # users = Logger.query.order_by(Logger.id.desc()).all()
        # HTML content of the email
        # html_content = render_template('printout.html',users=users)
        # html_content = """
        # <!DOCTYPE html>
        # <html>
        # <head>
        #     <style>
        #     @font-face {
        #         font-family: 'Plus Jakarta';
        #         src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
        #              url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
        #         font-weight: 100 900; /* Adjust font weights based on available weights */
        #         font-style: normal;
        #     }

        #     body {
        #         font-family: 'Plus Jakarta', sans-serif;
        #     }
        #     </style>
        # </head>
        # <body>
        #         <div class="container">
        #             <div style="display:flex; padding:10px; justify-content:space-between;">
        #                 AbiTrack  🚀
        #                   </div>
        #              <h3 style="text-align:center; font-size:40px;">Welcome to AbiTrack Management System
                   
        #         </h3>      
        #             <img src="https://abitu-ce1b6c8eb118.herokuapp.com/static/asets/images/portfolio/Portfolio.jpg" style="width:100%;">
                          
               
                
                
                
              

               
        #     </div>
            
            
        # </body>
        # </html>
        # """

    
        em = EmailMessage()
        em['From'] = f'{radio_display_name} <{radio}>'
        # em['From'] = f'{radio_display_name}'
        # em['From'] = f'{radio_display_name} <{radio}>'  # Use both display name and email address
        # em.replace_header('From', radio_display_name)  
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content('')
        em.add_alternative(html_content, subtype='html')
        context = ssl.create_default_context()

       
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(radio, email_password)
            smtp.sendmail(radio, email_receiver, em.as_string())

        return redirect(url_for('main')) 



@app.route('/adminlogin/<int:userid>', methods=['GET', 'POST'])
def adminlogin(userid):
    user = Person.query.get_or_404(userid)
    login_user(user)
    return redirect(url_for("admindashboard"))


 

@app.route('/admindashboard', methods=['GET', 'POST'])
@login_required
def admindashboard():
    
    form=Adduser()
    if form.validate_on_submit():
            new=User(
                product_name=form.product_name.data,
                cat=form.cat.data,
                desc=form.desc.data,
                variant=form.variant.data,
                price=form.price.data,
                size=form.price.data,
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            send_email()
            flash("New Product Added ","success")
            return redirect('/')
    print(form.errors)
    return render_template('gvs/admindashboard.html')
    





@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("profileid.html",current_user=current_user, profile=profile, title="list")
 
 
 
@app.route('/list', methods=['GET', 'POST'])
@login_required
def lists():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("list.html", users=users, current_user=current_user, title="list")



@app.route('/logout')
@login_required
def logout():
    if current_user:
        print(current_user.email)
        logout_user()
    flash('You have been logged out.','danger')
    return redirect(url_for("login"))


@app.route('/report',methods=['GET','POST'])
@login_required
def report():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("report.html", users=users, current_user=current_user, title="report")
 
 

#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Adduser()
    user=User.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.year.data =user.year
        form.schools.data =user.schools
        form.level.data =user.level
         
    if request.method== 'POST':
        new=User(name=form.name.data,
            level=form.level.data,
            schools=form.schools.data,
            year=form.year.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('pascoadmin')) 
        except:
            return"errrrror"
    return render_template("leadersadd.html", form=form)
    
#delete route
@app.route("/delete/<int:id>")
def deleteme(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('main')) 
    except: 
        return "errrrrorrr"

@app.context_processor
def inject_status():
    status = 'green' if current_user.is_authenticated else 'red'
    return dict(status=status)



@app.route('/product', methods=['POST','GET'])
def product():  
    users=User.query.order_by(User.id.desc()).all()
    return render_template('gvs/product.html',users=users)


@app.route('/order', methods=['POST','GET'])
def order():  
    users=User.query.order_by(User.id.desc()).all()
    return render_template('gvs/order.html',users=users)

    
@app.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user=Person.query.filter(Person.email.ilike(form.email.data)).first()
        print(form.email.data) 
        
        if user and user.password ==form.password.data:
            login_user(user)
            print ("Logged in:" + user.code + " " + user.email)
            print(form.password.data) 
            flash("Welcome to your dashboard " + " "  + user.name ,  'success')
            return redirect(url_for('admindashboard'))
        else:
            flash(f'Incorrect details, please try again', 'danger')
             
    return render_template('gvs/pages-login.html', form=form)

 



@app.route('/signup', methods=['POST','GET'])
def signup():
    form = Registration()
    if form.validate_on_submit():
        
        unique_code = str(secrets.randbelow(10**12)).zfill(12)  
        
        
        if len(str(form.code.data)) != 4:
            flash('Unique Code must be exactly 4 digits.', 'danger')
            return redirect(url_for('signup'))

        password = form.password.data
        if len(password) < 6 or not re.search("[A-Z]", password) or not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            flash('Password must be at least 6 characters long, contain at least one uppercase letter, and include at least one symbol (!@#$%^&*(),.?":{}|<>).', 'danger')
            return redirect(url_for('signup'))
        else:
            user = Person(password=form.password.data,
                        confirm_password=form.confirm_password.data,
                        email=form.email.data,
                        code=form.code.data, 
                        phone=form.phone.data,
                        unique_code=unique_code,
                        name=form.name.data)
            db.session.add(user)
            db.session.commit()
            send_email()
            params = "New Account Created for " + user.name
            # sendtelegram(params)
            flash("We will send you a Confirmation Code, kindly Confirm your identity.", 'success')
           
            # user = Person.query.filter_by(email = form.email.data).first()
            login_user(user, remember=True)
            return redirect (url_for('login'))
    else:
        print(form.errors)
   
            
    return render_template('gvs/pages-register.html', form=form)






    
    
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=8000, debug=True)
    
  