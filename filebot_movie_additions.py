#!/usr/bin/python3

import sys, os, re
import chardet
from termcolor import colored

def rename_image(dir):
    print(colored('1. Removing extra image files and renaming the only remained image:', 'blue'))
    last_image = ''
    last_image_suffix = ''
    found_movie = ''
    num_of_movies = 0
    num_of_images = 0
    if os.path.isdir(dir) == True:
        for subdir, dirs, files in os.walk(dir):
            # resetting counters
            num_of_images = 0
            num_of_movies = 0

            # finding last_image
            for file in files:
                if re.match(r'^(.*)\.(jpg|jpeg|JPG|JPEG)$', file):
                    #print('Image file found: ' + os.path.join(subdir, file))
                    last_image = file
                    last_image_suffix = '.jpg'
                    num_of_images += 1
                if re.match(r'^(.*)\.(png|PNG)$', file):
                    # print('Image file found: ' + os.path.join(subdir, file))
                    last_image = file
                    last_image_suffix = '.png'
                    num_of_images += 1

            # finding movie files
            for file in files:
                if re.match(r'^(.*)\.(mkv|avi|mp4|wmv|MKV|AVI|MP4|WMV)$', file):
                    found_movie = file[:-4]
                    num_of_movies += 1

            if num_of_images > 0:
                if num_of_movies == 1:
                    print(colored('Only movie found: ', 'green') + found_movie)
                    print(colored('Rename ', 'green') + os.path.join(subdir,last_image)
                          + colored(' to ', 'green') + os.path.join(subdir,found_movie + last_image_suffix))
                    # renaming image to the only movie name
                    os.rename(os.path.join(subdir,last_image), os.path.join(subdir,found_movie + last_image_suffix))

                    # deleting all images except last_image
                    for file in files:
                        if re.match(r'^(.*)\.(jpg|jpeg|JPG|JPEG|png|PNG)$', file) and file != last_image:
                            print(colored('Redundant image file removed: ', 'yellow') + os.path.join(subdir, file))
                            os.remove(os.path.join(subdir, file))
                elif num_of_movies == 0:
                    print(colored('No movie in dir ', 'red') + subdir)
                else:
                    print(colored('More than 1 movie in dir ', 'red') + subdir)
            else:
                print(colored('No image found in ', 'red') + subdir)
            print('')
    else:
        print("MyError: not dir")
        return 1


def detect_persian_encodings(dir):
    print(colored('2. Detecting suspicious Windows-1256 (Arabic) subtitles:', 'blue'))
    if os.path.isdir(dir) == True:
        for subdir, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.srt'):
                    rawdata = open(os.path.join(subdir,file), "rb").read()
                    result = chardet.detect(rawdata)
                    charenc = result['encoding']
                    confidence = result['confidence']

                    # Because chardet can't identify "Arabic (Windows 1256)", it always
                    # detects it as "MacCyrillic" with low confidence
                    if charenc == 'MacCyrillic' and confidence < 0.5:
                        print(colored('Suspicious file: ', 'yellow')
                              + os.path.join(subdir, file))
                        correct_persian_endoding(os.path.join(subdir,file))


def correct_persian_endoding(file_abspath):
    file = open(file_abspath, 'rb')
    try:
        raw_file = file.read()
    except Exception:
        print(colored("can't read file " + file_abspath, 'red'))
        return 1

    file_data = raw_file.decode('windows-1256')
    # Printing first 8 lines
    print(colored('Content read with Windows-1256 (Arabic) encoding: ', 'red'))
    for i in range(7):
           print(file_data.splitlines()[i])

    file = open(file_abspath, 'wb')
    try:
        file.write(file_data.encode('utf-8'))
        print(colored('Content converted to UTF-8.\n', 'green'))
    except Exception:
        print(colored(Exception, 'red'))
    finally:
        file.close()


if __name__ == "__main__":
    dir = sys.argv[1]
    rename_image(dir)
    detect_persian_encodings(dir)

