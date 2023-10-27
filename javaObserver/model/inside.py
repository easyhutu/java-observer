from javaObserver.model.javaFile import JavaFile
import javalang
from javalang.tree import CompilationUnit, ReferenceType, FormalParameter, MethodDeclaration, MethodInvocation


class InsideTree:
    def __init__(self, filepath):
        self.file = JavaFile(filepath)
        self._tree = None

    @property
    def tree(self) -> CompilationUnit:
        """
        :return: 当前文件的AST CompilationUnit
        """
        if self._tree:
            return self._tree
        tree = javalang.parse.parse(self.file.content)
        self._tree = tree
        return tree

    def with_method(self, methodName: str) -> CompilationUnit:
        for path, node in self.tree:
            if isinstance(node, MethodDeclaration):
                if methodName == node.name:
                    return path
    