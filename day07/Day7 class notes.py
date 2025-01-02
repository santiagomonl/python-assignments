##Day7 class notes

##create a txt with requirements to be install
##then you type pip install -r ../folder/requirements.txt

##File Chooser in jupyter notebook
pip install ipyfilechooser

from ipyfilechooser import FileChooser
import os

os.getcwd()
fc = FileChooser(os.path.dirname(os.getcwd()))
display(fc)

print(fc.selected_path)


