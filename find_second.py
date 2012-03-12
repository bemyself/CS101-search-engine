#Define a procedure, find_second, that takes
#two strings as its inputs: a search string
#and a target string. It should output a
#number that is the position of the second
#occurence of the target string in the
#search string.

#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace') => 25

def find_second(search_str, target_str):
    first = search_str.find(target_str)
    sec = search_str.find(target_str, first + 1)
    return sec

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
