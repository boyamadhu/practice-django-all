from flask import Flask

AP=Flask(__name__)

@AP.route('/wish')
def wish():
    return 'hello this is the basic project of flask'

AP.run(debug=True,port=5001,host='192.168.45.79')