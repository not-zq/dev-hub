
# Development workflow

## Git

Whenever the files from our project change, their changes will be tracked by git. This changes can be files being modified, created, or removed. Which all happen locally, but for them to be applied to the remote version of our project we have to stage, commit and push them. We can see the current status of our changes with
```powershell
git status
```

### Changes

If we want to move or rename a file, and not make our repository think we deleted one file and created a different one, we run
```powershell
git mv <old-file-name> <new-file-name>
```

### Staging

In first instance, we make modifications to our files and our status will show them as unstaged changes or untracked files if we created a new file. To stage modified files or start tracking new files we use
```powershell
git add <file-name>
```
or to stage everything
```powershell
git add .
```

### Commit

After staging all wanted changes, we commit them with a title and message using 
```powershell
git commit -m "<commit-title>" -m "<commit-message>"
```

A shortcut to automatically stage files that have been modified or deleted is `-all` / `-a`
```powershell
git commit -a -m "commit-message>"
```
This saves time having to add files, but this does not include untracked files. 

&emsp; Refer to [Conventions | Git - Commit messages](./conventions.md#git---commit-message) for guidelines on commit messages.

### Push

All commits happen locally and only affect the remote repository after they are pushed. 

To push commits we run
```powershell
git push origin main
```
However, if we are constantly pushing the branch `main` to `origin`, we can use `-u` as
```powershell
git push -u origin main
```
so that we can push `main` to `origin` only using
```powershell
git push
```

---

<br>

Some other commands that should be expanded on
```powershell
git checkout -b <new-branch>
git checkout main
git merge
git reset --soft / --mixed / --hard
git pull
```
