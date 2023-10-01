from local_data import get_schedule_type_from_user

def transform_json_to_ouptut_format(data):
  
    grouped_data = {}
    for item in data:
        date = item['date']
        weekday = item['weekday']
        if date not in grouped_data:
            grouped_data[date] = {
                "weekday": weekday,
                "classes": []
            }
        class_info = {
            "pairnumber": item['pairnumber'],
            "timestart": item['timestart'],
            "timeend": item['timeend'],
            "edworkkind": item['edworkkind'],
            "dis": item['dis'],
            "pos": item['pos'],
            "teacher": item['teacher'],
            "umk": item['umk'],
            "umk2": item['umk2'], 
            "groups": item['groups'],
            "online": item['online'],
            "room": item['room']
        }
        grouped_data[date]['classes'].append(class_info)

    # Convert to desired text format
    output = []
    for date, info in grouped_data.items():
        output.append(f"*=={date}, {info['weekday']}==*")


        for cls in info['classes']:
            # define online/offline fiels, room field
            if cls['online']=="1":
                online_offline = "онлайн"     
            else:
                if cls['room']!="null":
                    online_offline = "оффлайн: {}".format(cls['room'])
                else:
                    online_offline = "оффлайн"

            
            # Add groups field only if it exists (for teachers)
            if (cls['groups']!="null" and cls['teacher']=="null"):
                output.append(f"*{cls['pairnumber']} пара* - {cls['timestart']}-{cls['timeend']} _гр. {cls['groups']}_ {online_offline}")
            else:
                output.append(f"*{cls['pairnumber']} пара* - {cls['timestart']}-{cls['timeend']} _{online_offline}_")
            
            # Add second link only if it exists
            if cls['umk2'] and cls['umk2'] != 'null':
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']}), [Ссылка 2]({cls['umk2']})")
            else:
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']})")
            
            # Add pos and teacher only if pos exists
            if (cls['pos'] and cls['teacher']) and (cls['pos']!="null" and cls['teacher']!="null"):
                output.append(f"_{cls['pos']} {cls['teacher']}_")
            elif (cls['teacher'] and cls['teacher']!="null"):
                output.append(f"_{cls['teacher']}_")

            
                
        output.append("")

    # Join list elements to form the final text
    final_output = '\n'.join(output)
    return final_output


def transform_student_json(data):
            
    grouped_data = {}
    for item in data:
        date = item['date']
        weekday = item['weekday']
        if date not in grouped_data:
            grouped_data[date] = {
                "weekday": weekday,
                "classes": []
            }
        class_info = {
            "pairnumber": item['pairnumber'],
            "timestart": item['timestart'],
            "timeend": item['timeend'],
            "edworkkind": item['edworkkind'],
            "dis": item['dis'],
            "pos": item['pos'],
            "teacher": item['teacher'],
            "umk": item['umk'],
            "umk2": item['umk2']
        }
        grouped_data[date]['classes'].append(class_info)

    # Convert to desired text format
    output = []
    for date, info in grouped_data.items():
        output.append(f"*=={date}, {info['weekday']}==*")
        for cls in info['classes']:
            output.append(f"*{cls['pairnumber']} пара* - {cls['timestart']}-{cls['timeend']}")
            
            # add umk2 if only exists
            if cls['umk2'] and cls['umk2'] != 'null':
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']}), [Ссылка 2]({cls['umk2']})")
            else:
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']})")
            
            # Add pos and teacher only if pos exists
            if (cls['pos'] and cls['teacher']) and (cls['pos']!="null" and cls['teacher']!="null"):
                output.append(f"_{cls['pos']} {cls['teacher']}_")
            elif (cls['teacher'] and cls['teacher']!="null"):
                output.append(f"_{cls['teacher']}_")


                
        output.append("")

    # Join list elements to form the final text
    final_output = '\n'.join(output)
    return final_output

def transform_teacher_json(data):
            
    grouped_data = {}
    for item in data:
        date = item['date']
        weekday = item['weekday']
        if date not in grouped_data:
            grouped_data[date] = {
                "weekday": weekday,
                "classes": []
            }
        class_info = {
            "pairnumber": item['pairnumber'],
            "timestart": item['timestart'],
            "timeend": item['timeend'],
            "edworkkind": item['edworkkind'],
            "dis": item['dis'],
            "pos": item['pos'],
            "teacher": item['teacher'],
            "umk": item['umk'],
            "umk2": item['umk2']
        }
        grouped_data[date]['classes'].append(class_info)

    # Convert to desired text format
    output = []
    for date, info in grouped_data.items():
        output.append(f"*=={date}, {info['weekday']}==*")
        for cls in info['classes']:
            output.append(f"*{cls['pairnumber']} пара* - {cls['timestart']}-{cls['timeend']}")
            
            if cls['umk2'] and cls['umk2'] != 'null':
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']}), [Ссылка 2]({cls['umk2']})")
            else:
                output.append(f"[{cls['edworkkind']} {cls['dis']}]({cls['umk']})")
            
            # Add pos and teacher only if pos exists
            if (cls['pos'] and cls['teacher']) and (cls['pos']!="null" and cls['teacher']!="null"):
                output.append(f"_{cls['pos']} {cls['teacher']}_")
            elif (cls['teacher'] and cls['teacher']!="null"):
                output.append(f"_{cls['teacher']}_")
                
        output.append("")

    # Join list elements to form the final text
    final_output = '\n'.join(output)
    return final_output