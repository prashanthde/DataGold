import csv
import time

def pre_process():

    states={"AL": "Alabama" ,  "AK": "Alaska" , "AZ": "Arizona" ,  "AR": "Arkansas" , "CA": "California" ,  "CO": "Colorado" ,  "CT": "Connecticut" ,  "DE": "Delaware",
            "DC": "District of Columbia" ,  "FL": "Florida" ,  "GA": "Georgia" ,  "HI": "Hawaii" ,  "ID": "Idaho" ,  "IL": "Illinois" ,  "IN": "Indiana" ,  "IA": "Iowa" ,
            "KS": "Kansas" ,  "KY": "Kentucky" ,  "LA": "Louisiana" ,  "ME": "Maine" ,  "MD": "Maryland" ,  "MA": "Massachusetts" ,  "MI": "Michigan" ,  "MN": "Minnesota" ,
            "MS": "Mississippi" ,  "MO": "Missouri" ,  "MT": "Montana" ,  "NE": "Nebraska" ,  "NV": "Nevada" ,  "NH": "New Hampshire" ,  "NJ": "New Jersey" ,
            "NM": "New Mexico" ,  "NY": "New York" ,  "NC": "North Carolina" ,  "ND": "North Dakota" ,  "OH": "Ohio" ,  "OK": "Oklahoma" ,  "OR": "Oregon" ,
            "PA": "Pennsylvania" ,  "RI": "Rhode Island" ,  "SC": "South Carolina" ,  "SD": "South Dakota" , "TN": "Tennessee" ,  "TX": "Texas" , "UT": "Utah" ,
            "VT": "Vermont" , "VA": "Virginia" ,  "WA": "Washington" ,  "WV": "West Virginia" ,  "WI": "Wisconsin" ,  "WY": "Wyoming"}
    directory='/Users/prashanth.shivarudri/PycharmProjects/'
    file_in='school_data.csv'
    file_out='school_tokens.csv'
    file_in_path=directory+file_in
    file_out_path=directory+file_out
    with open(file_in_path,encoding='cp1252') as fp:
        csv_reader=csv.reader(fp)
        next(csv_reader)
        school_names_city_state_tokens_set=set()
        school_names_city_tokens=set()
        schools_dict={}

        for csv_record in csv_reader:
              school_name_tokens=csv_record[3].replace('-',' ').split()
              city_tokens=csv_record[4].split()
              state=states.get(csv_record[5],'')
              state_list=[state.upper()]

              school_name_city_state_tokens=school_name_tokens+city_tokens+state_list
              school_name_city_state_tokens_set=tuple(school_name_city_state_tokens)
              school_names_city_state_tokens_set.add(school_name_city_state_tokens_set)

              schools_dict[school_name_city_state_tokens_set]=csv_record[3]+' '+csv_record[4]+' '+csv_record[5]


    with open(file_out_path,'w') as fp2:
        for key in schools_dict.keys():
            key1=str(key)
            fp2.write("%s:%s\n"%(key,schools_dict[key]))


def school_search(search_token):
    directory='/Users/prashanth.shivarudri/PycharmProjects/'
    file_out='school_tokens.csv'
    file_out_path=directory+file_out
    i=1
    j=1
    search_token2=set(search_token.upper().split())

    with open(file_out_path,'r') as fp3:
        reader=csv.reader(fp3,delimiter=':')
        schools_dict2={}
        for row in reader:
            schools_dict2[row[0]]=row[1]
            row1=tuple(row[0].replace("(","").replace(")","").replace("'","").split(", "))
            if search_token2.issubset(row1):
                print(i,'.',row[1])
                i+=1
                if i>3:
                    break
            else:
                new_search_token=search_token2
                school_constant={'SCHOOL'}
                if school_constant.issubset(new_search_token):
                    new_search_token.remove('SCHOOL')
                    if new_search_token.issubset(row1):
                        print(j,'.',row[1])
                        j+=1
                        if j>3:
                            break

if __name__ == '__main__':
    pre_process()
    start_time = time.time()
    school_search('elementary school highland park')
    print("time elapsed: {:.2f}s".format(time.time() - start_time) )
