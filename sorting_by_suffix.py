"""Сортировка файлов по расширению"""



def sort_files():
    curr_path = pathlib.Path(os.getcwd())
    for file in curr_path.iterdir():
        try:
            file.replace(f"{file.suffix}/{file.name}")
        except FileNotFoundError:
            os.mkdir(file.suffix)
            file.replace(f"{file.suffix}/{file.name}")

sort_files()
