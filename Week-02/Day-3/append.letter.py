# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs

verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(verb,preverb):
    for i in range(len(verbs)):  
        new_verbs = preverb + verbs[i]
        print(new_verbs)
        
create_new_verbs(verbs,preverb)

# def create_new_verbs(preverb):
#     for i in range(len(verbs)):
#         cc = preverb + verbs[i]
#         print(cc)

# create_new_verbs(preverb)