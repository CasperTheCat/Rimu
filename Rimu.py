import os
import sys
import pypandoc
import codecs

chapterMisc = []

for r,ds,fs in os.walk("./"):
    for f in fs:
        if(f.startswith("Chapter")):
            chapterMisc.append(r+f)

print(chapterMisc)

chapterMisc.sort()

print(chapterMisc)

# Handle Meta
metadata = ""
concatChapters = ""

with open("Meta.md", "r+") as f:
    metadata = ''.join(f.readlines())
    metadata += '\n\n'

for chapter in chapterMisc:
    concatChapters += pypandoc.convert_file(chapter, "md")
    concatChapters += '\n\n'

temp = metadata + concatChapters

# Output intermediate
with codecs.open("markdown.ric", "w+", "utf-8-sig") as f:
    f.write(temp)

# Sanity the Tex File
pypandoc.convert_text(temp, 'tex', format='md', outputfile='compile.tex', extra_args=['-s'])

# Do the PDF
pypandoc.convert_text(temp, 'pdf', format='md', outputfile='compile.pdf', extra_args=['--pdf-engine=lualatex'])
