import pymupdf
import sys
from pathlib import Path

if __name__ == "__main__":
    # 1. get output directory
    if len(sys.argv)>1:
        out_dir = sys.argv[1]
    else:
        out_dir = input(">>> Output directory: ")
    
    # 2. get source file path
    if len(sys.argv)>2:
        src_path = sys.argv[2]
    else:
        src_path = input(">>> Source path: ")

    src = pymupdf.open(src_path)
    filename = Path(src_path).stem

    pdf_data = src.convert_to_pdf()
    out = pymupdf.open("pdf",pdf_data)
    out.save(Path(out_dir) / "{}.pdf".format(filename))
