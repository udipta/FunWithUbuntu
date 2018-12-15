#!/bin/bash

#pypad - simple python ide
function pypad() {

	python3 /home/udipta/PyPad/src/main.py
}


# labelImg - labeling the image
function labelImg() {
  	python3 /home/udipta/OpenCV_lab/labelImg/labelImg.py
}

#youtube-dl
function playlist() {
	youtube-dl -o "%(playlist_index)s-%(title)s.%(ext)s" -f 22 $1
}

#replaceWordinFiles
function replace() {
	python3 /home/udipta/myCommand/replace.py
}
