from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.statistics import Statistic

@app.route('/estadisticas/add')
def showuser():
    return render_template("statistics_add.html")

@app.route('/estadisticas/year')
def dashboardd():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }
    statistic = Statistic.show_all(formulario)
    user = User.get_by_id(formulario)
    return render_template('statistics_year.html', user=user, statistic=statistic)


@app.route('/estadisticas/add')
def statistics_add():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario)
    return render_template('statistics_add.html', user=user)


@app.route('/register/statistics', methods=['POST'])
def register_statistics():
    if 'user_id' not in session:
        return redirect('/estadisticas/add')

    Statistic.save(request.form)
    return redirect('/estadisticas/year')

#-----------------
@app.route('/update/statistic', methods=['POST'])
def update_statistic():
    if 'user_id' not in session:
        return redirect('/')
    if not Statistic.validate_appointment(request.form):
        return redirect('/edit/appointment/' + request.form['id'])

    Statistic.update(request.form)
    return redirect('/appointments')


@app.route('/delete/statistic/<int:id>')
def delete_statistic(id):
    if 'user_id' not in session:
        return redirect('/estadisticas/add')
    formulairo = {'id': id}
    Statistic.delete(formulairo)
    return redirect('/estadisticas/year')








