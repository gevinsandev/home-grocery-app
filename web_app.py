from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Load items from file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            return {
                "active_items": data.get("active_item", []),
                "history": data.get("history", [])
            }
            
    except:
        return {
            "active_items": [],
            "history": []
        }

# Save items to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load once when app starts
data = load_data()

items = data["active_items"]
history = data["history"]

@app.route("/")
def home():
    return render_template(
        "index.html",
        items=items,
        history=history
        )

@app.route("/add", methods=["POST"])
def add():
    item = request.form.get("item")

    if item and item.strip():
        items.append({
            "name": item.strip(),
            "done": False
        })

        save_data(items)

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(items):
        items.pop(index)

        save_data(items)

    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(items):
        items[index]["done"] = not items[index]["done"]

        save_data(items)

    return redirect("/")

from datetime import datetime

@app.route("/complete")
def complete():
   
    if items:

        history.append({
            "date": datetime.now().strftime("%d %B %Y"),
            "items": items.copy()
        })
        items.clear()

        save_data(data)

    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


