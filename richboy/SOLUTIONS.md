# Solution: Recovering the Message from the Corrupted Disk Image

In this challenge, we were given a corrupted disk image named `treasure` and tasked with recovering its content to unveil the secret to infinite wealth and happiness. The file was analyzed and identified as a Game Boy (GameBoy) ROM.

## Identifying the Corrupted Byte

The first step was to identify the corrupted byte within the disk image. We compared the header of the disk image with a known Game Boy ROM, specifically "Tetris" (tetris.gb). We found that the header of the `treasure` file contained a corrupted byte where the expected value was 'C3 50 01'. Instead, we found '50 01 00' in the file.

## Fixing the Corrupted Byte

To recover the original content of the disk image, we needed to fix the corrupted byte. By changing '50 01 00' to 'C3 50 01' in the file, we restored the Game Boy ROM to its original state.

## Running the Disk Image

With the corrected disk image, we can now run it using a Game Boy emulator. When we did so, the following message was revealed:

**I USE GAMEBOY BTW**

This message suggests that the disk image was indeed a Game Boy ROM.

