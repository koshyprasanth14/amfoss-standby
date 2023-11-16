from pathlib import Path

def mad_libs(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    placeholders = []
    for word in content.split():
        if word.isupper() and(len(word))>1:
            placeholders.append(word)

    for placeholder in placeholders:
        replacement = input(f"Enter an {placeholder.lower()}: ") 
        content = content.replace(placeholder, replacement, 1)  

    print("\nModified Text:")
    print(content)

    
    with open(file_path, 'w') as new_file:
        new_file.write(content)

    print(f"\nResults saved to '{file_path}'.")

file_to_modify = Path('typee.txt')
file_to_modify = file_to_modify.resolve()
mad_libs(file_to_modify)
