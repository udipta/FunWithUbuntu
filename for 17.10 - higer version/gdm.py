
def LoginBackground():
	filename = input('enter the path for the file(jpg/png):	')
	os.system('cp filename /usr/share/backgrounds/')

	default = '''#lockDialogGroup {
		background: #2c001e url(resource:///org/gnome/shell/theme/noise-texture.png);
		background-repeat: repeat; } '''

	updated = '''#lockDialogGroup {
		background: #2c001e url(file:///usr/share/backgrounds/''' + filename +''');
		height: 100%; 
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		}'''

	with open("/etc/alternatives/gdm3.css","r") as f:
		newline=[]
		for word in f.readlines():
			newline.append(word.replace(default,updated))  ## Replace the keyword while you copy.
	
	os.system(reboot)


def main():
	import os
	os.system('sudo -s')
	LoginBackground()


if __name__== "__main__":
  main()
