# Commitment Issues
## Challenge Overview
I accidentally wrote the flag down. Good thing I deleted it!

## Hints:
1. Version control can help you recover files if you change or lose them!
2. Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)
3. You can 'checkout' commits to see the files inside them


Challenge link: https://learn.cylabacademy.org/library/411?page=6
<img width="1004" height="686" alt="image" src="https://github.com/user-attachments/assets/c2a701c8-8d27-41c0-bd3f-c5439c791c1f" />

## Solutions
Based on the challenge description, the flag inside the text file was deleted. We can recover the previous version of the file using Git history to retrieve the flag
Do this command to see the commit history:

```bash
git log --oneline
```
We will see the commit history along with its SHA-1.
<img width="1642" height="197" alt="image" src="https://github.com/user-attachments/assets/7a19ca2e-cb3d-4ce2-a8a8-398c93a1e230" />

From the log, we can see a commit titled "create flag" with the SHA hash 6603cb4. To inspect the files at that specific point in time, we can checkout to that commit:
```bash
git checkout 6603cb4
```

After checking out, the message.txt file will be restored to its previous state containing the flag.
<img width="364" height="154" alt="image" src="https://github.com/user-attachments/assets/ed2b8619-79fe-47af-be0a-86a706889672" />

Flag: `picoCTF{s@n1t1z3_9539be6b}`
