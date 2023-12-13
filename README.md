created README

Task 1-2: mkdir lab1 cd lab1 git init git touch README git commit -a -m "created README"

Task 3: git branch first_branch git checkout first_branch // changes in README git worktree list git status git commit -a -m "rep: first changes in README"

Task 4: git checkout master // changes in README git commit -a -m "rep: second changes in README"
git log --oneline --graph --decorate=short --all