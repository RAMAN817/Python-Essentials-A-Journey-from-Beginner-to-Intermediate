for i in range(1, 23):
    with open("hello.txt", "a") as file:
        file.write(f'<a href="chapter{i}.html" style="display: block;">Chapter {i}: </a>\n')

