#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as name_list:
    invited=name_list.readlines()
    for name in invited:
        correct_name=name.strip("\n")
        with open("./Input/Letters/starting_letter.txt",mode="r") as mail:
            corp=mail.read()
        new_corp=corp.replace("[name]",correct_name )
        with open(f"./Output/ReadyToSend/Letter_for_{correct_name}",mode="w") as definitive_mail:
            definitive_mail.write(f"{new_corp}")













#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp