import os
from javaObserver.model.inside import InsideTree


def loadAst(project: str):
    """
    :return: List[InsideTree]
    """
    asts = []
    for root, dirs, files in os.walk(project):
        for file in files:
            if file.endswith('.java'):
                filePath = os.path.join(root, file)
                asts.append(InsideTree(filePath))
    return asts


if __name__ == '__main__':
    pass
