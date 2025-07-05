import shutil
import os
#Copy
#shutil.copy('Shutil.py', 'Shutil (Copied).py')
#Copy2 is almost same to copy but copy2 also copy metadata also
#shutil.copy2('Shutil.py', 'Shutil (Copied-1).py')
#Copytree is used to copy folder 
#shutil.copytree('Shutil', 'Shutil-1')
#Move is used to move file or folder
#shutil.move('Shutil/Shutil (Copied-1).py', 'Shutil (Copied-1).py')
#rmtree used to delete folder
#shutil.rmtree('Shutil-1')
#And there is no function for removing follow so we can use os module
#os.remove('Shutil (Copied-1).py')