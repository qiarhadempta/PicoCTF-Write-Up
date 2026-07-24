# Corrupted file
## Challenge Overview
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

## Hints
1. Try checking the file’s header.
2. JPEG
3. Tools like xxd or hexdump can help you inspect and edit file bytes.

Challenge link: https://learn.cylabacademy.org/library/519?page=4

<img width="1009" height="592" alt="image" src="https://github.com/user-attachments/assets/b9a45fd1-785f-4b6d-8ea1-963c78fd98db" />

## Solutions

Based on the hints, I checked the file header and found that it does not match the standard JPEG format. Standard JPEG files typically begin with the magic bytes `FF D8 FF E0` or `FF D8 FF E1`. However, inspecting the provided file revealed that it starts with `5C 78`, which corresponds to the ASCII representation of `\x` and indicates corrupted or misencoded header bytes.

<img width="1038" height="531" alt="image" src="https://github.com/user-attachments/assets/ff6e920c-ef76-459e-9780-74ac581290dc" />

So to solve this challenge, I opened the file using hexeditor:
```bash
hexeditor file
```

Then I changed the first two bytes (`5C 78`) with the correct JPEG header bytes (`FF D8`)

![Corrupted Header (Before)](https://github.com/user-attachments/assets/c80255e4-ac5b-4fcd-a028-157e294c7b5c)
*(Before: Corrupted Header)*

![Repaired Header (After)](https://github.com/user-attachments/assets/05407df5-7edb-4a60-806a-12a1d0f61cdf)
*(After: Repaired Header)*

Save the file and rename the file back to JPG file
```bash
mv file repaired.jpg
```

Finally, opening `repaired.jpg` displayed the restored image containing the flag.
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/8d825ed6-e0ee-4a7a-a4b6-822e640d10b9" />

Flag: `picoCTF{r3st0r1ng_th3_by73s_0e8fb0ec}`
