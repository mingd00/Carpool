import pymysql
from flask import Flask
from flask import render_template
conn=None
cur=None
sql=''

conn=pymysql.connect(host='orion.mokpo.ac.kr',
                     port=8380,
                     user='root',
                     passwd='ScE1234**',
                     db='CARS',
                     charset='utf8')
cur=conn.cursor()
app=Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/driver')
def driver():
    return render_template('driver.html')

@app.route('/choice')
def choice():
    return render_template('choice.html')

@app.route('/complete')
def complete():
    return render_template('complete.html')

@app.route('/car')
def car():
    sql='SELECT * FROM Car_List;'
    cur.execute(sql)
    car_list=cur.fetchall()
    return render_template('car.html', car_data=car_list)