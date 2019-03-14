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


def generateSubstitutes(x):
    # x is keyvalue
    keyvalue = {}
    for xi in x:

        sxi = xi.split("=")

        if(len(sxi) == 2):
            # Correct
            safeKey = sxi[0].rstrip().lstrip()
            safeValue = sxi[1].rstrip().lstrip()
            print("[INFO] Registered Keyword \"" + safeKey + "\" will substitute out for \"" + safeValue + "\"")
            keyvalue[safeKey] = safeValue

    return keyvalue

def markdownSubstitute(x, kv):
    # load x
    outLines = []
    with codecs.open(x) as fileHandle:
        lines = fileHandle.readlines()

        for li in lines:

            recurrentStr = li
            for sub in kv:
                recurrentStr = recurrentStr.replace(sub, kv[sub])

            outLines.append(recurrentStr)
    
    return ''.join(outLines) + "\n\n"

  
def markdownSubstituteInline(x, kv):
    for sub in kv:
        x = x.replace(sub, kv[sub])
    return x
            
# Handle Variable Sub
variableSubstitutions = {}
if(os.path.isfile("Substitute.md")):
    try:
        with codecs.open("Substitute.md") as vsub:
            vsLines = vsub.readlines()
            variableSubstitutions = generateSubstitutes(vsLines)
    except Exception as e:
        print(e)
        print("Substitution file exists, but cannot be read. Exiting.")
        sys.exit(-1)

# Handle Meta
metadata = ""
meta = ""
concatChapters = ""

with open("Meta.md", "r+") as f:
    meta = f.readlines()

metadata, chapterOrder = ParseMetadata(meta)


for chapter in chapterOrder:
    #if(chapter.endswith(".md")):
        # Subbing is only enabled on markdown sources!
    #    concatChapters += markdownSubstitute(chapter, variableSubstitutions)
    #else:
    concatChapters += markdownSubstituteInline(pypandoc.convert_file(chapter, "md"),variableSubstitutions)    
    concatChapters += '\n\n'

temp = metadata + concatChapters

# Output intermediate
with codecs.open("markdown.ric", "w+", "utf-8-sig") as f:
    f.write(temp)

# Sanity the Tex File
pypandoc.convert_text(temp, 'tex', format='md', outputfile='compile.tex', extra_args=['-s'])

# Do the PDF
pypandoc.convert_text(temp, 'pdf', format='md', outputfile='compile.pdf', extra_args=['--pdf-engine=lualatex'])
