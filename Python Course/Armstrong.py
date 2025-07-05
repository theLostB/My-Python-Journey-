from flask import Flask, jsonify, request 
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr

    print(f"User Agent: {user_agent}")
    print(f"IP Address: {ip_address}")
   
    with open('User_info_DB.log', 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - User Agent: {user_agent}, IP Address: {ip_address}\n")

    
@app.route('/armstrong/<int:n>')
def armstrong(n):
    index()
    sum = 0
    order = len(str(n))
    copy_n = n
    
    while(n>0):
        digit = n%10
        sum += digit ** order
        n = n//10
    
    if (sum==copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            'Number': copy_n,
            'Armstrong': True,
            'Server IP': '193.108.21.48'
            
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            'Number': copy_n,
            'Armstrong': False,
            'Server IP': '193.108.21.48'
            
        }
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True)