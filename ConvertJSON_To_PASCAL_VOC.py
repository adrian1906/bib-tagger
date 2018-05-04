# import labelbox2pascal library
import labelbox2pascal as lb2pa

# set labeled_data to the file path of the Labelbox JSON export
labeled_data = 'testimages.json'

# set ann_output_dir to the file path of the directory to write Pascal VOC
# annotation files. The directory must exist.
ann_output_dir = 'M:\\Documents\\700_Tutorials\\bibtagger_hood_2018\\bib-tagger\\Annotatins'

# set images_output_dir to the file path of the directory to write images.
# The directory must exist.
images_output_dir = 'M:\\Documents\\700_Tutorials\\bibtagger_hood_2018\\bib-tagger\\Images'

# call the Labelbox to Pascal conversion
# NOTE: make sure to specify the correct label_format based on the export
#  format chosen on Labelbox; 'WKT' or 'XY'.
lb2pa.from_json(labeled_data=labeled_data, ann_output_dir=ann_output_dir,
                images_output_dir=images_output_dir, label_format='XY')