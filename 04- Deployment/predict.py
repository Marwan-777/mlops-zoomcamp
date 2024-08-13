import pandas as pd 
import numpy as np
from flask import Flask, request


app = Flask('application')

@app.route('/first_app', methods=['POST'])
def pred():
    average = np.mean(request.get_json()['values'])
    return 'The average of your values is: ' + str(average)


if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0', port=3000)
