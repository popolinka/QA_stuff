import requests
import time

url = "https://api.dev.kitchenstories.io/api"

"""
Login with a user
"""

headers = {
    'Content-Type': 'application/json'
}

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1bHRyb24iLCJ1c2VyIjoiNGUwMmQ2NDAtMWZhYS00MTZmLWIyYTAtZmJjMWU1MDI2NDJkIn0.C9ZIXK2gYg4XxNBnNIkcnaOOq7N46r11uKycoUy17Fg"
# get it from Postman

headers['Authorization'] = "Bearer {}".format(token)  # "Bearer" redundant
headers['Accept-language'] = "en"

'''
get external recipes
'''

urlExternalRecipe = url + "/users/me/external-recipe-preview/?url={}"

with open('/Users/orkunkadioglu/PycharmProjects/recipeLinkCrawler/kochBar_links.txt') as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

notParsebleRecipes = []
for count, x in enumerate(lines):
    r = requests.get(urlExternalRecipe.format(x), headers=headers)
    if "errors" in r.json():
        message = " | the error is: {}".format(r.json()["errors"])
        notParsebleRecipes.append(x[:len(x) - 1] + message) #+ "the error is: " + r.json["errors"])

    if (count + 1) % 10 == 0:  # enumerate starts counting from 0
        print(str(count + 1) + " out of " + str(len(lines)) + " are complete")
    time.sleep(0.7)

with open('notParsableRecipeLinks.txt', 'w+') as f:
    for recipes in notParsebleRecipes:
        f.write('%s\n' % recipes)
