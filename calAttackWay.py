import openpyxl

query_type = [
    [2, 4500, 0]
]


dict_ans={}

def load_ip_set(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f if line.strip())

ip_set = load_ip_set(" ")

ip_set2 = load_ip_set(" ")



def read_txt_file_with_header(file_path):
    global dict_ans
    with open(file_path, 'r') as file:

        header = file.readline().strip().split()


        for line in file:
            data = line.strip().split()
            row_dict = {header[i]: data[i] for i in range(len(header))}
            ip=row_dict['IP']
            if ip not in ip_set2:
                continue
            Maxsize=int(row_dict['Maxsize'])
            Truncsize=int(row_dict['truncated'])
            supTXT=int(row_dict['TXT'])
            supANY=int(row_dict['ANY'])
            supTXTEDNS=int(row_dict['TXTEDNS'])
            supANYEDNS=int(row_dict['ANYEDNS'])
            supTXTDNSSEC=int(row_dict['TXT_DNSSEC'])
            supANYDNSSEC=int(row_dict['ANY_DNSSEC'])
            answers=[]
            for query in query_type:
                if(query[0]==1):
                    querySize=query[1]
                    if(supANY!=1):
                        answers.append(0)
                    else:
                        if(querySize<512):
                            answers.append(querySize)
                        else:
                            if(supANYEDNS!=1):
                                answers.append(0)
                            else:
                                if(querySize<=Maxsize):
                                    answers.append(querySize)
                                else:
                                    if(querySize>Truncsize):
                                        answers.append(0)
                                    else:
                                        if ip in ip_set:
                                            answers.append(500)
                                        else:
                                            answers.append(Maxsize)
                elif(query[0]==2):
                    querySize=query[1]
                    if(supTXT!=1):
                        answers.append(0)
                    else:
                        if(querySize<512):
                            answers.append(querySize)
                        else:
                            if(supTXTEDNS!=1):
                                answers.append(0)
                            else:
                                if(querySize<=Maxsize):
                                    answers.append(querySize)
                                else:
                                    if(querySize>Truncsize):
                                        answers.append(0)
                                    else:
                                        if ip in ip_set:
                                            answers.append(500)
                                        else:
                                            answers.append(Maxsize)
                elif(query[0]==3):
                    querySize=0
                    if(supANY!=1):
                        answers.append(0)
                    else:
                        if(supANYEDNS!=1):
                            answers.append(0)
                        else:
                            if(supANYDNSSEC==0):
                                answers.append(0)
                            else:
                                if(supANYDNSSEC==1):
                                    querySize=query[1]
                                else:
                                    querySize=query[2]
                                if(querySize<=Maxsize):
                                    answers.append(querySize)
                                else:
                                    if(querySize>Truncsize):
                                        answers.append(0)
                                    else:
                                        if ip in ip_set:
                                            answers.append(500)
                                        else:
                                            answers.append(Maxsize)
                elif(query[0]==4):
                    querySize=0
                    if(supTXT!=1):
                        answers.append(0)
                    else:
                        if(supTXTEDNS!=1):
                            answers.append(0)
                        else:
                            if(supTXTDNSSEC==0):
                                answers.append(0)
                            else:
                                if(supTXTDNSSEC==1):
                                    querySize=query[1]
                                else:
                                    querySize=query[2]
                                if(querySize<=Maxsize):
                                    answers.append(querySize)
                                else:
                                    if(querySize>Truncsize):
                                        answers.append(0)
                                    else:
                                        if ip in ip_set:
                                            answers.append(500)
                                        else:
                                            answers.append(Maxsize)
            if(len(answers)<0):
                print('wrong answer mistake  '+ip)
            else:
                if(ip not in dict_ans):
                    dict_ans[ip]=answers


def save_dict_to_txt_and_excel(dict_ans, txt_file_path, excel_file_path):

    with open(txt_file_path, 'w') as txt_file:
        for key, value_list in dict_ans.items():

            value_str = ' '.join(map(str, value_list))

            txt_file.write(f"{key} {value_str}\n")



file_path = " "
read_txt_file_with_header(file_path)


txt_file_path = " "
excel_file_path = " "


save_dict_to_txt_and_excel(dict_ans, txt_file_path, excel_file_path)


