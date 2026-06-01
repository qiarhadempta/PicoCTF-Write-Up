# So Meta
We are given a `.png` file with hidden data embedded in it. The goal is to analyze
the file's metadata, and get the flag.  
Link: https://learn.cylabacademy.org/library/19?page=3&bookmarked=true

<img width="1358" height="670" alt="image" src="https://github.com/user-attachments/assets/fdff1bcf-44dc-40c2-999a-0b961ac0ac79" />

---

## Solution

### 1. Download the `.png` file

### 2. Inspect the metadata with `exiftool`

```bash
exiftool pico_img.png
```

At the Autor's field, we found the flag: `picoCTF{s0_m3ta_9a8b5aa1}`

<img width="854" height="632" alt="image" src="https://github.com/user-attachments/assets/c34d2f94-c866-4d45-9a94-7d6135ffa7f2" />
