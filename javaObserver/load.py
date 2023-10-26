import javalang


def loadAst(filepath):
    """

    :return:
    """
    with open(filepath, encoding='u8') as f:
        data = f.read()
    # print(data)
    tree = javalang.parse.parse(data)
    for path, node in tree:
        print(path)
        print(node)
        print('-' * 100)
    return tree


if __name__ == '__main__':
    fileData = loadAst("")
