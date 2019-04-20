from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee
import random

counter = random.randint(6,100000)

@auth.route('/register', methods=['GET','POST'])
def register():
	"""
	Handle request to the /register route
	Sdd an employee to the database through registration form 
	"""
	global counter
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data,
							username=form.username.data,
id = counter,							first_name=form.first_name.data,
							last_name=form.last_name.data,
							password=form.password.data, tier="1")

		# add an employee to the database
		counter = counter + 1
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered! You may now log in.')
		fo= open("create.sh", "w")
		filebuffer = ["aws cloudformation create-stack --stack-name ec2stk1 --template-body file://ec2stack.yml"]
		fo.writelines(filebuffer)
		fo.close()
		# Create.sh HERE

		# redirect to the login page
		return redirect(url_for('auth.login'))

	return render_template('auth/register.html', form=form, title='Register')

@auth.route('/register2', methods=['GET','POST'])
def register2():
	global counter
	"""
	Handle request to the /register route
	Sdd an employee to the database through registration form 
	"""
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data,
							username=form.username.data,
id = counter,							first_name=form.first_name.data,
							last_name=form.last_name.data,
							password=form.password.data, tier="2")

		# add an employee to the database
		counter = counter + 1
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered! You may now log in.')
		fo= open("create2.sh", "w")
		filebuffer = ["aws cloudformation create-stack --stack-name ec2stk2 --template-body file://ec2stack2.yml"]
		fo.writelines(filebuffer)
		fo.close()
		# redirect to the login page
		return redirect(url_for('auth.login'))

	return render_template('auth/register2.html', form=form, title='Register')

@auth.route('/register3', methods=['GET','POST'])
def register3():
	global counter
	"""
	Handle request to the /register route
	Sdd an employee to the database through registration form 
	"""
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data,
							username=form.username.data,
id = counter,							first_name=form.first_name.data,
							last_name=form.last_name.data,
							password=form.password.data, tier="3")

		# add an employee to the database
		counter = counter + 1
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered! You may now log in.')
		fo= open("create3.sh", "w")
		filebuffer = ["aws cloudformation create-stack --stack-name ec2stk3 --template-body file://ec2stack3.yml"]
		fo.writelines(filebuffer)
		fo.close()
		# redirect to the login page
		return redirect(url_for('auth.login'))

	return render_template('auth/register3.html', form=form, title='Register')

@auth.route('/registerGold', methods=['GET','POST'])
def registerGold():
	global counter
	"""
	Handle request to the /register route
	Sdd an employee to the database through registration form 
	"""
	form = RegistrationForm()
	if form.validate_on_submit():
		employee = Employee(email=form.email.data,
							username=form.username.data,
id = counter,							first_name=form.first_name.data,
							last_name=form.last_name.data,
							password=form.password.data, tier="Gold")
		
		# add an employee to the database
		counter = counter + 1
		db.session.add(employee)
		db.session.commit()
		flash('You have successfully registered! You may now log in.')
		fo= open("createGold.sh", "w")
		filebuffer = ["aws cloudformation create-stack --stack-name ec2stk4 --template-body file://ec2stack4.yml"]
		fo.writelines(filebuffer)
		fo.close()
		# redirect to the login page
		return redirect(url_for('auth.login'))

	return render_template('auth/register-gold.html', form=form, title='Register')

@auth.route('/login', methods=['GET','POST'])
def login():
	"""
	Handle requests to the /login route
	Log an employee in through the login form
	"""
	form = LoginForm()
	if form.validate_on_submit():

		# check whether the employee exists in the database and whether the password entered matches the passsword in the database
		
		employee = Employee.query.filter_by(email=form.email.data).first()
		if employee is not None and employee.verify_password(form.password.data):

			# log employee in 
			login_user(employee) 

			# redirect to the appropriate dashboard page
			if employee.is_admin:
				return redirect(url_for('home.admin_dashboard'))
			else:
				return redirect(url_for('home.dashboard'))



		# when login details are not correct
		else:
			flash('Invalid Email or Password')

	# load login template
	return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
	"""
	Handle requests to the /logout route
	Log an employee out through the logout link
	"""
	logout_user()
	flash('You have successfully been logged out')

	# redirect to the login page
	return redirect(url_for('auth.login'))
@auth.route('/subscribe')
def subscribe():
	"""
	Render the homepage template on the / route
	"""
	return render_template('/subscribe.html', title="Subscribe")


@auth.route('/register5', methods=['GET','POST'])
def register5():
	global counter
	# counter = counter + 1
	# db.session.add(employee)
	# db.session.commit()
	fo= open("delete.sh", "w")
	filebuffer = ["aws cloudformation delete-stack --stack-name ec2stk1"]
	fo.writelines(filebuffer)
	fo.close()
	fo= open("create1.sh", "w")
	filebuffer = ["aws cloudformation create-stack --stack-name ec2stk1 --template-body file://ec2stack1.yml"]
	fo.writelines(filebuffer)
	fo.close()

	return render_template('auth/register5.html', title='Register')

@auth.route('/register6', methods=['GET','POST'])
def register6():
	global counter

	fo= open("delete.sh", "w")
	filebuffer = ["aws cloudformation delete-stack --stack-name ec2stk2"]
	fo.writelines(filebuffer)
	fo.close()
	fo= open("create2.sh", "w")
	filebuffer = ["aws cloudformation create-stack --stack-name ec2stk2 --template-body file://ec2stack2.yml"]
	fo.writelines(filebuffer)
	fo.close()
	return render_template('auth/register6.html', title='Register')

@auth.route('/register7', methods=['GET','POST'])
def register7():
	global counter

	fo= open("delete.sh", "w")
	filebuffer = ["aws cloudformation delete-stack --stack-name ec2stk3"]
	fo.writelines(filebuffer)
	fo.close()
	fo= open("create3.sh", "w")
	filebuffer = ["aws cloudformation create-stack --stack-name ec2stk3 --template-body file://ec2stack3.yml"]
	fo.writelines(filebuffer)
	fo.close()
	return render_template('auth/register7.html', title='Register')

@auth.route('/register8', methods=['GET','POST'])
def register8():
	global counter

	fo= open("delete.sh", "w")
	filebuffer = ["aws cloudformation delete-stack --stack-name ec2stk4"]
	fo.writelines(filebuffer)
	fo.close()
	fo= open("create4.sh", "w")
	filebuffer = ["aws cloudformation create-stack --stack-name ec2stk1 --template-body file://ec2stack4.yml"]
	fo.writelines(filebuffer)
	fo.close()
	return render_template('auth/register8.html', title='Register')