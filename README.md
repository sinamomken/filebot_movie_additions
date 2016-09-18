# Filebot Movie Additions Repairer
A script correcting Windows-1256 (Arabic) subtitles and renaming/removing jpg files; To be used before import in "filebot"

## When to use?
This python script is written to organize and repair some additional files usually placed beside movies. These cleanup tasks are required before importing movie folders (with Arabic/Persian subtitles) in ["FileBot"](http://www.filebot.net/), because Filebot can't correct these issues yet.

## What does it do?
Currently it repairs 2 set of movie additions:
1. It renames jpg poster of movie to the exact filename of movie; If more than 1 jpg file is present, it retains last one and deletes others. By using this correction, FileBot can relate jpg file to movie name and rename/move it according to movie file.
Ex. In the picture below, you can see 2 jpg files whose name doesn't match filename of movie, and hence FileBot can't raname them alongside the movie.
![jpgs_before_script](./readme_pics/jpgs_before_script.png "Jpgs before script")
But after using this script redundant jpg files are removed and the only one is recognized in FileBot.
![jpgs_after_script](./readme_pics/jpgs_after_script.png "Jpgs after script")
2. It detects Persian/Arabic subtitles in "Windows-1256" encoding and re-encodes them to "UTF-8"; Therefor they can generally be displayed in most video players ever.
Ex. In the picture below, you can see a persian srt subtitle in "Windows-1256" encoding, which can't be displayed correctly by the text-editor (and video player).
![srt_windows-1256_before_script](./readme_pics/srt_windows-1256_before_script.png "Srt Windows-1256 before script")
But after applying this script, the Arabic encoding of the file got detected by some heuristics and corrected to "UTF-8" encoding, which then could be displayed rightly by the text-editor and video player.
![srt_utf-8_after_script](./readme_pics/srt_utf-8_after_script.png "Srt UTF-8 after script")

## How to use?
### Prerequisites
This script is written in Python3 and has used some of its libraries. So if you want to use it be sure to have python3 libraries below installed:
* chardet: A lib that tries to detect encoding of a file
* termcolor: Used to show colored texts in terminal outputs
If you use Ubuntu or any comparable GNU/Linux distro with pip installed, you can install them simply by running command:
```bash
sudo pip3 install chardet termcolor
```

After having all prerequisites installed on your system, use the script by syntax below:
```bash
python3 /<PATH_TO_filebot_movie_additions_DIRECTORY>/filebot_movie_additions.py <PATH_TO_FOLDER_OF_MOVIES>
```
Ex.
```bash
momken@momken-portable:~/PycharmProjects/filebot_movie_additions$ python3 filebot_movie_additions.py "/media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/"
```
Output:
```
1. Removing extra jpg files and renaming the only remained jpg:
No jpg found in /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/

Only movie found: Tangled 2010 720p (PatoghDL)
Rename /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Tangled/tangled.jpg to /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Tangled/Tangled 2010 720p (PatoghDL).jpg

Only movie found: The-Descendants
Rename /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/The Descendants/descendantsposter.jpg to /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/The Descendants/The-Descendants.jpg

Only movie found: Act.of.Valor.2012.KORSUB.720p.HDRip.x264-NA3R
Rename /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Act of Valor 2012/act_of_valor_ver2.jpg to /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Act of Valor 2012/Act.of.Valor.2012.KORSUB.720p.HDRip.x264-NA3R.jpg
Redundant jpg file removed: /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Act of Valor 2012/act_of_valor_ver5.jpg

2. Detecting suspicious Windows-1256 (Arabic) subtitles:
Suspicious file: /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Tangled/Tangled.2010.480p.720p.BluRay.DvDRip.amir_t6262.srt
Content read with Windows-1256 (Arabic) encoding: 
1
00:00:00,000 --> 00:00:21,000
تقديم به پارسي‌زبانان جهان

2
00:00:22,051 --> 00:00:29,000
WwW.PersianDown.CoM
Content converted to UTF-8.

Suspicious file: /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/The Descendants/The.Descendants.2011.DVDSCR.XviD-PRESTiGE.Fa.srt
Content read with Windows-1256 (Arabic) encoding: 
1
00:00:05,000 --> 00:00:24,600
تقديم به تمام پارسي زبانان جهان

2
00:01:01,000 --> 00:01:04,500
wWw.FarsiSubtitle.cOm
Content converted to UTF-8.

Suspicious file: /media/momken/nas_media/Videos/Others/Arvin's/film 1/To Organize/Act of Valor 2012/Act.of.Valor.2012.HDRiP.XViD.AC3-PRESTiGE.srt
Content read with Windows-1256 (Arabic) encoding: 
1
00:00:55,382 --> 00:00:56,885
، قبل از اينکه پدرم بميره

2
00:00:57,069 --> 00:00:58,834
گفتش که بدترين نکته ي بزرگ شدن
Content converted to UTF-8.

```

