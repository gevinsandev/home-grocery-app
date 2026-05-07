# Import tools from Flask
# Flask = the web server
# render_template_string = lets us show HTML directly
# request = handles form input
# redirect = sends user back to homepage after actions
from flask import Flask, render_template_string, request, redirect

# Create the app
# __name__ tells Flask where your app lives
app = Flask(__name__)

# This is your grocery list stored in memory
# NOTE: This resets when the server stops
items = []

# This is your webpage (HTML)
# Think of this as the "screen" your phone will show
HTML = """
<!doctype html>
<html>
<head>
<title>Grocery App</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    padding: 20px;
}

.container {
    max-width: 400px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}

h1 {
    text-align: center;
}

form {
    display: flex;
    gap: 10px;
}

input {
    flex: 1;
    padding: 10px;
}

button {
    padding: 10px;
    background: #2ecc71;
    border: none;
    color: white;
    border-radius: 5px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    display: flex;
    justify-content: space-between;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}

a {
    color: red;
    text-decoration: none;
}
</style>

</head>

<body>

<div class="container">
    <h1>Grocery List</h1>

    <form method="POST" action="/add">
        <input name="item" placeholder="Add item" required> 
        <button type="submit">Add</button>
    </form>

    <ul>
    {% for i in items %}
        <li>
            {{ i }}
            <a href="/delete/{{ loop.index0 }}">Remove</a>
        </li>
    {% endfor %}
    </ul>
</div>

</body>
</html>
"""

# Route for homepage "/"
# This runs when you open the app in browser
@app.route("/")
def home():
    # Sends the HTML page with current items
    return render_template_string(HTML, items=items)

# Route to add items
@app.route("/add", methods=["POST"])
def add():
    # Get item from form input
    item = request.form.get("item")

    # Check item is not empty
    if item and item.strip():
        # Add cleaned item to list
        items.append(item.strip())

    # Go back to homepage after adding
    return redirect("/")

# Route to delete items
@app.route("/delete/<int:index>")
def delete(index):
    # Check index is valid
    if 0 <= index < len(items):
        # Remove item at position
        items.pop(index)

    # Go back to homepage
    return redirect("/")

# Start the server
if __name__ == "__main__":
    # host="0.0.0.0" allows phone access on same WiFi
    # port=5000 is the app port
    # debug=True auto reloads when you save changes
    app.run(host="0.0.0.0", port=5000, debug=True)