# Hidden in Plainsight

We are given a `.jpg` file with hidden data embedded in it. The goal is to analyze
the file's metadata, decode the obfuscated content, and extract the flag using
steganography tools.  
Link: https://learn.cylabacademy.org/library/524?page=2&workspace=true

<img width="1391" height="539" alt="challenge overview" src="https://github.com/user-attachments/assets/9cbf81cd-4f36-42e4-a78e-338ed2e51e7f" />

---

## Solution

### 1. Download the `.jpg` file

### 2. Inspect the metadata with `exiftool`

```bash
exiftool img.jpg
```

A comment field appears in the output with a non-readable value. It's a sign that the
data has been encoded

<img width="867" height="606" alt="exiftool output showing encoded comment" src="https://github.com/user-attachments/assets/f0aa88e3-399f-4295-a6c1-9a1cdfdd3ec9" />

### 3. Decode the first Base64 string

The comment is Base64-encoded. Decoding it reveals steghide:cEF6endvcmQ=  
This tells us the file uses steghide, and the password is itself another Base64 string.

<img width="829" height="667" alt="first Base64 decoded" src="https://github.com/user-attachments/assets/6a0c5e41-5d3d-48eb-8323-44f2065e7385" />

### 4. Decode the second Base64 string

Decoding `cEF6endvcmQ=` gives the steghide password: `pAzzword`

<img width="836" height="629" alt="second Base64 decoded - steghide password" src="https://github.com/user-attachments/assets/3f20e358-c9ff-4b5d-8ff8-7cbafc709e58" />

### 5. Extract the hidden file with steghide

```bash
steghide extract -sf img.jpg -p pAzzword
```

<img width="1248" height="222" alt="steghide extraction" src="https://github.com/user-attachments/assets/048f9ffc-67eb-4e8c-82fd-38f9d6074c02" />

### 6. Retrieve the flag

Open the extracted `flag.txt` and submit the flag.

<img width="992" height="384" alt="flag.txt contents" src="https://github.com/user-attachments/assets/31de26ce-5d26-4f70-95fb-d966bb3a1e63" />
