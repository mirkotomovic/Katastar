from flask import Flask, render_template
from flask import request
from sql.mariaDB import (
    create_connection,
    execute_query,
    getParceleDataByNaziv,
    getObjekatDataByNaziv,
    getPodObjekatDataByNaziv,
)

app = Flask(__name__)


conn = create_connection("localhost", "root", "", "katastar")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    naziv = str(request.form["naziv"]).upper()
    parcele = getParceleDataByNaziv(naziv, conn=conn)
    objekati = getObjekatDataByNaziv(naziv, conn=conn)
    delovi_objekata = getPodObjekatDataByNaziv(naziv, conn=conn)
    print(objekati)
    return render_template(
        "search.html",
        parcele=parcele,
        objekati=objekati,
        delovi_objekata=delovi_objekata,
    )


def check(l):
    if len(l) == 0:
        return ""
    return l[0][2]


if __name__ == "__main__":
    app.run(debug=True)
