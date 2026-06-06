
# Setting up a new project

## GitHub repository

In [GitHub](https://github.com), create a repository for the project. 
This will create a web URL for the project, similar to `https://github.com/<user>/<project-name>.git`.

Locally, create a folder for the project and create `README.md` and `.gitignore` files. 
It is suggested to have projects in a common memorable place like `C:\Projects\<project-name>`.

To set the local repository and its connection to the remote repository, in a terminal, run

```bash
git init
git branch -M main
git remote add origin https://github.com/<user>/<project-name>.git
```

Then, to push your first commit, run

```bash
git add README.md
git commit -m "Added README.md"
git push -u origin main
```

## Python environment

In a terminal, in the project's folder, to create a local environment for the project, run

```bash
python -m venv .venv
```

To activate the environment

```bash
.venv/Scripts/activate
```

To install packages you can run `pip install <package>`.
However, it is better practice to set a `requirements.txt` file with the needed packages. The content of the file should like this

```
pandas
pyodbc
matplotlib
pyyaml
```

and you would run 

```bash
python -m pip install -r requirements.txt
```

