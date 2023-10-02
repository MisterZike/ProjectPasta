import ast
from src.llm.chat_bot import ChatBot
from src.data.data_interface import DataInterface


class AppLogic:
    def __init__(self):
        self.bot = ChatBot()
        self.data_interface = DataInterface()

    def dish_lookup(self, dish_name: str, unit_of_measure: str, serving_size: str):

        recipe_prompt = f"""What are the ingredients and quantities needed for a 
                            common {dish_name} recipe in {unit_of_measure} units
                            for {serving_size} people"""

        response = self.bot.predict(recipe_prompt)
        return response

    def list_ingredients(self, recipe: str):
        prompt = f"""From this recipe: {recipe}, list brief descriptions of the ingredients required. Like the size,
                     fresh or processed, size, etc.
                     
                     Only return a python list without any other text so that it can be parsed by ast.literal_eval().
                     For example, ['fresh prawns', 'loose garlic', 'eggs', 'bean sprouts', 'firm tofu']
                    """
        list_representation = self.bot.predict(prompt)
        list_of_ingredients = ast.literal_eval(list_representation)
        return list_of_ingredients

    def query_db(self, ingredient_list):
        df = self.data_interface.query_database(index_name='coles-data', queries=ingredient_list)
        return df

    def upsert_data(self, fp):
        self.data_interface.upsert_coles_data(file_path=fp, index_name='coles-data')


if __name__ == '__main__':
    # Run this to create the database
    app = AppLogic()
    app.upsert_data(fp='../data/coles.json')
