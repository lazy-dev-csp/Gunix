### Gunix
Gunix or Gux is a tool that enables you to see the uni timestamp or date of creation of any file.

## Usage

**Default:** basic info
./gux.py photo.jpg

**Size in GiB**
./gux.py movie.mp4 -s GiB

**Date only**
./gux.py doc.pdf -d

**Unix + Date**
./gux.py log.txt -u -d

# Eample Output

```bash$ ./gux.py example.mp4 -s GiB
File Is: 0.39 GiB

$ ./gux.py example.mp4
File: example.mp4
  Modified: 11/08/25
  Size: 413957.24 KiB
```
