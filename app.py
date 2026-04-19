@app.route("/contact19", methods=["GET", "POST"])
def contact19():

    if request.method == "POST":

        phone = request.form.get("phone")
        address = request.form.get("address")

        return render_template(
            "result19.html",
            phone=phone,
            address=address
        )

    return render_template("index19.html")
