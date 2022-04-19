import os


def find_files(suffix, path):
  """
  Find all files beneath path with file name suffix.

  Note that a path may contain further subdirectories
  and those subdirectories may also contain further subdirectories.

  There are no limit to the depth of the subdirectories can be.

  Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

  Returns:
      a list of paths
  """
  if suffix == None:
    return []

  if len(os.listdir(path)) == 0:
    return []

  
  path_contents = os.listdir(path)
  
  files = [file for file in path_contents if file.endswith('.'+ suffix)]

  folders = [folder for folder in path_contents if '.' not in folder ]


  for folder in folders:
    files.extend(find_files(suffix=suffix, path=os.path.join(path,folder)))


  return files

path_base = os.path.join(os.getcwd(), 'testdir')


print(find_files(suffix='c', path=path_base))
# ['a.c', 'b.c', 'a.c']

print()
print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'b.h', 'a.h']

print()
print(find_files(suffix='z', path=path_base))
# []

print()
print(find_files(suffix='', path=path_base))
# []
print()
print(find_files(suffix='t', path=path_base))
# ['t2.t']