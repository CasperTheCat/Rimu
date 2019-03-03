import os
import sys
import pypandoc
import codecs

#chapterMisc = []
#
#for r,ds,fs in os.walk("./"):
#    for f in fs:
#        if(f.startswith("Chapter")):
#            chapterMisc.append(r+f)
#
#print(chapterMisc)
#
#chapterMisc.sort()
#
#print(chapterMisc)

def ParseBeatStructure(x):
    chapterList = []
    print("Chapter Outline")
    rollingChapterCounter = 0
    for i in x:
        i = i.rstrip()
        i = i.lstrip()
        if(i.startswith("# Arc")):
            print(i[2:len(i)])
            rollingChapterCounter = 0
            continue
        elif(i.startswith("- ")):
            rollingChapterCounter += 1
            f = i.split(" ")
            if(len(f) == 3):
                print("Chapter " + str(rollingChapterCounter) + " - \"" + f[1] + "\"")
                chapterList.append(f[2][0:len(i)])
            else:
                print("Chapter " + str(rollingChapterCounter) + " - \"" + f[1] + "\" is not yet written!")
    print(chapterList)
    return chapterList

def ParseMetadata(x):
    headerStart = -1
    headerEnd = -1

    for i in range(0, len(x)):
        if(headerStart == -1 and x[i].startswith("---")):
            headerStart = i
        elif(headerEnd == -1 and x[i].startswith("---")):
            headerEnd = i

    fileList = ParseBeatStructure(x[headerEnd+1:len(x)])

    return ''.join(x[headerStart:headerEnd + 1]) + "\n\n", fileList

# Handle Meta
metadata = ""
meta = ""
concatChapters = ""

with open("Meta.md", "r+") as f:
    meta = f.readlines()

metadata, chapterOrder = ParseMetadata(meta)


for chapter in chapterOrder:
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
