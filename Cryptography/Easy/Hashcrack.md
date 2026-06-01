# PicoCTF: hashcrack

We are given a challenge that requires us to crack multiple cryptographic hashes 
in succession via a remote server. The goal is to identify the hash types based 
on their characteristics, perform a dictionary attack. In this challenge, I'm using John the Ripper (JtR), 
and submit the correct plaintext passwords to retrieve the final flag.  
Link: https://learn.cylabacademy.org/library/475?page=3&workspace=true 

<img width="503" height="381" alt="image" src="https://github.com/user-attachments/assets/0c8cdfe1-33c8-45a4-b776-0c894c5bc8c7" />

---

## Solution

### 1. Analyze and crack the first hash (MD5)
The server prompts us with the first hash. Based on its 32-character length and hexadecimal format, it is identified as an MD5 hash.
Open a new terminal tab to keep the challenge session active. Save the hash into a file and extract the rockyou.txt wordlist if it hasn't been unzipped yet:
Launch the instance on PicoCTF and copy the provided netcat (`nc`) command. Connect to the remote server using the terminal:

```bash
echo "[first_hash_here]" > hash.txt
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

```
Run John the Ripper with the raw-md5 format:

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
The tool successfully cracks the hash and returns the password: `password123`
