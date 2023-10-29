import git
from git.diff import DiffIndex
from javalang.tree import MethodDeclaration
from javaObserver.log import logger

defaultBranch = 'master'


class RepoDiff:
    def __init__(self, repoPath, aBranchName=defaultBranch, bBranchName=None):
        self.repo = git.repo.Repo(repoPath)
        self.aBranch: git.repo.base.Reference = self._with_branch(aBranchName)
        self.bBranch: git.repo.base.Reference = self._with_branch(bBranchName)

    @property
    def diffIndex(self):
        assert self.aBranch and self.bBranch
        return self.bBranch.commit.diff(self.aBranch.commit)

    def _with_branch(self, branchName):
        refs = self.repo.references
        for branch in refs:
            print(branch)
            if branch.name == branchName:
                logger.info(f'find branch {branchName}')
                return branch
        logger.warn(f"{branchName} not find")
        return None

    def diffBranch(self):
        for df in self.diffIndex:
            print('*' * 100)
            print(df.a_path)
            self._withDiffBlobData(df.a_blob.data_stream.read().decode('u8'), df.b_blob.data_stream.read().decode('u8'))

    @staticmethod
    def _withDiffBlobData(a: str, b: str):
        al = a.split('\n')
        bl = b.split('\n')
        index = 0
        while index < len(al) and index < len(bl):
            if al[index] != bl[index]:
                print(al[index])
                print(bl[index])
                print("-" * 100)
            index += 1


if __name__ == '__main__':
    rd = RepoDiff('', defaultBranch, '')
    rd.diffBranch()
