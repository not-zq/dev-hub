
# Guide for software installation

### Considerations

- It is suggested that programs are installed in a separate memorable folder, like `C:\Programs`, within a folder with a generic name.
- `Path` refers to the variable in the **User variables** within the  **Environment variables**. 

## Git

### Installation

- [Click here](https://git-scm.com/install/windows) and download the installer for the latest Git version for Windows.
- Open the installer and use the installer suggested options.
    - **Suggestion**: Install on `C:\Programs\Git`.
- Ensure the following values are in `Path`:
    - `C:\Programs\Git\bin`
    - `C:\Programs\Git\cmd`

### Check installation

In a Terminal, running `git --version` should return
```bash
git version 2.54.0.windows.1
```

## Python

### Installation

- [Click here](https://www.python.org/downloads/) and download the standalone installer for the desired version.
- Run the installer as administrator.
    - Check the box for **Add python.exe to PATH**.
    - Select **Customize installation**
        - Only *pip* is needed from *Optional Features*
        - **Suggestion**: Install on `C:\Programs\Python\<version>`. For example, `C:\Programs\Python\3.14.5`.
- Ensure the following values are in `Path`:
    - `C:\Programs\Python\<version>\`
    - `C:\Programs\Python\<version>\Scripts\`
- On Windows, in `Settings > Apps > Advanced app settings > App execution aliases` disable `App Installer` for `python.exe` and `python3.exe`.

### Check installation

In a Terminal, running `pip --version` should return
```bash
pip 26.1.1 from C:\Programs\Python\3.14.5\Lib\site-packages\pip (python 3.14)
```

### Optional

- For **VS Code** integration, install the `Python` extension.

## Visual Studio Code

- Download and install [Visual Studio Code](https://code.visualstudio.com/Download).

## MiKTeX and Strawberry Perl for LaTeX

- Download and install [MiKTeX](https://miktex.org/download) in `C:\Programs\MiKTeX`.
- Download and install [Strawberry Perl](https://strawberryperl.com/) in `C:\Programs\Strawberry`.
- Check the following values are in `Path`:
    - `C:\Programs\Strawberry\c\bin`
    - `C:\Programs\Strawberry\perl\bin`
    - `C:\Programs\Strawberry\perl\site\bin`
- For **VS Code** integration, install the `LaTeX Workshop` extension.
