import csv


def create_csv(document_title):
    # Open csv in write mode to create column names
    with open(document_title,'w',newline='') as f:
        theWriter = csv.writer(f)


def write_to_csv(document_title,array_for_csv_entry):
    # Open csv in append mode to add new row
    with open(document_title,mode='a') as f:

        theWriter = csv.writer(f)

        # csv data
        theWriter.writerow(array_for_csv_entry)