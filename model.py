import random

def generate_pet_names(image_path, gender, style):
    # Listas de nombres según género y estilo
    funny_names_male = ["Chistorra", "Firulais", "Bigotes", "Salchicha"]
    funny_names_female = ["Doña Pelos", "Chispa", "Galleta", "Chiquita"]
    
    cute_names_male = ["Peluchín", "Bobby", "Coco", "Max"]
    cute_names_female = ["Luna", "Mimi", "Nina", "Bella"]
    
    tough_names_male = ["Thor", "Rex", "Bruno", "Rocky"]
    tough_names_female = ["Xena", "Sombra", "Electra", "Atenea"]

    # Seleccionar lista adecuada según género y estilo
    if gender == "male":
        if style == "funny":
            names_list = funny_names_male
        elif style == "cute":
            names_list = cute_names_male
        elif style == "tough":
            names_list = tough_names_male
        else:
            names_list = funny_names_male + cute_names_male + tough_names_male  # Default
    else:  # gender == "female"
        if style == "funny":
            names_list = funny_names_female
        elif style == "cute":
            names_list = cute_names_female
        elif style == "tough":
            names_list = tough_names_female
        else:
            names_list = funny_names_female + cute_names_female + tough_names_female  # Default
    
    # Seleccionar 3 nombres aleatorios
    return random.sample(names_list, 3)

