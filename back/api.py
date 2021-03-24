from flask import Flask, request
from mySql import mysql_
from user import users
from cars import cars
from ensuring import ensuring



app = Flask(__name__)
db = mysql_('localhost', 'root', 'Ido*&@#132465798', 'ototHoad')
users_  = users(db)
cars_ = cars(db)
ensuring_ = ensuring(db)

######################
# USER FUNCTIONS API 
######################

#route to user will create new user
# need to get for example {'id':1, 'name':"ido" ...}
@app.route('/user', methods=['POST'])
def create_user():
    user = request.json
    return users_.insertUsers(user)
   

#route to usersSelect will return the userTable
@app.route('/userSelect', methods=['GET'])
def select_users():
    return users_.selectUsers()

#route to  userSelectSpesific will return the a spesifcs users
# need to get for example:[{'id':1}]
@app.route('/userSelectSpesific', methods=['POST', 'GET'])
def select_spesific_users():
    wherelist = request.json
    return users_.selectSpesificUser(wherelist)

#route to userUpdate will update a user
# need to get [[{where}],[{update}]]

@app.route('/userupdate', methods=['POST'])
def updateuser():
    data = request.json
    whereList = data[0]
    updateList = data[1]
    return users_.updateUser(updateList, whereList)

#route to userDelete will delete user
#new to get [{where}]
@app.route('/userDelete', methods=['POST'])
def user_delete():
    whereList = request.json
    return users_.deleteUser(whereList)


######################
# USER FUNCTIONS API 
######################



######################
# CAR FUNCTIONS API 
######################

#route to car will create new car
# need to get for example {'id':1, ...}
@app.route('/car', methods=['POST'])
def create_car():
    carValue = request.json
    return cars_.insertToCar(carValue)

#route to carsSelect will return the carsTable
@app.route('/carsSelect', methods=['GET'])
def select_cars():
    return cars_.selectAllCar()

#route to  carsSelectSpesific will return the a spesifcs cars
# need to get for example:[{'id':1}]
@app.route('/carsSelectSpesific', methods=['POST', 'GET'])
def select_spesific_car():
    wherelist = request.json
    return cars_.selectSpesificCar(wherelist)

#route to carUpdate will update a car
# need to get [[{where}],[{update}]]
@app.route('/carUpdate', methods=['POST'])
def update_car():
    data = request.json
    whereList = data[0]
    updateList = data[1]
    return cars_.upadateCar(whereList, updateList)

#route to carDelete will delete car
#new to get [{where}]
@app.route('/carDelete', methods=['POST'])
def car_delete():
    whereList = request.json
    return cars_.deleteCar(whereList)



######################
# CAR FUNCTIONS API 
######################


######################
# ENSURING FUNCTIONS API 
######################


#route to ensuring will create new ensuring
# need to get for example {'id':1, ...}
@app.route('/ensuring', methods=['POST'])
def create_ensuring():
    ensuring = request.json
    return ensuring_.insertToEnsuring(ensuring)

#route to ensuringSelect will return the ensuringTable
@app.route('/ensuringSelect', methods=['GET'])
def select_ensuring():
    return ensuring_.selectAllEnsuring()

#route to  ensuringSelectSpesific will return a spesifcs ensuring
# need to get for example:[{'id':1}]
@app.route('/ensuringSelectSpesific', methods=['POST', 'GET'])
def select_spesific_ensuring():
    wherelist = request.json
    return ensuring_.selectSpesificEnsuringr(wherelist)

#route to ensuringUpdate will update a car
# need to get [[{where}],[{update}]]
@app.route('/ensuringUpdate', methods=['POST'])
def update_ensuring():
    data = request.json
    whereList = data[0]
    updateList = data[1]
    return ensuring_.upadateEnsuring(whereList, updateList)

#route to ensuringDelete will delete ensuring
#new to get [{where}]
@app.route('/ensuringDelete', methods=['POST'])
def ensuring_delete():
    whereList = request.json
    return ensuring_.deleteEnsuring(whereList)




######################
# ENSURING FUNCTIONS API 
######################


