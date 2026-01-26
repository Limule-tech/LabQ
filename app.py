from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "labq-secret-key"  # obligatoire pour flash

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # DEMO LOGIC (à remplacer plus tard par DB)
        if email != "scientist@lab.com" or password != "lab123":
            flash("Email or Password Incorrect", "error")
            return redirect(url_for("login"))

        flash("Connection Successfull", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/register")
def register():
    return "<h1>Register page</h1>"


@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome To ScienceLab 🔬</h1>"


if __name__ == "__main__":
    app.run(debug=True)