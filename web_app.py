from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Load items from file
def load_items():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

# Save items to file
def save_items(items):
    with open(DATA_FILE, "w") as file:
        json.dump(items, file)

# Load once when app starts
items = load_items()

@app.route("/")
def home():
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add():
    item = request.form.get("item")

    if item and item.strip():
        items.append({
            "name": item.strip(),
            "done": False
        })
        save_items(items)

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(items):
        items.pop(index)
        save_items(items)

    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(items):
        items[index]["done"] = not items[index]["done"]
        save_items(items)

    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)