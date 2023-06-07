from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,PasswordField,IntegerField
from wtforms.validators import DataRequired
FAI=Flask(__name__)


class NameForm(Form):
    Name=StringField(validators=[DataRequired()])
    Password=PasswordField(validators=[DataRequired()])
    age=IntegerField(default=None)
    Submit=SubmitField()

@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    NFO=NameForm()
    if request.method=='POST':
        NFD=NameForm(request.form)
        if NFD.validate():
            return NFD.data

    return render_template('webforms.html',NFO=NFO)

if __name__=='__main__':
    FAI.run(debug=True)