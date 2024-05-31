from django import template
register = template.Library()

# 사용자들이 매긴 칵테일 평점을 이미지로 보여준다.
@register.filter(name='grade_to_star_image')
def grade_to_star_image(grade):
    star_images=['Star-empty.png','Star-half.png','Star-full.png']
    stars = []
    
    # 정수 일때
    if grade % 1 == 0 : 
        stars.extend(['Star-full.png']* int(grade))

    #실수일 때
    if grade % 1 != 0:
        # 정수개수만큼 full_star 이미지를 리스트에 추가
        stars.extend(['Star-full.png']* int(grade/1))
        # half_star 이미지를 리스트에 추가
        stars.append('Star-half.png')
   

    stars.extend(['Star-empty.png'] * (5 - len(stars)))
    return stars

# 사용자들이 매긴 칵테일 평점의 평균을 계산한다.
@register.filter(name='calculate_average_grade')
def calculate_average_grade(comments):
    total_grade = 0
    count = 0
    for comment in comments:
        total_grade += comment.grade
        count += 1
    if count == 0:
        return 0

    return round(total_grade / count, 1)


# 가장 평균이 높은 post를 보여준다.
# @register.filter(name='find_highest_rated_cocktail')
# def find_highest_rated_cocktail(cocktails):
#     highest_rated_cocktail = None
#     highest_grade = 0

#     for cocktail in cocktails:
#         average_grade = calculate_average_grade(cocktail.comments)
#         if average_grade > highest_grade:
#             highest_grade = average_grade
#             highest_rated_cocktail = cocktail

#     return highest_rated_cocktail
