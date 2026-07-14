# Blame Game
## Challenge Overview
Someone's commits seems to be preventing the program from working. Who is it?

## Hints
1. In collaborative projects, many users can make many changes. How can you see the changes within one file?
2. Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)
3. You can use python3 <file>.py to try running the code, though you won't need to for this challenge.

Challenge link: https://learn.cylabacademy.org/library/405?page=6

<img width="910" height="713" alt="image" src="https://github.com/user-attachments/assets/1e063926-bbd1-4e31-a598-9d9f54fef959" />

## Solutions
To see who has changed the github file, we can use this command:
```bash
git blame message.py
```

and we will gain the flag: `picoCTF{@sk_th3_1nt3rn_81e716ff}`

<img width="1643" height="403" alt="image" src="https://github.com/user-attachments/assets/52440a20-3040-415e-82b6-7ebec67dcbaf" />

