from flask import Flask, render_template, request

app = Flask(__name__)

class_roster = [("Sayef","A","Junior"),("Joshua","B+","Senior"),("Kevin","A-","Junior"),
("Tiffany","B","Sophomore"),("Karl","A","Senior"),("Eric","A","Junior"),("Leo","D","Freshman")]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html",student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()
