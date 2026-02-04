from flask import Flask, render_template, request, redirect
from config import Config
from db import get_db_connection

app = Flask(__name__)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# 🔥 CRITICAL
init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        message = request.form.get("message")
        if message:
            cursor.execute(
                "INSERT INTO messages (content) VALUES (%s)",
                (message,)
            )
            conn.commit()
        return redirect("/")

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
