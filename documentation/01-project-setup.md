
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
git add .gitignore
git commit -m "Added README.md and .gitignore."
git push -u origin main
```

## Python environment

### Create the base environment

In a terminal, in the project's folder, to create a local environment for the project, run

```bash
python -m venv .venv
```

To link this new environment to the current **VS Code** workspace, we use the shortcut `Ctrl + Shift + P` and find the command `Python: Select Interpreter`. After running this command, we select our local environment interpreter `./.venv/Scripts/python.exe` for the workspace. 

Now, for python files, our local environment is selected as the interpreter, having the necessary packages. To manually activate the environment in a terminal we run

```bash
.venv/Scripts/activate
```

### Install packages

To install packages you can run `pip install <package>`.
However, it is better practice to set a `requirements.txt` file with the needed packages to keep track of the installed packages and for other to be able to recreate the same environment. The content for the `requirements.txt` file should look like following
```
pandas
pyodbc==5.3.0
matplotlib
pyyaml
```
where you can specify the version of the package. 

Having this file set up with the necessary packages, to install them you would instead run
```bash
python -m pip install -r requirements.txt
```
and to confirm the installation, you would run
```bash
python -m pip list
```
