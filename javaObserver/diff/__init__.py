import git
from git.diff import DiffIndex
from javalang.tree import MethodDeclaration
from javaObserver.log import logger
import difflib

defaultBranch = 'master'


class RepoDiff:
    def __init__(self, repoPath, aBranchName=defaultBranch, bBranchName=None):
        self.repo = git.repo.Repo(repoPath)
        self.aBranch: git.repo.base.Reference = self._with_branch(aBranchName)
        self.bBranch: git.repo.base.Reference = self._with_branch(bBranchName)

    @property
    def diffIndex(self):
        """基于a分支-对比b分支
        通常aBranchName=master，bBranchName=当前开发分支
        """
        assert self.aBranch and self.bBranch
        return self.aBranch.commit.diff(self.bBranch.commit)

    def _with_branch(self, branchName):
        refs = self.repo.references
        for branch in refs:
            if branch.name == branchName:
                logger.info(f'find branch {branchName}')
                return branch
        logger.warn(f"{branchName} not find")
        return None

    def diffBranch(self):
        for df in self.diffIndex:
            print('*' * 100)
            print(df.a_path)
            acontent = df.a_blob.data_stream.read().decode('u8')
            bcontent = df.b_blob.data_stream.read().decode('u8')

            oneContent = ''
            start = None
            end = None
            for diff in difflib.unified_diff(acontent.split('\n'), bcontent.split('\n')):
                oneContent += diff + '\n'
            spC = oneContent.split("@@")[1:]
            for c in range(0, len(spC), 2):
                print(spC[c], self.parseDiffPosition(spC[c]))

    @staticmethod
    def parseDiffPosition(diff: str):
        a, b, c, d = 0, 0, 0, 0
        z = diff.strip().split(' ')
        z0 = z[0]
        z1 = z[1]
        if z0.startswith('-'):
            a, b = z0.replace('-', '').split(',')
        if z1.startswith('+'):
            c, d = z1.replace('+', '').split(',')

        return int(a), int(c)


if __name__ == '__main__':
    rd = RepoDiff('', defaultBranch, '')
    rd.diffBranch()
