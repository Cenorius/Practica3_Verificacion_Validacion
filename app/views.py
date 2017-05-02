from flask import render_template
from flask import Flask, request
from app import app
from .form import FormText
import Practica

@app.route('/' ,methods=['POST','GET'])
def count():	
    #text=request.form.get('text')
    form = FormText(request.form)   
    result=""

    print form.errors

    if form.validate():
        text=form.text.data
        temp=Practica.count(text)
        for e in temp:
            result+=str(e)+", "
    else:
        print form.text
    return render_template("wordsCounter.html", results=result)

    
