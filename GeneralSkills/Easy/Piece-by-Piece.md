# Piece by Piece
## Challenge Overview
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.

Challenge link: https://learn.cylabacademy.org/library/740?page=2&workspace=true

<img width="1374" height="361" alt="image" src="https://github.com/user-attachments/assets/022d83e6-301b-4189-8f8a-f82058d4d6df" />

## Solutions
Log in with the instance ssh and password. Once we logged in, there are 6 files found in the directory: `instructions.txt`  `part_aa`  `part_ab`  `part_ac`  `part_ad`  `part_ae`


<img width="646" height="95" alt="image" src="https://github.com/user-attachments/assets/7b5d2f42-ddf2-4f93-b393-e754405fb5b8" />

By opening `instructions.txt`, we will find some hints:
```bash
- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
```

So, the first thing we are going to do is to combine all the part files using concatenate into 1 file `flag.zip` 
```bash
cat part_* > flag.zip
```

Once we combined it, we can unzip the file with supersecret as its password:
```bash
unzip flag.zip
```

And lastly, open the `flag.txt`
Flag: `picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_28d309dc}`

<img width="683" height="178" alt="image" src="https://github.com/user-attachments/assets/079b467b-1785-4ad4-89f6-f528071da481" />

