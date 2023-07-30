from datetime import datetime 
"""
def calculate_age():
    input_year = input('enter ur birth year')
    age = datetime.today().year - int(input_year)

    bissextile = age // 4
    ageInDays = age *365 + bissextile
    ageInWeeks = age * 52
    ageInMonth = age * 12
    print(f' you have {ageInDays} days , {ageInMonth} Months , {ageInWeeks} weeks , {age} in years')
"""



# def str_manipilation():
#     str = input(' enter a string : ')
#     word_list = str.split(' ')
#     print(f'number of words : {len(word_list)}')
#     print('liste de words : ',word_list)

#     vowel = ['aeuio']
#     vowel_count = 0
#     for i in vowel:
#          vowel_count += str.lower().count(i)

#     print(f'number of vowels in the string : {vowel_count}')

#     lettre_count = {}
#     for i in str:
#         if i.isalpha():
#             if i in lettre_count.keys():
#                 lettre_count[i] +=1
#             else:
#                 lettre_count[i] = 1
#     print(lettre_count)

#     letter = input(' enter a letter to search :')
#     if str.count(letter) > 0:
#         print(f'the letter {letter} is present at {str.find(letter)}')
#     else:
#         print(f'the letter {letter} dosent exist')

#     word = input('entre a word to search : ')
#     if str.count(word) > 0:
#         print(f'the word {word} is at {str.find(word)} in the string')
#     else:
#         print(f'th eword {word} dosent exist in the string')


def gestion_list():
    wrd_list = []
    while True:
        stdin = input('enter a word : ')
        if stdin.lower() == 'stop':
            break
        elif stdin.lower() == 'tableau':
            print(wrd_list[::])
        else:
            if wrd_list.count(stdin) > 0:
                wrd_list.remove(stdin)
            else:
                wrd_list.append(stdin)
    print('thanks for using our service!')
# we calculate_age()

# str_manipilation()

gestion_list()