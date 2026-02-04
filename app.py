from flask import Flask, render_template, request, redirect
from config import Config
from db import get_db_connection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    # If form is submitted
    if request.method == "POST":
        message = request.form.get("message")

        if message:
            cursor.execute(
                "INSERT INTO messages (content) VALUES (%s)",
                (message,)
            )
            conn.commit()

        return redirect("/")

    # Fetch messages
    cursor.execute("SELECT content, created_at FROM messages ORDER BY id DESC")
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        app_name=Config.APP_NAME,
        environment=Config.ENV,
        messages=messages
    )

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
