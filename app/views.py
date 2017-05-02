from flask import render_template
from flask import Flask, request
from app import app
from text_form import text_form
import Practica

@app.route('/' ,methods=['POST','GET'])
def count():	
    text=request.form.get('text')
    result=""
    print request.form  
    if(text is not None):
        temp=Practica.count(text)
        for e in temp:
            result+=str(e)+", "
    
    return render_template("wordsCounter.html", results=result)

    
