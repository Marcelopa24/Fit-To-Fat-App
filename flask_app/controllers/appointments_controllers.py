from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.appointments import Appointment

@app.route('/appointments')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    appointment = Appointment.show_all(formulario)
    user = User.get_by_id(formulario)
    appointment_missed = Appointment.show_appointment_missed(formulario)
    print(appointment_missed)
    return render_template('appointments.html', user=user, appointment=appointment, appointment_missed=appointment_missed)


@app.route('/appointment/add')
def appointment_add():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    return render_template('appointment_add.html', user=user)


@app.route('/register/appointment', methods=['POST'])
def register_appointment():
    if 'user_id' not in session:
        return redirect('/')
    if not Appointment.validate_appointment(request.form):
        return redirect('/appointment/add')

    Appointment.save(request.form)
    return redirect('/appointments')


@app.route('/edit/appointment/<int:id>')
def edit_appointment(id):
    if 'user_id' not in session:
        return redirect('/')

    formulario = {'id': id}
    appointment = Appointment.get_appointment(formulario)
    formulario1 = {
        'id': session['user_id']
    }
    user = User.get_by_id(formulario1)
    return render_template('edit_appointment.html', user=user, appointment=appointment)


@app.route('/update/appointment', methods=['POST'])
def update_appointment():
    if 'user_id' not in session:
        return redirect('/')
    if not Appointment.validate_appointment(request.form):
        return redirect('/edit/appointment/' + request.form['id'])

    Appointment.update(request.form)
    return redirect('/appointments')


@app.route('/delete/appointment/<int:id>')
def delete_appointment(id):
    if 'user_id' not in session:
        return redirect('/')
    formulairo = {'id': id}
    Appointment.delete(formulairo)
    return redirect('/appointments')




