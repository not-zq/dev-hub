
# Development workflow

## Git

Whenever the files from our project change, their changes will be tracked by git. This changes can be files being modified, created, or removed. Which all happen locally, but for them to be applied to the remote version of our project we have to stage, commit and push them. We can see the current status of our changes with
```bash
git status
```

### Changes

If we want to move or rename a file, and not make our repository think we deleted one file and created a different one, we run
```bash
git mv <old-file-name> <new-file-name>
```

### Staging

In first instance, we make modifications to our files and our status will show them as unstaged changes or untracked files if we created a new file. To stage modified files or start tracking new files we use
```bash
git add <file-name>
```
or to stage everything
```bash
git add .
```

### Commit

After staging all wanted changes, we commit them with a title and message using 
```bash
git commit -m "<commit-title>" -m "<commit-message>"
```

A shortcut to automatically stage files that have been modified or deleted is `-all` / `-a`
```bash
git commit -a -m "commit-message>"
```
This saves time having to add files, but this does not include untracked files. 



When writing commit messages there is a convention called **Angular convention**, which provides a set or rules for creating a standardized commit history. This conventions sets the structure of a commit message as:
```
<type>(<optional scope>): <subject>
<BLANK LINE>
<optional body>
```
which is expanded upon in the [Commit Message Guidelines](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

The most relevant message *types* are
- `docs`: documentation changes only, 
- `feat`: new features,
- `fix`: bug fix,
- `perf`: code change that improves performance,
- `refactor`: code change that neither fizes a bug nor adds a feature,
- `style`: changes that do not affect the meaning of the code.

Some relevant guidelines are
- the **subject** is concise description of the change, where we
    - use the imperative, present tense: "change" not "changed" nor "changes",
    - do not capitalize the first letter, and
    - do not add a dot (.) at the end.
- the **body** should include the motivation for the change and contrast with previous behavior, and we also use the imperative, present tense.

### Push

All commits happen locally and only affect the remote repository after they are pushed. 

To push commits we run
```bash
git push origin main
```
However, if we are constantly pushing the branch `main` to `origin`, we can use `-u` as
```bash
git push -u origin main
```
so that we can push `main` to `origin` only using
```bash
git push
```

---

<br>

Some other commands that should be expanded on
```bash
git checkout -b <new-branch>
git checkout main
git merge
git reset --soft / --mixed / --hard
git pull
```
