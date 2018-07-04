import csv

input_file_name = "jobs.csv" #name/path of your csv file
template_file_name = "template.xml" #name/path of your xml template
output_file_name = "OUTPUT_{}.xml"

with open(template_file_name,"rb") as template_file:
    template = template_file.read()

with open(input_file_name,"rb") as csv_file:
    my_reader = csv.reader(csv_file, delimiter='\t')
    for row in my_reader:
        if row:
            with open(output_file_name.format(row[0]),"wb") as current_out:
                current_out.write(template.format(job_name=row[0],
                                              script_path=row[1]))
