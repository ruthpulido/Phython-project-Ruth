import requests
import info  # Store my Edamam API credentials in info. Extract the information of the API KEY and API ID for privacy.

class RecipeMaker:
    def __init__(self): #initializes the API ID and API Key.
        self.api_id = info.API_ID
        self.api_key = info.API_KEY

    def get_recipe(self, ingredients):
        url = f'https://api.edamam.com/search?q={",".join(ingredients)}&app_id={self.api_id}&app_key={self.api_key}'
        response = requests.get(url)  # Make a GET request to the Edamam API
        data = response.json()  # response as JSON

        # Check if a recipe is found
        if 'hits' in data and data['hits']:
            # Retrieve recipe, total cooking time, and URL
            recipe = data['hits'][0]['recipe']
            label = recipe['label']
            time = recipe['totalTime']
            url = recipe['url']

            # Display the recipe information to the user
            print(f"Recipe: {label}")
            print(f"Total Cooking Time: {time} minutes")
            print(f"URL: {url}")
        else:
            print("No recipe found for the given ingredients.")

    def run(self):
        while True:
            ingredients = input("Enter the ingredients you have (comma-separated): ").split(",")
            self.get_recipe(ingredients)

            retry = input("Do you want to try again? (Y/N): ") #gives the option to the user to introduce again ingredients or end.
            if retry.upper() != "Y":
                print("Thanks for choosing Cook-Eat-App.")
                break

if __name__ == '__main__':
    recipe_maker = RecipeMaker()
    recipe_maker.run()