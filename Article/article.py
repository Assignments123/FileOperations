from flask import Flask,render_template,request
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os
import smtplib
import ssl
import re
import imghdr

article = Flask(__name__)

@article.route('/')
def home():
    return render_template('home.html')

@article.route('/registrationpage')
def registrationpage():
    return render_template('register.html')

@article.route('/register',methods=['POST'])
def register():
    name = request.form['name']

    if not name.isalpha() :
        data = {
            "status":"error",
            "message":"Please Enter Correct Name"
        }
        return render_template('register.html',data=data)
    
    toemail = request.form['email']

    string = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(string,toemail):
        data = {
            "status":"error",
            "message":"Invalid email address"
        }
        return render_template('register.html', data=data)

    fromemail = 'manojkanadi1212@gmail.com'
    password = os.getenv('PASSWORD')
    subject = 'User registration successful'
    message = "Dear "+name +", \n \
Thank you for registering on our website. \
We are excited to have you as part of our community! \n \
You have successfully subscribed to our monthly newsletter. \
We will be sending you the articles and updates directly to your email. \n \
If you have any questions or need assistance, feel free to reach out to us. \n \
Best regards,\n Article.com Website Team "

    em = EmailMessage()
    em['From'] = fromemail
    em['To'] = toemail
    em['subject'] = subject
    em.set_content(message)
    em.add_attachment('img.jpg')
    
    
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465 , context = context) as smtp:
        smtp.login(fromemail,password)
        smtp.send_message(em)
        smtp.sendmail(fromemail,toemail,em.as_string())

    data = {
        "status":"success",
        "message": "user with name "+name + " is registered successfully"
    }
    return render_template('register.html',data = data)


@article.route('/image',methods=["POST"])
def image():
    password = os.getenv('PASSWORD')
    fromemail = "manojkanadi1212@gmail.com"
    name = request.form['name']
    toemail = request.form['email']
    subject = "Image code"
    if not name.isalpha() :
        data = {
            "status":"error",
            "message":"Please Enter Correct Name"
        }
        return render_template('register.html',data=data)
    
    toemail = request.form['email']

    string = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(string,toemail):
        data = {
            "status":"error",
            "message":"Invalid email address"
        }
        return render_template('register.html', data=data)

    try:
    # MIMEMultipart() this is usefull when you have to send multipart files..
        mail = MIMEMultipart()
        mail['From'] = fromemail
        mail['To'] = toemail
        mail['subject'] = subject
    
        msg = "Hello "+name+"\nThis is a basic text with image"
        message = MIMEText(msg,'plain')
        

        # Open and read bytes of image
        image = open('img.jpg','rb').read()
        # file_type = imghdr.what(image.name)
        # set image so that we can attach it to mail
        attchment = MIMEImage(image ,'jpg',name = 'nature.jpg')
        mail.attach(message)
        mail.attach(attchment)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465 , context = context) as smtp:
            smtp.login(fromemail,password)
            print("login successfull")
            smtp.send_message(mail)
            # smtp.sendmail(fromemail,toemail,mail.as_string())
        # return "Mail is sent succesfully"

        data = {
            "status":"success",
            "message": "user with name "+name + " is registered successfully"
        }
        return render_template('register.html',data = data)
    except:
        data = {
            "status":"error",
            "message": "user not registered...Please try again"
        }
        return render_template('register.html',data = data)


@article.route('/pdf',methods=['POST'])
def pdf():
    password = os.getenv('PASSWORD')
    fromemail = "manojkanadi1212@gmail.com"
    name = request.form['name']
    toemail = request.form['email']
    subject = "Image code"

    if not name.isalpha() :
        data = {
            "status":"error",
            "message":"Please Enter Correct Name"
        }
        return render_template('register.html',data=data)
    
    toemail = request.form['email']

    string = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(string,toemail):
        data = {
            "status":"error",
            "message":"Invalid email address"
        }
        return render_template('register.html', data=data)
    
    try:
        # MIMEMultipart() this is usefull when you have to send multipart files.
        mail = MIMEMultipart()
        mail['From'] = fromemail
        mail['To'] = toemail
        mail['subject'] = subject

        msg = "Hello "+name+"\nThis is a basic text with pdf"
        message = MIMEText(msg,'plain')

        # for attaching pdf to mail
        pdf = open('report.pdf','rb').read()
        attachment = MIMEImage(pdf,'pdf',name = "report.pdf")
        mail.attach(message)
        mail.attach(attachment)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465 , context = context) as smtp:
            smtp.login(fromemail,password)
            print("login successfull")
            smtp.send_message(mail)
        # return "Mail is sent succesfully"
        data = {
            "status":"success",
            "message": "user with name "+name + " is registered successfully"
        }
        return render_template('register.html',data = data)
    except:
        data = {
            "status":"error",
            "message": "user not registered...Please try again"
        }
        return render_template('register.html',data = data)



article.run(debug=True,port=5050,host="localhost")