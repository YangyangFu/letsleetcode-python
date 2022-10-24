import os 

toc = '_toc.yml'
with open(toc, 'w') as f:
    f.write('# Table of Contents generated from generate_toc.py\n')
    f.write('format: jb-book \n')
    f.write('root: intro \n')
    f.write('parts:\n')

# generate content
def generate_table(folder):
    """
    This function generates table texts based on folder structure.
    The file is generated as chapter, and the subdirectories are generated as sections for the folder
    """
    table = []
    # generate caption
    table.append('- caption: '+folder.capitalize()+'\n')

    # scan folder
    files_and_folders = os.scandir(folder)
    print(dir(files_and_folders))

    # separate subdirectories and files
    subdirs = []
    files = []
    for f in files_and_folders:
        if f.is_dir():
            subdirs.append(f.path)
        else:
            files.append(f.path)
    
    # only keey .ipynb, .md file
    for f in files:
        if '.ipynb' not in f and '.md' not in f:
            files.remove(f)
    
    # generate toc for chapters
    ordered_chapters = sorted(files)
    table.append('  chapters:' + '\n')
    for chapter in ordered_chapters:
        table.append('  - file: '+chapter+'\n')
        # check if there are sections
        section = chapter.split('/')[-1].split('.')[0]
        for subdir in subdirs:
            # there are sections for current chapter
            if section in subdir:
                table.append('    sections: \n')
                # get all files for sections
                section_files = [f.path for f in os.scandir(subdir) if not f.is_dir()]
                for sf in sorted(section_files):
                    table.append('    - file: '+sf+'\n')

    return table    

## generate toc for ./basics
folder = 'basics'
table = generate_table(folder)
with open(toc, 'a') as f:
    f.writelines(table)

## generate toc for ./convex optimization
folder = "convex-optimization"
table = generate_table(folder)
with open(toc, 'a') as f:
    f.writelines(table)

## generate toc for leetcode
folder = "leetcode"
table = generate_table(folder)
with open(toc, 'a') as f:
    f.writelines(table)

## generate notes
folder = "notes"
table = generate_table(folder)
with open(toc, 'a') as f:
    f.writelines(table)

