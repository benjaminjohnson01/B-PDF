#!/usr/bin/env python3

import datetime
import os

from pypdf import PdfWriter

default_directory = os.getcwd()
default_time = datetime.datetime.now()


def set_working_directory(directory):
    os.chdir(directory)


def merge_pdfs(merged_name, pdfs, directory):
    os.chdir(directory)
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf + ".pdf")
    merger.write(merged_name + ".pdf")
    merger.close()
    os.chdir(default_directory)


merged_name = "merged_pdf"
pdfs = ["pdf1", "pdf2"]
directory = r"path\to\directory"

merge_pdfs(merged_name, pdfs, directory)

# future:

# add option to merge all pdfs in directory
# add option to merge all pdfs in directory with certain name
# add option to merge all pdfs in directory with certain name and certain date
# add option to merge all pdfs in directory with certain name and certain date and certain time
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments and certain javascript
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments and certain javascript and certain fonts
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments and certain javascript and certain fonts and certain images
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments and certain javascript and certain fonts and certain images and certain content
# add option to merge all pdfs in directory with certain name and certain date and certain time and certain size and certain number of pages and certain author and certain title and certain subject and certain keywords and certain creator and certain producer and certain version and certain encryption and certain page size and certain page layout and certain page mode and certain metadata and certain outline and certain bookmarks and certain attachments and certain javascript and certain fonts and certain images and certain content and certain forms

# add function to rotate specified pages in combined pdf
# add function to delete specified pages in combined pdf

# handle .pdf and .PDF and .pDf and .pdF and .Pdf and .PDf and .pDF and .pDf
