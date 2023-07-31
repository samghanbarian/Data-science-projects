dicEleves = { 
	'titi' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne' }, 
	'toto' : {'notes' :{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' }, 
	'tata' : {'notes':{'tp1':15,'tp2':8,'tp3':13}, 'appréciation': 'Bonne' },
	'tutu' : {'notes':{'tp3':15,'tp4':13}, 'appréciation': 'Bonne' },
}

def add_std():
    std_name = input('enter the name of the new studnt :')
    dicEleves[std_name] ={'notes':{}, 'appréciation': '' }
    print(dicEleves)

def add_notes():
    while True:
        tp_note = input('Please enter the name of student, tp name, and its note seperated with space :')
        tblInput =tp_note.split()
        std_name = tblInput[0]
        tp_name = tblInput[1]
        tp_note = int(tblInput[2])

        if tp_note :
            if std_name in dicEleves:
                    
                dicEleves[std_name]['notes'][tp_name] = tp_note

            else :
                print('student dosent exist in the list!')
        else :
            break




def mod_appr():
     tp_note = input('Please enter the name of student and its evaluation to mdify seperated with space :')
        tblInput =tp_note.split()
        std_name = tblInput[0]
        std_appr = tblInput[1]
        dicEleves[std_name]['appréciation'] = std_appr


def list_std():
    for std in dicEleves:
        print(f'student_name : {std} , notes : {dicEleves[std]['notes'] }, appreciation : {dicEleves[std]['appréciation']}')


while True:
    stdin = input('please enter a command : ')

    match stdin:
        case 'add':
         add_std()

        case 'notes' :
         add_notes()

        case 'appr':
          mod_appr()

        case 'list' :
          list_std()

        case 'quitter':
         print('Thanks for using the app')
         break

        case _ :
         print('not valid entry!')
         