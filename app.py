import os
import PyPDF2
from flask import Flask,render_template,redirect,request,jsonify
from Code.Inference import main

from bert import QA

app= Flask(__name__)

wsgi_app = app.wsgi_app
model = QA("bert-large-uncased-whole-word-masking-finetuned-squad")
# result=""

@app.route('/')
def hello():
    return render_template("index.html", message ="Enter your Comprehension")


@app.route('/upload',methods = ['POST'])
def upload():
        file=request.files["file"]
        file.save(os.path.join("uploads", file.filename))
        pdf_file_obj = open('uploads/' + file.filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        numPages=pdf_reader.numPages
        result = ""
        for i in range(numPages):
            page_obj = pdf_reader.getPage(i)
            result += page_obj.extractText()
  
        print(result)
        return render_template("index.html", message=result)


    
@app.route('/model1',methods=['POST'])
def getp():
    if request.method=='POST':
        para=request.form['para']
        q=request.form['ques']
        # print("hello")
        answer="2000"
        # if len(result)!=0:
        #     para=result
        try:
            print(para)
            answer = model.predict(para,q)
            answer=answer['answer']
            
        except Exception as e:
            print(e)
        
        return render_template("index.html", ans=answer,para=para, ques=q)

@app.route('/model2',methods=['POST'])
def getpred():
    if request.method=='POST':
        para=request.form['para']
        q=request.form['ques']
        # print("hello")
        answer="2000"
        # if len(result)!=0:
        #     para=result
        try:
            print(para)
            # answer = model.predict(para,q)
            # answer=answer['answer']

            a = main(paragraph = para , questions = [q])

            response = {
                "reply" : a
            }
            
        except Exception as e:
            print(e)
        
        return render_template("index.html", ans=a[0]["text"],para=para, ques=q)

@app.route('/predict',methods=['POST'])
def predict():
    doc = request.json["document"]
    q = request.json["question"]
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

@app.route("/predict2" , methods = ['POST' , 'GET'])
def predict2() :
	# message = request.get_json(force = True)
	# ques = message["quest"]

	a = main(paragraph = request.json["document"] , questions = [request.json["question"]])

	response = {
		"reply" : a
	}

	return jsonify(response)

    
if __name__=='__main__' :
    app.run(debug=True)