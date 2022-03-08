from flask import Flask, render_template, redirect, url_for, request

project = Flask(__name__,static_url_path="",static_folder="static")

@project.route("/")
def HomePage():
    return redirect(url_for("search"))

@project.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        name = request.form["user_search"]
        return render_template("result.html", result = name)
    else:
        return render_template("search.html")

# @project.route("/<show>")
# def display(show):
#     return render_template("result.html",result=show)


if __name__ == "__main__":
    project.run(debug= True)

