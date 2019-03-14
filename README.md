# Rimu
A latex build tool

## Meta Configuration

The Meta document is a pandoc header in addition to the chapter listing in the following form:

```
# Arc ...                               -- Used for ordering, and a few chapter count things
 - <chaptername> <chapterlocation>      -- A chapter list is generated from the order here
 - <chaptername> <chapterlocation>      -- Note, location is optional to allow placeholding
```

A future update will expand on the aforementioned functionality.

## Substitution Configuration

Text substitution can be enabled by supplying a file named `Substitute.md`.

Substitution entries take the following form:

```
Original Text = Substitute
```

Note that the above will find every occurance of `Original Text`, regardless of the original document format, and replace it with `Substitute`.


## Setting Header and Text Font Families
Adding the below configuration to the Header Includes field will
cause the headers to be Serif and the document text to be Sans-Serif.

Sectsty can be substituted for Koma-Script as is documented lower in
this document.

```
\renewcommand{\familydefault}{\sfdefault}
\usepackage{sectsty}
\allsectionsfont{\rmfamily}
```



## Container Configuration
This repository uses a container based on Ubuntu 18.10 with the following
commands executed:

```
apt-get install -y texlive-lang-english texlive-luatex fonts-noto fonts-noto-cjk python3 pandoc python3-pip texlive-games texlive-humanities texlive texlive-latex-extra
```

```
pip3 install pypandoc
```


## Setting CJK Fonts
This can be done by adding the following to the meta document

```
CJKsansfont: <CJK Sans-Serif Font>
CJKmainfont: <CJK Serif Font>
```

## Koma
This is only here because I forget about Koma a lot...

This sets the headers to serif in Koma
```
\addtokomafont{disposition}{\rmfamily}
```
