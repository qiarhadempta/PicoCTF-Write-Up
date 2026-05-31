# Riddle Registry

We are given a `.pdf` file where some text is redacted with black blocks, just like Epstein files. The goal is to analyze
the file's and get the flag.  
Link: https://learn.cylabacademy.org/library/530?page=2&workspace=true

<img width="1376" height="631" alt="image" src="https://github.com/user-attachments/assets/b53255d5-020c-42e7-ab6e-3417e0eaf84a" />

---

## Solution

### 1. Download the `.pdf` file

### 2. Inside the pdf, there are some text covered black. I tried to copy them all, and it only reveals all of the text were just random (no flag in it)

<img width="689" height="735" alt="image" src="https://github.com/user-attachments/assets/6a2f0512-881c-48f1-9065-a372ded3cb33" />

### 3. So here, I used `exiftool` to analyze the file's metadata. On the Author line, it shows us a base64 string. 

<img width="1187" height="592" alt="image" src="https://github.com/user-attachments/assets/a4f3a514-57ca-4726-863d-6220e247c25a" />

### 4. Decode the Author base64 string, and we will get the flag: `picoCTF{puzzl3d_m3tadata_f0und!_42440c7d}`

<img width="937" height="614" alt="image" src="https://github.com/user-attachments/assets/a3700897-4123-4753-8626-e636dbde8aad" />

