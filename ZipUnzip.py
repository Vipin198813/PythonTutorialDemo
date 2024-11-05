f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')

comp_file.write('fileone.txt',compress_type= zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type= zipfile.ZIP_DEFLATED)
comp_file.close()
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('Extracted_content')

import os
file_path = os.path.abspath("Extracted_content")
print(file_path)

import shutil
dir_to_zip = "C:\\Users\\User\\PycharmProjects\\LearningPython\\Extracted_content"
output_filename = 'Example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive("Example.zip","final_unzip",'zip')