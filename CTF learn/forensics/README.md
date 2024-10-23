
## File Signatures
- File signatures are unique sequences of bytes that identify the type of file.
- They are also known as magic numbers or magic bytes.
- They are used by file managers and operating systems to identify the type of file.

### Tools to Identify File Signatures
- `file` command in Linux
    - ```bash
      file <filename>
      ```
- `TrID` tool in Windows
    - ```bash
      trid <filename>
      ```
- `binwalk` check for embedded (compressed) files in another file
    - ```bash
      binwalk <filename>
      ```
- `xxd` in linux to view the hexadecimal representation of a file
    - ```bash
      xxd <filename> | head
      ```

### Common File Signatures


File Type	File Extension	File Signature (Hexadecimal)	File Signature (ASCII)
| File Type                  | Extension  | Hex Signature                        | ASCII Signature       |
|----------------------------|------------|--------------------------------------|------------------------|
| JPEG Image                 | .jpg / .jpeg | FF D8 FF E0 or FF D8 FF E1           | ÿØÿà or ÿØÿá           |
| PNG Image                  | .png       | 89 50 4E 47 0D 0A 1A 0A              | .PNG....               |
| GIF Image                  | .gif       | 47 49 46 38 39 61 or 47 49 46 38 37 61 | GIF89a or GIF87a       |
| PDF Document               | .pdf       | 25 50 44 46                          | %PDF                   |
| ZIP Archive                | .zip       | 50 4B 03 04                          | PK..                   |
| RAR Archive                | .rar       | 52 61 72 21 1A 07                    | Rar!..                 |
| Microsoft Word (DOC)       | .doc       | D0 CF 11 E0 A1 B1 1A E1              | .........              |
| Microsoft Word (DOCX)      | .docx      | 50 4B 03 04                          | PK.. (ZIP compressed format) |
| Executable (EXE)           | .exe       | 4D 5A                                | MZ                     |
| Windows DLL                | .dll       | 4D 5A                                | MZ                     |
| MP3 Audio                  | .mp3       | 49 44 33                             | ID3                    |
| MP4 Video                  | .mp4       | 66 74 79 70 69 73 6F 6D              | ftypisom               |
| BMP Image                  | .bmp       | 42 4D                                | BM                     |
| TAR Archive                | .tar       | 75 73 74 61 72                       | ustar                  |
| ELF Executable             | .elf       | 7F 45 4C 46                          | .ELF                   |
| WAV Audio                  | .wav       | 52 49 46 46                          | RIFF                   |

### References
- https://www.garykessler.net/library/file_sigs.html

- https://en.wikipedia.org/wiki/List_of_file_signatures

## Metadata
- Metadata is data about data. Different types of files have different metadata. The metadata on a photo could include dates, camera information, GPS location, comments, etc. For music, it could include the title, author, track number and album. CTF challenges often have you looking for specific clues in the metadata of a file (especially media files).

### How do I find it?
- `exiftool` is a tool that can be used to extract metadata from files.
    - ```bash
      exiftool <filename>
      ```
      - [Docs](https://exiftool.org/exiftool_pod.html)

- `strings` command in Linux can be used to extract ASCII strings from a file.
    - ```bash
      strings <filename>
      ```

## Segnography

- Hiding data in a unused area of a file or in a way that is not obvious.
- Can be used to hide messages in images, audio files, etc.
- Can be used to hide files in other files.

### Tools
- `steghide` is a tool that can be used to hide and extract data from files.
    - ```bash
      steghide embed -cf <cover_file> -ef <file_to_hide>
      steghide extract -sf <stego_file>
      ```
- `stegsnow` is a tool that can be used to hide and extract data from files.
    - ```bash
      stegsnow -C <cover_file> -m <message>
      stegsnow -C <stego_file>
      ```
- `zsteg` is a tool that can be used to detect hidden data in PNG and BMP files.
    - ```bash
      zsteg <filename>
      ```

## Memory Forensics
- Memory forensics is the analysis of a computer's memory (RAM) to investigate an incident or to find evidence of malicious activity.
- Memory forensics can be used to:
    - Find running processes
    - Find open network connections
    - Find open files
    - Find hidden processes
    - Find hidden files
    - Find malware
    - Find rootkits
    - Find evidence of an attack

### Steps
1. Acquire the memory image
    - Use a tool like `LiME`, `FTK Imager`, `Magnet RAM Capture`, `Winpmem`, etc.
    
2. Analyze the memory image
    - Analyze the image that you have acquired.
    - Analyze for running processes, open network connections, open files, hidden processes, hidden files, malware, rootkits, etc.
    - Use a tool like `Volatility`, `Rekall`, `Mandiant Redline`, etc.
    
#### Tools
- `Volatility` is a tool that can be used to analyze memory images.
    - [Volatility](./Volatility.md)