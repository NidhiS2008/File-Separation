import os,shutil

# dict_extension={
# 'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
# 'video_extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
# 'document_extension' : ('.doc','.pdf','.txt')

# }

# folderpath=input("enter a folder path :")

# def file_finder(folder_path,file_extensions):
#     files=[]
#     for file in os.listdir(folder_path):
#         for extension in file_extensions:
#             if file.endswith(file_extensions):
#                 files.append(file)
#     return files

# for extension_type,extension_tuple in dict_extension.items():
#     folder_name=extension_type.split('-')[0]+'files'
#     folder_path=os.path.join(folderpath,folder_name)
#     os.mkdir(folder_path)
#     for item in file_finder(folderpath,extension_tuple):
#         item_path=os.path.join(folderpath,item)
#         item_new_path=os.path.join(folder_path,item)
#         shutil.move(item_path,item_new_path)
#     print('calling file finder')
#     print(file_finder(folderpath,extension_tuple))




