# Rimu
A latex build tool

## Meta Configuration
Currently the Meta document is a pandoc header though I have plans for it.


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
