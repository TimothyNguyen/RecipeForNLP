import pickle
import csv

with open('archive/ingr_map.pkl', 'rb') as ingredient_map:
    df = pickle.load(ingredient_map)

print([col for col in df.columns])

for row in range(5):
    print(df.loc[[row]].values.tolist())

ingredient_dictionary = {}

for index, row in df.iterrows():
    # print(row['replaced'], row['id'])
    ingredient_dictionary[row['id']] = row['replaced']

# print(ingredient_dictionary)

recipe_list = []

longest_list = 0

with open('archive/PP_recipes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    current_line = 0
    for row in csv_reader:
        if current_line == 0:
            print(", ".join(row))
        else:
            string_list = row[7][1:-1]
            ingredient_list = [ingredient_dictionary[int(ingr_id)] for ingr_id in string_list.split(", ")]
            recipe_list.append(ingredient_list)
            longest_list = max(longest_list, len(ingredient_list))
        current_line += 1

print("The longest recipe has", longest_list, "ingredients.")
print("There are", len(recipe_list), "recipes.")
print("Saving recipe bows as a pickle file...")
with open('recipe_ingredient_bows.pkl', 'wb') as f:
    pickle.dump(recipe_list, f)
print("Saved recipe ingredient bows to recipe_ingredient_bows.pkl")