import os
import sys
import pypandoc
import codecs

RootPath = sys.argv[1]

pandoc_extra_arguments = ['--verbose', f'--resource-path={RootPath}', '--embed-resources', '--standalone', '-f', 'markdown-implicit_figures']

OutputDirectory = os.path.join(RootPath, "Output")

chapterMisc = []

for r,ds,fs in os.walk(RootPath):
    for f in fs:
        if(f.startswith("Chapter")):
            chapterMisc.append(os.path.join(r,f))

print(chapterMisc)

chapterMisc.sort()

print(chapterMisc)

# Handle Meta
metadata = ""
concatChapters = ""

with open(os.path.join(RootPath, "Meta.md"), "r+") as f:
    metadata = ''.join(f.readlines())
    metadata += '\n\n'

for chapter in chapterMisc:
    print("Processing: {}".format(chapter))
    concatChapters += pypandoc.convert_file(chapter, "md", extra_args=pandoc_extra_arguments)
    concatChapters += '\n\n'

temp = metadata + concatChapters

if not os.path.exists(OutputDirectory):
    os.makedirs(OutputDirectory)

# Output intermediate
with codecs.open(os.path.join(OutputDirectory, "markdown.ric"), "w+", "utf-8-sig") as f:
    f.write(temp)

# Sanity the Tex File
pypandoc.convert_text(temp, 'tex', format='md', outputfile=os.path.join(OutputDirectory, 'compile.tex'), extra_args=['-s'] + pandoc_extra_arguments)

# Do the PDF
pypandoc.convert_text(temp, 'pdf', format='md', outputfile=os.path.join(OutputDirectory, 'compile.pdf'), extra_args=['--pdf-engine=lualatex']  + pandoc_extra_arguments)
