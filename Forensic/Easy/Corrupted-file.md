## Challenge Overview
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

## Hints
1. Try checking the file’s header.
2. JPEG
3. Tools like xxd or hexdump can help you inspect and edit file bytes.

Challenge link: https://learn.cylabacademy.org/library/519?page=4

<img width="1009" height="592" alt="image" src="https://github.com/user-attachments/assets/b9a45fd1-785f-4b6d-8ea1-963c78fd98db" />

## Solutions

Based on the hints, I checked the file header's and found out that the header is not in JPEG standard. In JPEG standards, the header/file magic number usually starts with 
```bash
ffd8 ffe0 0010 4a46 4946 0001 0101 0047 ......JFIF.....G ffd8
```

But in the file we have, the header starts with `5c 78`, which was wrong encoding for JPEG
<img width="1038" height="531" alt="image" src="https://github.com/user-attachments/assets/ff6e920c-ef76-459e-9780-74ac581290dc" />

So to solve this challenge, the first thing I did was open the hexeditor
```bash
hexeditor file
```

and then I changed the first 2 hex `5C 78` into `FF D8`

<img width="1063" height="522" alt="image" src="https://github.com/user-attachments/assets/c80255e4-ac5b-4fcd-a028-157e294c7b5c" />
(before)

<img width="1124" height="677" alt="image" src="https://github.com/user-attachments/assets/05407df5-7edb-4a60-806a-12a1d0f61cdf" />
(after)

Save the file, and lastly, rename the file back to JPG file
```bash
mv file repaired.jpg
```

We can check the flag in `repaired.jpg` 
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/8d825ed6-e0ee-4a7a-a4b6-822e640d10b9" />

Flag: `picoCTF{r3st0r1ng_th3_by73s_0e8fb0ec}`
