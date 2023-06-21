def format_data_for_display(people):
        return [f'{item["given_name"]} {item["family_name"]}: {item["title"]}' for item in people]
    

def format_data_for_excel(people):
        excel_data = 'given,family,title\n'
        for item in people:
                excel_data += f'{item["given_name"]},{item["family_name"]},{item["title"]}\n'
        return excel_data


        