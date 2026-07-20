# DISKO 1
## Challenge Overview
Can you find the flag in this disk image?

## Hints
Maybe Strings could help? If only there was a way to do that?


Challenge link: https://learn.cylabacademy.org/library/505?page=4
<img width="1012" height="610" alt="image" src="https://github.com/user-attachments/assets/b95f35e5-5861-4050-a67c-7c8684810ba8" />

## Solutions
The first thing I did was unzip the file with this command:
```bash
gunzip disko-1.dd.gz
```

<img width="1587" height="167" alt="image" src="https://github.com/user-attachments/assets/ed41cc90-0631-47c2-9c23-6fcfbc9a8f01" />

Next, I'm trying to extract the printable strings in the file, but it turns out it has so many string lines. It would be hard for us to analyze and find the flag. 
So, at the end, I'm using grep command to find the specific string that contains `pico`:
```bash
strings disko-1.dd | grep "pico"
```

<img width="1485" height="600" alt="image" src="https://github.com/user-attachments/assets/0308f13f-eae2-475f-b392-73cf05c196f1" />

Flag: `picoCTF{1t5_ju5t_4_5tr1n9_be6031da}`

