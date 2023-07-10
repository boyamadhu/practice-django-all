from flask import Flask,render_template

API=Flask(__name__)

@API.route('/all_well')
def all_well():
    return render_template('all_well.html')
if __name__=='__main__':
    API.run(debug=True)
