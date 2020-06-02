import csv

def print_counts():
    directory='/Users/prashanth.shivarudri/PycharmProjects/'
    file_in='school_data.csv'
    file_in_path=directory+file_in

    with open(file_in_path,encoding='cp1252') as fp:
        csv_reader=csv.reader(fp)
        next(csv_reader)
        total_schools=0
        state_schools={}
        metro_schools={}
        city_schools={}

        for csv_record in csv_reader:
            if len(csv_record)>0:
              total_schools+=1
              if csv_record[5] in state_schools.keys():
                  state_schools[csv_record[5]]+=1
              else:
                   state_schools[csv_record[5]]=1

              if csv_record[8] in metro_schools.keys():
                  metro_schools[csv_record[8]]+=1
              else:
                   metro_schools[csv_record[8]]=1

              if csv_record[4] in city_schools.keys():
                  city_schools[csv_record[4]]+=1
              else:
                   city_schools[csv_record[4]]=1

        max_schools_in_city=max(city_schools.values())
        max_schools_city=filter(lambda x:city_schools[x]==max_schools_in_city,city_schools.keys())
        city_count=len(city_schools)
        print('Total Schools: ',total_schools)
        print('Schools by State:')
        for key,value in state_schools.items():
            print(key,':',value)
        print('Schools by Metro-centric locale:')
        for key,value in metro_schools.items():
            print(key,':',value)
        print('City with most schools: ',list(max_schools_city)[0],'(',max_schools_in_city,')')
        print(len(city_schools))
        print('Unique cities with at least one school: ',city_count)

if __name__ == '__main__':
    print_counts()
