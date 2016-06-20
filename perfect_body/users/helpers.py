import requests
# from .models import Food, HealthLabel, DietLabel, BaseUser
# from perfect_body.users.models import BaseUser
FOOD_CHOICES = []


# def crawl_food(food_name, food_meal_time):
#     payload = {'app_id': '10a834bf', 'app_key': '60a214d2bced63520a7dc3e77f7557f4', 'ingr': food_name}
#     r = requests.get('https://api.edamam.com/api/nutrition-data', params=payload)
#     # if r.status_code != 200:
#     #     raise "Request failed!"
#     result = r.json()
#     # if 'parsed' not in result['ingredients'][0].keys():
#     #     raise "Food not found"
#     food_parsed_name = result['ingredients'][0]['parsed'][0]['foodMatch']
#     food_weight = result['ingredients'][0]['parsed'][0]['weight']
#     food_quantity = result['ingredients'][0]['parsed'][0]['quantity']
#     food_calories = result['calories']

#     if 'PROCNT' not in result['ingredients'][0]['parsed'][0]['nutrients']:
#         food_protein_in_grams = 0.0
#     else:
#         food_protein_in_grams = result['ingredients'][0][
#             'parsed'][0]['nutrients']['PROCNT']['quantity']
#         food_protein_in_grams = round(food_protein_in_grams, 2)
#     if 'PROCNT' not in result['ingredients'][0]['parsed'][0]['nutrients']:
#         food_fat_in_grams = 0.0
#     else:
#         food_fat_in_grams = result['ingredients'][0][
#             'parsed'][0]['nutrients']['FAT']['quantity']
#         food_fat_in_grams = round(food_fat_in_grams, 2)
#     if 'CHOCDF' not in result['ingredients'][0]['parsed'][0]['nutrients']:
#         food_carbohydrate_in_grams = 0.0
#     else:
#         food_carbohydrate_in_grams = result['ingredients'][
#             0]['parsed'][0]['nutrients']['CHOCDF']['quantity']
#         food_carbohydrate_in_grams = round(food_carbohydrate_in_grams, 2)

#     health_label = result['healthLabels']
#     diet_label = result['dietLabels']

#     health_objects = []
#     diet_objects = []

#     for diet_tag in diet_label:
#         if not DietLabel.objects.filter(tag=diet_tag):
#             obj = DietLabel.objects.create(tag=diet_tag)
#             diet_objects.append(obj)

#     for health_tag in health_label:
#         if not HealthLabel.objects.filter(tag=health_tag):
#             obj = HealthLabel.objects.create(tag=health_tag)
#             health_objects.append(obj)

#     if not Food.objects.filter(name=food_parsed_name):
#         food = Food.objects.create(
#             name=food_parsed_name,
#             weight=food_weight,
#             quantity=food_quantity,
#             calories=food_calories,
#             protein_in_grams=food_protein_in_grams,
#             fat_in_grams=food_fat_in_grams,
#             carbohydrate_in_grams=food_carbohydrate_in_grams,
#             meal_time=food_meal_time,
#         )

#         for health_obj in health_objects:
#             food.health_label.add(health_obj)
#             food.save()

#         for diet_obj in diet_objects:
#             food.diet_label.add(diet_obj)
#             food.save()


# def get_user_post_attr(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     gender = request.POST.get('gender')
#     years = request.POST.get('years')
#     weight = request.POST.get('weight')
#     height = request.POST.get('height')

#     return name, email, password, gender, years, weight, height


# def get_cls_get_attr(cls, request):
#     for field in cls.objects.all():
#         name = field.name
#         email = field.email
#         password = field.password
#         gender = field.gender
#         years = field.years
#         weight = field.weight
#         height = field.height
#         BMI = field.BMI
#         max_cal = field.max_cal

#     return name, email, password, gender, years, weight, height, BMI, max_cal


# NORMAL_BMI = {
#     (19, 24): (19, 24),
#     (25, 34): (20, 25),
#     (35, 44): (21, 26),
#     (45, 54): (22, 27),
#     (55, 64): (23, 28),
#     (65, 100): (24, 29),
# }


# def calculate_normal_BMI(years, bmi):
#     for value in NORMAL_BMI.keys():
#         current_bmi = NORMAL_BMI[value]
#         if years >= value[0] and years <= value[1]\
#            and bmi >= current_bmi[0] and bmi <= current_bmi[1]:
#             return 'Your BMI is normal.'
#         else:
#             return 'Your BMI is not normal. Normal BMI is between {} and {}.'\
#                 .format(current_bmi[0], current_bmi[1])


def max_calories(height, weight, years, gender):

    max_cal = 0

    if gender == 'm':
        max_cal = 66 + (13.7 * weight) + (5 * height) - (6.8 * years)

    else:
        max_cal = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * years)

    return max_cal
