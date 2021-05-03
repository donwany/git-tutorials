import csv
import sys

males_older_than_30 = []
females_older_than_30 = []
file_name = 'Social_Network_Ads.csv'

# read data
with open(file_name, 'r') as social:
    csv_dict = csv.DictReader(social)
    try:
        for row in csv_dict:
            if int(row['Age']) >= 30 and row['Gender'] == 'Male':
                males_older_than_30.append(row)
            elif int(row['Age']) >= 30 and row['Gender'] == 'Female':
                females_older_than_30.append(row)
    except csv.Error as ex:
        sys.exit('file {}, line {}:{}'.format(file_name, csv_dict.line_num, ex))


# write male data
with open('males_older_than_30.csv', 'w') as male_write:
    # field names
    field_names = ['User ID', 'Gender', 'Age', 'EstimatedSalary','Purchased']
    male_writer = csv.DictWriter(male_write, fieldnames=field_names)
    male_writer.writeheader()
    male_writer.writerows(males_older_than_30)


# write females data
with open('females_older_than_30.csv', 'w') as female_write:
    # field names
    field_names = ['User ID', 'Gender', 'Age', 'EstimatedSalary','Purchased']
    female_writer = csv.DictWriter(female_write, fieldnames=field_names)
    female_writer.writeheader()
    female_writer.writerows(females_older_than_30)


if __name__ == '__main__':

    for male in males_older_than_30:
        print(male)

    print('*'*100)

    for female in females_older_than_30:
        print(female)

    print("Done!")
    print("Completed!")