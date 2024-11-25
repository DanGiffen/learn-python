#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as input_letter:
    letter = str(input_letter.read())

for name in names_list:
    new_name = name.strip("\n")
    rep_letter = letter.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as output_letter:
        output_letter.write(str(rep_letter))





