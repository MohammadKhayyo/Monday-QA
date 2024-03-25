from infra.infra_api.api_wrapper import MondayApi


class Column:
    def __init__(self, board, column_type=None, column_id=None, exist=False, title=None, description=""):
        self.send_request = MondayApi()
        self.board = board
        self.column_name = title
        self.column_id = column_id
        self.column_description = description
        self.column_type = column_type
        if exist is False:
            if title is None:
                raise ValueError("")
            self.create_column()
        else:
            if self.column_name not in self.board.columns:
                raise Exception('Column not found')

            columns_details = self.board.columns[self.column_name]
            # if column_id:
            #     columns_details = self.check_group_via_key(key='id', value=column_id)
            # elif title:
            #     columns_details = self.check_group_via_key(key='title', value=title)
            # if columns_details is None:
            #     raise ValueError("")
            self.column_name = columns_details.column_name
            self.column_id = columns_details.column_id
            self.column_type = columns_details.column_type
            self.column_description = columns_details.column_description

    def check_group_via_key(self, key, value):
        columns = self.board.get_all_columns()

        for column in columns:
            if column[key] == value:
                return column
        return None

    def create_column(self):
        self.board.columns[self.column_name] = self
        column_details = self.send_request.post_request(
            query='mutation{ create_column(board_id: ' + self.board.board_id + ', title:"' + self.column_name +
                  '", description: "' + str(self.column_description) + '", column_type:' + self.column_type +
                  ') { id title description } }')['create_column']
        self.column_id = column_details['id']
        self.column_name = column_details['title']

    def delete_column(self):
        column_id = self.column_id
        if self.column_name in self.board.columns:
            del self.board.columns[self.column_name]
            return self.send_request.post_request(
                query='mutation{ delete_column(board_id: ' + self.board.board_id + ', column_id:"' + column_id +
                      '") { id }}')['delete_column']['id']
        else:
            raise Exception('Column not found')
