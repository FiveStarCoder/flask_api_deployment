from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def myapi():
    if request.method == 'POST':
        if request.is_json:
            return jsonify({"message":f"You sent {request.json['data']}"})
        return jsonify({"message":f"Bad Format Request"})
    
    else:
        return jsonify({"message":"GET METHOD IS SENT"})



if __name__ == '__main__':
    app.run(debug=True)