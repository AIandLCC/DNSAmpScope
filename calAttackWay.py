import openpyxl

query_type = [
    [2, 4500, 0]
]


dict_ans={}

def load_ip_set(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f if line.strip())

ip_set = load_ip_set("/root/lzh/Total/result/less500.txt")  #超过阈值响应回退至500字节

ip_set2 = load_ip_set("/root/lzh/Total/data/4500.txt")  # 参与计算的IP



def read_txt_file_with_header(file_path):
    """
    逐行读取 TXT 文件，跳过第一行（表头），并将每行数据存储为字典，便于通过表头访问。
    :param file_path: TXT 文件路径
    """
    global dict_ans
    with open(file_path, 'r') as file:
        # 读取并处理表头
        header = file.readline().strip().split()

        # 逐行读取后续数据并存储为字典
        for line in file:
            data = line.strip().split()  # 按空格分隔每行数据
            row_dict = {header[i]: data[i] for i in range(len(header))}  # 创建字典，将表头和数据一一对应
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
    # 保存到 TXT 文件
    with open(txt_file_path, 'w') as txt_file:
        for key, value_list in dict_ans.items():
            # 将列表中的元素按空格连接成字符串
            value_str = ' '.join(map(str, value_list))
            # 将键和值写入TXT文件
            txt_file.write(f"{key} {value_str}\n")



file_path = "/root/lzh/tmp.txt"  
read_txt_file_with_header(file_path)

# 输出文件路径
txt_file_path = " "  # 输出文件格式csv
excel_file_path = " "  # 输出文件格式csv

# 调用函数保存到文件
save_dict_to_txt_and_excel(dict_ans, txt_file_path, excel_file_path)

print(f"数据已保存到 {txt_file_path} 和 {excel_file_path}")
