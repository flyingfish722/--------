from inspect import Parameter
from TrajectoryAnalysis import app
from flask import render_template, url_for, redirect
from TrajectoryAnalysis.forms import ParameterForm, DataAnalysisForm

@app.route('/home/')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dataanalysis/', methods=['GET', 'POST'])
def dataAnalysis():
    form = DataAnalysisForm()
    form.dataList.choices = ['traj1', 'traj2']
    form.algorithm.choices = ['PM-CFSFDP', 'DBSCAN']
    if form.validate_on_submit():
        return redirect(url_for('setParameter'))
    return render_template('dataanalysis.html', form=form)

@app.route('/parameter/', methods=['GET', 'POST'])
def setParameter():
    form = ParameterForm()
    if form.validate_on_submit():
        #进行聚类
        pic = 0
        return render_template('result.html', pic=pic)
    return render_template('dataanalysis.html', form=form)

@app.route('/datastorage/')
def dataStorage():
    return render_template('datastorage.html')

@app.route('/datapreprocess/')
def dataPreprocess():
    return render_template('datapreprocess.html')