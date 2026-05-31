# Riddle Registry

We are given a `.pdf` file with some text are covered black, just like Epstein files. The goal is to analyze
the file's and get the flag.  
Link: https://learn.cylabacademy.org/library/530?page=2&workspace=true

<img width="1391" height="539" alt="challenge overview" src="https://github.com/user-attachments/assets/9cbf81cd-4f36-42e4-a78e-338ed2e51e7f" />

---

## Solution

### 1. Download the `.pdf` file

### 2. Inside the pdf, there are some text covered black. I tried to copy them all, and it only reveals all of the text were just random (no flag in it)

<img width="867" height="606" alt="exiftool output showing encoded comment" src="https://github.com/user-attachments/assets/f0aa88e3-399f-4295-a6c1-9a1cdfdd3ec9" />

### 3. So here, I used `exiftool` to analyze the file's metadata. On the Author line, it shows us a base64 string. 

<img width="829" height="667" alt="first Base64 decoded" src="https://github.com/user-attachments/assets/6a0c5e41-5d3d-48eb-8323-44f2065e7385" />

### 4. Decode the Author base64 string, and we will get the flag: `picoCTF{puzzl3d_m3tadata_f0und!_42440c7d}`
