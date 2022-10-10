def biggestPath(x: dict) -> str:
    path = "/"
    for directory, cont in x.items():
        if isinstance(cont, dict):
            # Если вложенность больше, чем у предыдущего пути
            if len(tmp_path := f"/{directory}{'/'}{biggestPath(cont)}") > len(path):
                path = tmp_path
        else:
            # Убираем дублирующиеся имена файлов
            cont = [item for item in cont if cont.count(item) == 1]
            if cont:
                path += f"{directory}{'/'}{cont[0]}"
            else:
                path += "/"
    return path