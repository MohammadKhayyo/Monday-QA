from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from logic.logic_api.column import Column
from logic.logic_api.item import Item
from Utils import generate_string

send_request = MondayApi()

# data_columns = [
#     {"title": "Date", "column_type": "date", "description": "When the row was added to the board",
#      "value": "2024-03-24"},
#     {"title": "Favourite color", "column_type": "text", "description": "the favourite color of the row",
#      "value": "blue"},
#     {"title": "Link", "column_type": "link", "description": "A link to a website",
#      "link": "www.google.com", "placeholder": "search with google"},
#     {"title": "Rating", "column_type": "rating", "description": "",
#      "value": "5"}
# ]


# def flow_api_end_to_end():
#     work_space_name = "MY_TEAM"
#     board_name = generate_string.create_secure_string()
#     group_name = generate_string.create_secure_string()
#     columns_values = list()
#     work_space = WorkSpace(work_space_name=work_space_name)
#     board = Board(work_space=work_space, board_name=board_name, exists=False)
#     group = Group(board=board, group_name=group_name, exist=False)
#     for data_column in data_columns:
#         Column(board=board, title=data_column["title"], column_type=data_column["column_type"],
#                description=data_column["description"], exist=False)
#         columns_values.append((data_column["title"], data_column["value"]))
#         item_name = generate_string.create_secure_string()
#         item = Item(group=group, item_name=item_name, exist=False,
#                     columns_values=columns_values)
#         if data_column['title'] == 'Link':
#             item.add_link(column_title=data_column['title'], link=data_column['link'],
#                           description=data_column['placeholder'])
#         if data_column['title'] == 'Rating':
#             item.set_rating(column_title=data_column['title'], value=data_column['value'])
#     board.delete_board()


def create_board(work_space_id, board_name):
    query = 'mutation { create_board (board_name: "' + board_name + \
            '", board_kind: private, workspace_id: ' + str(work_space_id)
    query += ') { id } }'
    board_id = send_request.post_request(query, until_status_code_429=True)['create_board']['id']
    return board_id


def delete_board(board_id):
    query = 'mutation { delete_board(board_id: "' + board_id + '") { state } }'
    response = send_request.post_request(query, until_status_code_429=True)
    deleted_status = response['delete_board']['state'] == "deleted"
    return deleted_status
