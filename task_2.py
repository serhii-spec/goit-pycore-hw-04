def get_cats_info(path):
    """Читає файл з котами (рядки «id,ім'я,вік»)
    і повертає список словників з ключами id, name, age."""
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Пропущено пошкоджений рядок: {line}")

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)