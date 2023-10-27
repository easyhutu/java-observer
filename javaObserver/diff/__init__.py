import git
from git.diff import DiffIndex


def diffWithBranch(repoPath, baseBranchName, diffBranchName) -> DiffIndex:
    """
    :param repoPath: 仓库目录
    :param baseBranchName:
    :param diffBranchName:
    :return:
    """
    repo = git.repo.Repo(repoPath)
    baseBranch = None
    diffBranch = None
    for branch in repo.references:
        if baseBranchName == branch.name:
            baseBranch = branch
        if diffBranchName == branch.name:
            diffBranch = branch
    assert baseBranch and diffBranch

    return diffBranch.commit.diff(baseBranch.commit)


if __name__ == '__main__':
    pass
