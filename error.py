from swa import string_with_arrows


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'File {self.pos_start.fn} line {self.pos_end.ln + 1}' + '\n'
        result += string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end) + '\n'
        result += f'{self.error_name}: {self.details}'
        return result

