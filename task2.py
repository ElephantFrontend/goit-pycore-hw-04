file_path = 'cats.txt'
data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""
    
with open(file_path, 'w') as file:
    file.write(data)

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age_str = line.strip().split(',')
                age = int(age_str)

                cat_dict = {
                    "id": id,
                    "name": name,
                    "age": age
                }

                cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    except ValueError:
        print(f"Data format error in the file {path}.")

    return cats_info

cats_info = get_cats_info(file_path)
print(cats_info)