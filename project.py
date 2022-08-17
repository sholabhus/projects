import csv


# read data from spreadsheet
# open file
def main():
    data = []
    # reading csv file
    with open('sales.csv', 'r') as csv_files:
        # creating csv file reader object
        reader = csv.DictReader(csv_files)
        # extracting each data row one by one
        for row in reader:
            data.append(row)
            print(row)
            # print(row["month"], row["sales"])
            # print(data)

        return data


# calling function
# main()

print("-" * 100)


# collect all of the sales from each month
def sales():
    data = main()
    sales_list = []
    num_of_months = len(data)

    for i in range(num_of_months):
        # data is the LIST of DICTIONARIES
        # i is the POSITION of the DICTIONARY in the LIST (e.g. 0th index, or 3rd index)
        # "sales" is the KEY in the DICTIONARY that will give us the VALUE we want
        sales_list.append(int(data[i]["sales"]))
    print("-" * 100)
    print("sales for each month:")
    print(sales_list)
    print("-" * 100)

    return sales_list


# output the total sales across each month
def sales_sum():
    sales_list = sales()
    total = sum(sales_list)
    # print the total
    print('Total sales: {} '.format(total))
    return total

#
def write_data():
    #header
    header = ['Total sales']
    #call sales_sum
    var = sales_sum()
    data =[var]
    #print(data)

    #open file in write mode
    with open('total.csv', 'w', encoding='UTF8', newline='') as f:
        #create the csv writer
        writer = csv.writer(f)
        #write the header
        writer.writerow(header)
        #write var
        writer.writerow(data)


write_data()
