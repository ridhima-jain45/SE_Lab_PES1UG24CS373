# Lab 5 – Static Code Analysis

## Issues Identified and Fixed

| No. | Issue | Type | Tool | Original Line | Description | Fix Applied |
|---|---|---|---|---|---|---|
| 1 | Mutable default argument | Bug | Pylint | 9 | Using `system_logs=[]` causes the same list to be shared across function calls. | Changed default to `None` and initialized a new list inside the function. |
| 2 | Bare exception | Code quality | Pylint / Flake8 / Bandit | 21 | A bare `except` catches all exceptions and hides unexpected errors. | Replaced with `except (KeyError, ValueError)` and returned False. |
| 3 | MD5 hashing | Security | Bandit | 25 | MD5 is cryptographically weak and vulnerable to collision attacks. | Replaced MD5 with SHA-256. |
| 4 | Insecure file permissions | Security | Bandit | 55 | Permission `0o777` allows everyone extensive access to the file on POSIX systems. | Changed permissions to `0o600`. |
| 5 | Unclosed files | Code quality | Pylint | 28, 33 | Files were opened without being explicitly closed. | Used `with open()` to manage file resources. |
| 6 | Missing encoding | Code quality | Pylint | 28, 33 | File operations did not specify an encoding. | Added `encoding="utf-8"`. |
| 7 | Missing docstrings | Code quality | Pylint | Multiple | Functions and module lacked documentation. | Added module and function docstrings. |
| 8 | Formatting violations | Style | Flake8 | Multiple | Missing blank lines and lines exceeding the recommended length. | Reformatted the code according to PEP 8. |
| 9 | Old string formatting | Code quality | Pylint | 12, 15 | Used `%` formatting instead of modern f-strings. | Replaced with f-strings. |
| 10 | Global statement | Code quality | Pylint | 32 | The loading function modified global state using `global`. | Used `SHOWS.clear()` and `SHOWS.update()` instead. |

## Conclusion

Static code analysis helped identify bugs, security vulnerabilities, and style violations without executing the program. Pylint improved code quality, Bandit identified security risks, and Flake8 helped enforce consistent Python formatting.

The identified issues were corrected and the program was reanalysed to verify the improvements.
