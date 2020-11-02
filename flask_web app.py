
from flask import Flask, render_template


test_app2 = Flask(__name__)


@test_app2.route("/")
def home():
    return render_template("home.html", title="Home", custom_css="css/home.css")


@test_app2.route("/add")
def add():
    return render_template("add.html", title="add", custom_css="css/add.css")


skills_progress_list = [("Python", 70), ("Html", 50),
                        ("Css", 40), ("Js", 20), ("Sql", 40)]


@test_app2.route("/skills_progress")
def skills_progress():
    return render_template("skills_progress.html",
                           title="skills Progress",
                           custom_css="css/skills_progress.css",
                           page_head="Skills Progress",
                           page_description="this is my skills Progress page",
                           skills=skills_progress_list
                           )


@test_app2.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    test_app2.run(host="127.0.0.1", port=9000, debug=True)


