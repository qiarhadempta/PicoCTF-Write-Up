# PicoCTF: hashcrack

We are given a challenge that requires us to crack multiple cryptographic hashes 
in succession via a remote server. The goal is to identify the hash types based 
on their characteristics, perform a dictionary attack. In this challenge, I'm using John the Ripper (JtR), 
and submit the correct plaintext passwords to retrieve the final flag.  
Link: https://learn.cylabacademy.org/library/475?page=3&workspace=true 

<img width="1366" height="550" alt="image" src="https://github.com/user-attachments/assets/71ae9576-93a0-448e-8540-ff4110f81819" />

---

## Solution

### 1. Analyze and crack the first hash
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

### 2. Analyze and crack the second hash
Submit password123 back to the challenge terminal. The server accepts it but provides a second hash. This hash has a length of 40 characters, indicating it is a SHA-1 hash.

Save the new hash into hash2.txt and crack it using the raw-sha1 format:

```bash
echo "[second_hash_here]" > hash2.txt
john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt
```

The second password is found: `letmein`

### 3. Analyze and crack the third hash
Submit letmein to the server. We are given a final hash with a length of 64 characters, which corresponds to a SHA-256 hash.

Save it to hash3.txt and run JtR with the raw-sha256 format:

```bash
echo "[third_hash_here]" > hash3.txt
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt
```

The third password is recovered: qwerty098.

### 4. Retrieve the flag
Submit qwerty098 to the active netcat session. The server validates the input and returns the flag.
`picoCTF{UseStr0nG_h@shEs_&PaSswDs!_6965e43b}`
