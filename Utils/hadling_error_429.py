from infra.infra_api.api_wrapper import MondayApi

send_request = MondayApi()


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
