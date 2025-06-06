from flask import Flask 
from flask import jsonify

app = Flask(__name__)

ice_cream_flavours = {
    "Classic": [
        "🍦 Vanilla",
        "🍫 Chocolate",
        "🍓 Strawberry",
        "🍮 Butterscotch",
        "☕ Coffee"
    ],
    "Fruity": [
        "🥭 Mango",
        "🍇 Black Currant",
        "🍈 Lychee",
        "🍍 Pineapple",
        "🥥 Tender Coconut"
    ],
    "Nutty": [
        "🌼 Kesar Pista",
        "🌰 Roasted Almond",
        "🥜 Walnut Fudge",
        "🥄 Peanut Butter Swirl"
    ],
    "Exotic": [
        "🍰 Tiramisu",
        "🍵 Matcha Green Tea",
        "🧂🍬 Salted Caramel",
        "🫐🍰 Blueberry Cheesecake",
        "❤️🍰 Red Velvet"
    ],
    "Sugar-Free": [
        "🍦 Vanilla (SF)",
        "🍫 Chocolate (SF)",
        "🥭 Mango (SF)"
    ]
}

# STATIC ROUTES
@app.route('/')
def welcome():
    return "Welcome to my Ice-cream store... 🍨🍨🍨🍨"

@app.route('/ice-cream/all/types')
def getAllTypes():
    return str(ice_cream_flavours.keys())

@app.route('/ice-cream/all')
def getAll():
    return jsonify(ice_cream_flavours)

# DYNAMIC ROUTES
@app.route('/ice-cream/<type>')
def getByType(type):
    try:
        return f"""
            🍨 Your ice-cream type is {type}🧊
            The list of ice-creams are: {ice_cream_flavours[type]}
        """
    except Exception as e:
        return "some thing went wrong " + str(e)

if __name__== '__main__':
    app.run(debug=True)
