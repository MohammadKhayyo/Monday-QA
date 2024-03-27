from Utils import generate_string
from logic.logic_api.column import Column
from logic.logic_api.item import Item


def upload_file_helper(board, group, data_column):
    item_name = generate_string.create_secure_string()
    Column(board=board, title=data_column['title'], description=data_column['description'],
           column_type=data_column['column_type'])
    item = Item(group=group, item_name=item_name, exist=False)
    item.upload_files(column_title=data_column['title'], files_paths=data_column["files_paths"])
    item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
    return item_details['text']


def returning_local_file_names(files_names):
    local_file_names = list()
    for i in range(0, len(files_names)):
        local_file_names.append(files_names[i].split('/')[-1])
    local_file_names.sort()
    return local_file_names


def returning_file_names_from_the_website(files_names):
    website_file_names = list()
    files_names = files_names.split(',')
    for i in range(0, len(files_names)):
        website_file_names.append(files_names[i].split('/')[-1])
    website_file_names.sort()
    return website_file_names
