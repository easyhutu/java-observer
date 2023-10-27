from javaObserver.load import loadAst


def scanInfo(objPath: str):
    asts = loadAst(objPath)
    print(len(asts))



if __name__ == '__main__':
    scanInfo()
