
# Development workflow

## Git

Whenever the files from our project change, their changes will be tracked by git. This changes can be files being modified, created, or removed. Which all happen locally, but for them to be applied to the remote version of our project we have to stage, commit and push them. We can see the current status of our changes with
```bash
git status
```

### Staging changes

In first instance, we make modifications to our files and our status will show them as unstaged changes or untracked files if we created a new file. To stage changes or start tracking files we use
```bash
git add <file-name>
```

If we want to change the name of a file, and not make our repository think we deleted one file and created a different one, we run
```bash
git mv <old-file-name> <new-file-name>
```

### Commit and push changes

After staging all wanted changes we add a commit them with a message using 
```bash
git commit -m "<commit-message>"
```
and, finally, to push them to the remote repository we use
```bash
git push -u origin main
```
