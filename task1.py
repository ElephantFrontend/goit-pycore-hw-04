
file_path = 'salaries.txt'
data = """Alex Korp,3000
    Nikita Borisenko,2000
    Sitarama Raju,1000"""
    
with open(file_path, 'w') as file:
    file.write(data)

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary_str = line.split(',')
                salary = int(salary_str)

                total += salary
                count += 1
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
        return (0, 0)
    except ValueError:
        print(f"There is an error in data format in the file {path}.")
        return (0, 0)

    average = total / count if count != 0 else 0

    return total, average

total, average = total_salary(file_path)
print(f"Загальна сума зарплат: {total}")
print(f"Середня зарплата: {average}")