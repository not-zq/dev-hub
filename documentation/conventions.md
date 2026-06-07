
# Conventions

## Git - Commit message

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

## Python - Paths

*Note*: In this documentation, for Python variables we use `snake_case`.

Considering the path `C:\Projects\<project>\output\result.csv`, these are its components:

- `working_directory` or `cwd`: `C:\Projects\<project>`
- `file_path` or `path`:
    - `absolute_file_path`: `C:\Projects\<project>\output\result.csv`
    - `relative_file_path`: `output\result.csv`
- `directory_name`: `output`
- `file_name`: composed of `file_stem` and `file_extesion`
- `file`: Open file in Python

In Python, using `file_path = Pathlib.Path(file_path)` is adviced to maintain paths as `Path` objects instead of `str`.
