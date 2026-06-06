
# Installation guide for essential software

### Considerations and recommendations

- `Path` refers to the variable in **User variables** within the  **Environment variables**. 
- It is suggested that programs are installed in `C:\Programs`.

## Git

- [Click here](https://git-scm.com/install/windows) and download the installer for the latest Git version for Windows.
- Open the installer and use the installer suggested options.
    - **Suggestion**: Install in `C:\Programs\Git`.
- Ensure the following values are included in `Path`:
    - `C:\Programs\Git\bin`
    - `C:\Programs\Git\cmd`
- To confirm the installation, running `git --version` in a terminal should return
```bash
git version 2.54.0.windows.1
```

## Python

- [Click here](https://www.python.org/downloads/) and download the standalone installer for the desired version.
- Run the installer as administrator.
    - Check the box **Add python.exe to PATH**.
    - Select **Customize installation**
        - Only *pip* is necessary in **Optional Features**
        - **Suggestion**: Install on `C:\Programs\Python\<version>`. For example, `C:\Programs\Python\3.14.5`.
- Ensure the following values are included in `Path`:
    - `C:\Programs\Python\<version>\`
    - `C:\Programs\Python\<version>\Scripts\`
- On Windows, in `Settings > Apps > Advanced app settings > App execution aliases` disable `App Installer` for `python.exe` and `python3.exe`.
- To confirm correct installation, running `pip --version` in a terminal should return something similar to
```bash
pip 26.1.1 from C:\Programs\Python\3.14.5\Lib\site-packages\pip (python 3.14)
```
- For **VS Code** integration, install the `Python` extension.

## Visual Studio Code

- Download and install [Visual Studio Code](https://code.visualstudio.com/Download).

## SQL Server Management Studio

- Download and install [SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/install/install).

## MiKTeX and Strawberry Perl for LaTeX

- Download and install [MiKTeX](https://miktex.org/download) in `C:\Programs\MiKTeX`.
- Download and install [Strawberry Perl](https://strawberryperl.com/) in `C:\Programs\Strawberry`.
- Check the following values are in `Path`:
    - `C:\Programs\Strawberry\c\bin`
    - `C:\Programs\Strawberry\perl\bin`
    - `C:\Programs\Strawberry\perl\site\bin`
- For **VS Code** integration, install the `LaTeX Workshop` extension.
