# Aprire e leggere un file, in questo caso la modalità sata solo di lettura mode="r"
with open("my_file.txt") as file:
    contents= file.read()
    print (contents)

# Modificare un file aprendolo in modalita scrittura (write) mode="w"
# In questo caso se il file non esiste verrà automaticamente creato.
with open("new_file.txt",mode="w") as file:
    file.write("\nnew text")

# Aggiungere del testo con la funzione APPEND mode="a"
# Anche in questo caso se il file non esiste verrà automaticamente creato.
with open("car_file.txt",mode="a") as file:
    file.write("\nnew text")

