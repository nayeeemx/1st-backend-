# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:06:51 2022

@author: 21pw15
"""

''' BACKEND SERVER '''


from flask import Flask,request

app = Flask(__name__)

student={
           '1':{"id":1,"name":"nayeem","mark":100},
           '2':{"id":2,"name":"shyam","mark":10},
           '3':{"id":3,"name":"kanishk","mark":90},
           '4':{"id":4,"name":"abd","mark":99},
           '5':{"id":5,"name":"hamza","mark":10},
           '6':{"id":6,"name":"deepe","mark":20},
           '7':{"id":7,"name":"tharun","mark":14},
           '8':{"id":8,"name":"nithiesh","mark":60},
           '9':{"id":9,"name":"shankes","mark":19},
           '10':{"id":10,"name":"guava","mark":20},
           
         }




@app.route('/p')
def opop():
    return '<h>hello world</h>'

@app.route('/get/students/<id>')
def display(id):
    
   return student[id]

@app.route('/get/students')
def displayall():
    return student


if __name__=='__main__':
    app.run()

