from pandas import DataFrame, Series
import pandas as pd



# Top 10 most occurring ingredients
def get_ingredients(data):
    """This function gets a dataframe o series of lists and returns all the
    ingredients that appear in the object - NOT UNIQUE ingredients"""
    all_ingredients = []
    for i in range(len(data)):
        if isinstance(data, pd.core.frame.DataFrame):
            all_ingredients.extend(data.loc[i, 'ingredients'])
        else:
            all_ingredients.extend(data.iloc[i])
    return Series(all_ingredients)




def count_occ(group):
    """ This function gets a list and counts how many times each
     item appears"""
    return dict(Series(group).value_counts())



# Get unique ingredients by cuisine
def remove_duplicates(value):
    """This function get a list and removes duplicates"""
    return list(set(value))



def check_for_ingredient(my_dict, ingredient):
    """This function gets a series or a dict and an ingredient and
    returns how many times it occurs in each cuisine"""
    result = {}
    for cuisine, list_ingredients in my_dict.items():
        if ingredient in list_ingredients:
            result[cuisine] = list_ingredients[ingredient]
    return result




# Number of times each ingredient appear in a cuisine
def number_cuisine_per_ingredient(unique):
    """Get a list of ingredients and returns their occurrence in each cuisine"""
    cuisines_count_per_ingredient = Series()
    for ingredient in unique:
        cuisines_count_per_ingredient.loc[ingredient] = check_for_ingredient(all_ingredient_by_cuisine_count, ingredient)
    return cuisines_count_per_ingredient


# Extract cuisines from a dict
def extract_cuisine(my_series):
    '''Extract cuisines from a dict '''
    return list(my_series.keys())



def get_common_ingredients(data):
    """gets a dict with unique ingredients per cuisine and returns common
    ingredients across all cuisines"""
    common = set(data.loc[data.index[0]])
    for cuisine in data.index[1:]:
        next_cuisine = set(data.loc[cuisine])
        common.intersection_update(next_cuisine)
    return list(common)


#Remove ingredients from a list of ingredients
def remove_ingredients(series, remove):
    """Remove ingredients from a list of ingredients"""
    return list(set(series) - set(remove))


#Checks the recipes that contain same name ingredient
def has_same_name_ingredient(data, special_ingredients):
    """Checks recipes that contain same name ingredients"""
    result = Series(data).isin(Series(special_ingredients))
    return any(result)




# Remove ingredients and zero ingredient recipes from a table
def remove_ingredients_from_table(df, ingredients_to_remove):
    """Remove ingredients and zero ingredient recipes from a table"""
    new_df = df.copy()
    # Removes common ingredients from DataFrame
    new_df.loc[:, 'ingredients'] = new_df.loc[:, 'ingredients'].apply(remove_ingredients, remove=ingredients_to_remove)
    new_df.loc[:, 'size_recipe'] = new_df.loc[:, 'ingredients'].apply(len)

    # Checks for zero ingredient recipes to remove
    if any(new_df['size_recipe'] == 0):
        # Removes zero ingredient recipes from DataFrame
        new_df = new_df[new_df['size_recipe'] != 0]
        new_df.reset_index(drop=True, inplace=True)

    return new_df




# Method to remove ingredients and zero ingredient recipes
def remove_ingredients_from_table_dummified(df, ingredients_to_remove, drop_rows=True):
    # Remove ingredients from columns
    df = df.loc[:, ~df.columns.isin(ingredients_to_remove)]

    # Update size_recipe
    df.loc[:, 'size_recipe'] = df.iloc[:, 4:].sum(axis=1)

    # Remove zero ingredient recipes left after removing common ingredients
    if drop_rows:
        df = df[df['size_recipe'] != 0]
        return df
    else:
        return df


# Get list of ingredients from dummies
"""Get list of ingredients from dummies"""
def get_ingredients_dummified(my_series):
    return list(my_series[my_series == 1].index)


# Gets a series and check if at least one ingredient of the list_ingredient is present and return a boolean
def check_recipe_contain_ingredient(my_series, ingredients):
    """Gets a series and check if at least one ingredient
    of the list_ingredient is present and return a boolean"""
    index = my_series.index.isin(ingredients)
    return any(my_series[index])



def keep_recipes_contain_list_ingredients(df, ingredients, n):

    index = df.apply(check_recipe_contain_ingredient, ingredients=ingredients, axis=1)
    if len(index) > 1:
        df_left = df.iloc[:, :n]
        dummies = df.iloc[:, n + 1:]

        df_left['ingredients'] = dummies.apply(get_ingredients_dummified, axis=1)

        df_left = df_left[index]

        dummies = dummify_ingredients(df_left)

        new_df = (df_left.drop(columns=['ingredients'])).join(dummies)

        return new_df

    else:
        print("There are no recipes that meet the ingredient criteria")




# Dummifies a list of ingredients
def dummify_ingredients(df):
    """Dummifies a list of ingredients"""
    from sklearn.preprocessing import MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    dummies = DataFrame(mlb.fit_transform(df['ingredients']), columns=mlb.classes_, index=df.index)
    return dummies

























