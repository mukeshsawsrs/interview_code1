# import necessary libraries and modules
from app import app
from app.database import delete_usecase, get_data, get_usecases, insert_usecase, update_usecase
from flask import render_template, redirect, url_for, request


# define routes for our flask app
# route for home page
@app.route("/", methods=['GET','POST'])
def index():
    # get all entity names and department names to be filled in dropdown options in the html form
    entities, departments = get_data()

    # set keyword arguments to be passed to the frontend
    kwargs = {"entities":entities, "departments":departments}
    
    # steps to perform only if the form is submitted
    if request.method == 'POST':
        # get all the values entered by user
        usecase_name = request.form['usecase_name']
        entity = request.form['entity']
        department = request.form['department']
        usecase_descr = request.form['usecase_descr']

        # insert usecase values into the database
        insert_usecase(usecase_name, entity, department, usecase_descr)
        
        # reload the home page
        return render_template("index.html", **kwargs)
    
    # load the home page
    return render_template("index.html", **kwargs)

# route for the usecase page where all usecases are displayed
@app.route("/usecases")
def usecases():
    # fetch all the usecases from the database
    usecases = get_usecases()

    # get all entity names and department names to be filled in dropdown options in the html form
    entities, departments = get_data()

    # set keyword arguments to be passed to the frontend
    kwargs = {"usecases":usecases, "entities":entities, "departments":departments}
    
    # load the usecase page with all the data
    return render_template("usecases.html", **kwargs)

# route to update a usecase in database
@app.route("/update", methods=['GET', 'POST'])
def update():
    # update only if form by submitted 
    if request.method == 'POST':
        # get updated values for the usecase
        usecase_id = request.form['usecase_id']
        usecase_name = request.form['usecase_name']
        entity = request.form['entity']
        department = request.form['department']
        usecase_descr = request.form['usecase_descr']

        # update the data in the database
        update_usecase(usecase_id, usecase_name, entity, department, usecase_descr)
        
    # redirect to the usecase page and display the updated data
    return redirect(url_for('usecases'))

# route to delete a usecase
@app.route("/delete", methods=['GET', 'POST'])
def delete():
    # delete only if form was submitted
    if request.method == 'POST':
        # get id for the usecase to be deleted
        usecase_id = request.form['u_id']

        # delete usecase from the database
        delete_usecase(usecase_id)
    
    # redirect to the usecase page and display the updated data
    return redirect(url_for('usecases'))