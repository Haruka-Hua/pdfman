# pdfman

This repo collects some python scripts I wrote to deal with pdf files.

## Install environment

You need a python3 interpreter and pip.

You can install the environment using:

```Shell
python -m venv .venv
source .venv/bin/activate # or whatever command to activate the environment
pip install -r requirements.txt
```

## pdf_concat

This scripts concats multiple pdf files into a new one. You can choose the range of pages from the source file that you want to put into the new pdf file.

To run this script, you can use the following command:

```Shell
# make sure you open the terminal under folder pdfman,
# and you have activated the virtual environment
python scripts/pdf_concat.py out_path src_path1 (page_range1)? src_path2 (page_range2)? ...
# where src_path is path to the source file,
# page_range is the pages you want to keep, in a format like: 1,3-4,8-9,10 (index is 1-based)
# if no page_range is give for a source file, then all of its pages will be added.
# here is an example:
python scripts/pdf_concat.py output.pdf in1.pdf 1,3-6,7 in2.pdf 4,1-3,6-8,5
```

> note: You can also use this script to extract certain pages from a pdf file or rearrange the pages.
