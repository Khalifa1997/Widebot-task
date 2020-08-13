from flask import Flask, render_template, request
#from sklearn.externals import joblib
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

#mul_reg = open("multiple_regression_model.pkl", "rb")
#ml_model = joblib.load(mul_reg)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        print(request.form.get('NewYork'))
        try:
            var1 = request.form['var1']
            var4 = request.form['var4']
            var5 = request.form['var5']
            var6 = request.form['var6']
            var7 = request.form['var7']
            var9 = request.form['var9']
            var10 = request.form['var10']
            var12 = request.form['var12']
            var13 = request.form['var13']
            var18 = request.form['var18']
            var19 = float(request.form['var19'])
            dic1 = {'a': 0, 'b': 1}
            dic4 = {'l': 0, 'u': 1, 'y': 2}
            dic5 = {'g': 0, 'gg': 1, 'p': 2}
            dic6 = {'W': 0, 'aa': 1, 'c': 2, 'cc': 3, 'd': 4, 'e': 5, 'ff': 6,
                    'i': 7, 'j': 8, 'k': 9, 'm': 10, 'q': 11, 'r': 12, 'x': 13}
            dic7 = {'bb': 0, 'dd': 1, 'ff': 2, 'h': 3,
                    'j': 4, 'n': 5, 'o': 6, 'v': 7, 'z': 8}
            dic9 = {'f': 0, 't': 1}
            dic10 = {'f': 0, 't': 1}
            dic12 = {'f': 0, 't': 1}
            dic13 = {'g': 0, 'p': 1, 's': 2}
            var1 = dic1[var1]
            var4 = dic4[var4]
            var5 = dic5[var5]
            var6 = dic6[var6]
            var7 = dic7[var7]
            var9 = dic9[var9]
            var10 = dic10[var10]
            var12 = dic12[var12]
            var13 = dic13[var13]

            var2 = float(request.form['var2'])
            var3 = float(request.form['var3'])
            var8 = float(request.form['var8'])
            var11 = float(request.form['var11'])
            var14 = float(request.form['var14'])
            var15 = float(request.form['var15'])
            var17 = float(request.form['var17'])

            varsxd = [var1, var2, var3, var4, var5, var6, var7, var8,
                      var9, var10, var11, var12, var13, var14, var15, var17, var19]
            pred_args_arr = np.array(varsxd)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            # mul_reg = open("multiple_regression_model.pkl", "rb")
            # ml_model = joblib.load(mul_reg)
            loaded_model = pickle.load(open("model.pkl", 'rb'))
            model_prediction = loaded_model.predict(pred_args_arr)
            print("prediction: " + str(model_prediction[0]))
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction=("Yes" if model_prediction[0] == 1 else "No"))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
