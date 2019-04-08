from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

recipes = [
    {
        "Recipe": "Chicken & tofu noodle soup",
        "Ingredients": "   2 shallots (140g), 2 cloves of garlic, 2cm piece of ginger, 4 free-range chicken thighs, skin off, bone in, groundnut oil,  sesame oil, 1 star anise,  ½ a bunch of fresh coriander,  ½ a bunch of fresh mint, 100g tofu",
        "steps": "Start preparing the soup the night before. Peel and finely slice the shallots, garlic and ginger. Remove the meat from the chicken thighs, reserving the bones, and slice it into nice thin strips. Place a large pan over a medium–low heat and pour in a good lug of groundnut oil, then fry the shallots, ginger and garlic for 5 minutes, or until soft, then add the chicken and 1 tablespoon of sesame oil and fry for a few minutes more. Add the chicken bones and star anise, then cover with 700ml of water. Gently bring to the boil, reduce the heat to low, cover the pan with a lid and simmer for 35 to 40 minutes, or until the chicken is tender. etc..."
    },
    {
        "Recipe": "Roasted salmon & artichokes",
        "Ingredients": " olive oil, 2 x 1 kg sides of salmon , skin on, scaled, pin-boned, from sustainable sources, 100 g blanched almonds, cloves of garlic, 2 lemons, 100 g stale ciabatta, 2 fresh baby Italian artichokes, 1 x 280 g jar of artichoke hearts in oil, 1 bunch of fresh mint , (30g) ",
        "steps": "Preheat the oven to 220ºC/425ºF/gas 7. Line a large baking tray with greaseproof paper and rub with a little oil.Lay 8 pieces (roughly an arm’s length each) of butcher’s string at 5cm intervals widthways across the tray, then place one salmon fillet on top, skin side down.Toast the almonds in a dry frying pan until golden, tossing regularly, then tip into a food processor. Peel, roughly chop and add the garlic, finely grate in the lemon zest, then tear in the ciabatta. Season with black pepper, then pulse until finely chopped. Carefully layer the crumbs over the salmon.Halve 1 lemon. Trim the fresh artichoke stalks 2cm from the base. Peel away the tough outer leaves until you reach the paler ones that are tender enough to eat, then trim the heads to 3cm, rubbing with the cut lemon as you go to prevent discoloration. etc.."
    },
    {
        "Recipe": "tortilla",
        "Ingredients": "300 g waxy potatoes , 1 onion, olive oil, 5 large free-range eggs",
        "steps": "Peel the potatoes using a speed-peeler, then carefully cut them into thin slices. Pat the potato slices dry with a clean tea towel. Peel and finely slice the onion. Drizzle 2 tablespoons of oil into a small frying pan over a medium heat, then add the onion and potatoes.Turn the heat down to low and cook for 25 to 30 minutes, or until the onions are turning golden and the potato slices are cooked through. Try not to stir it too much or the potatoes will break up – just use a fish slice to flip them over halfway through. etc.. "
    }
]

class Food(Resource):
    def get(self, Recipe):
        for food in recipes:
            if(Recipe == food["Recipe"]):
                return food, 200
        return "recipe not found", 404

    def post(self, Recipe):
        parser = reqparse.RequestParser()
        parser.add_argument("Ingredients")
        parser.add_argument("steps")
        args = parser.parse_args()

        for food in recipes:
            if(Recipe == food["Recipe"]):
                return "recipe with title {} already exists".format(Recipe), 400

        food = {
            "Recipe": Recipe,
            "Ingredients": args["Ingredients"],
            "steps": args["steps"]
        }
        recipes.append(food)
        return food, 201

    def put(self, Recipe):
        parser = reqparse.RequestParser()
        parser.add_argument("Ingredients")
        parser.add_argument("steps")
        args = parser.parse_args()

        for food in recipes:
            if(Recipe == food["Recipe"]):
                food["Ingredients"] = args["Ingredients"]
                food["steps"] = args["steps"]
                return food, 200
        
        food = {
            "Recipe": Recipe,
            "Ingredients": args["Ingredients"],
            "steps": args["steps"]
        }
        recipes.append(food)
        return food, 201

    def delete(self, Recipe):
        global recipes
        recipes = [food for food in recipes if food["Recipe"] != Recipe]
        return "{} is deleted.".format(Recipe), 200
      
api.add_resource(Food, "/food/<string:Recipe>")

app.run(debug=True)