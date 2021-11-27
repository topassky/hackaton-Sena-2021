from flask import Flask, json, request, jsonify
from GUI_pandas import Gui_pandas
app = Flask(__name__)
data_pandas = Gui_pandas("dataset.csv")


@app.route("/")
def server_info():
    good_intentions, bad_intentions = data_pandas.analyze_data()
    intesiones = {"buenas_intesiones":good_intentions, 
                    "malas_intesiones":bad_intentions}
    return jsonify(intesiones)

  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True,
            threaded=True, use_reloader=False)

