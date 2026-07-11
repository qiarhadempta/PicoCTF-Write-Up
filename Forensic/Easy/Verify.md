# Verify
## Challenge Overview
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

## Hints
1. Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.
2. You can create a SHA checksum of a file with sha256sum <file> or all files in a directory with sha256sum <directory>/*.
3. Remember you can pipe the output of one command to another with |. Try practicing with the 'First Grep' challenge if you're stuck!

Challenge link: https://learn.cylabacademy.org/library/450?page=5&workspace=true
<img width="1376" height="567" alt="image" src="https://github.com/user-attachments/assets/5ac19b2f-724b-48f3-8672-b2119e325c10" />

## Solutions
Once we are logged in via SSH, we have to find the file with the same SHA256 value with our given SHA with this specific command:
```bash
sha256sum files/* | grep [insert your SHA here]
```

And we will get the file name with the same hash value: `files/8eee7195`
<img width="1714" height="123" alt="image" src="https://github.com/user-attachments/assets/f343998d-d799-445f-a635-7e348ce9ab32" />

The next thing we gotta do is decrypt the file, so we are be able to read the file:
```bash
./decrypt.sh files/8eee7195
```

<img width="696" height="67" alt="image" src="https://github.com/user-attachments/assets/9b849894-7e7b-4217-ab30-5baa638f4ae6" />

Flag: `picoCTF{trust_but_verify_8eee7195}`
