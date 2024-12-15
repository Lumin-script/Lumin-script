# 进口
从常量导入 *
从代币导入 *
从错误导入*
从位置导入位置

# 创建一个新的词法分析器类
词法分析器类别：
    def    __init__ ( self, fn, 文本) :
        # 初始化参数
        自己。fn = fn
        自己。文字=文字
        # 初始化位置
        自己。pos =位置( - 1 , 0 , - 1 , fn , 文本)
        自己。当前字符=无
        自己。进步（）

    # 创建一个新的高级函数
    默认提前（自我）：
        自己。位置。提前( self. 当前角色  ）
自己。当前字符=自身。文本[自我。位置。idx ]如果是自己。位置。idx < len      ( self.text ) else 无       

    # 生成列表的函数
    def        make_tokens       ( self ) :
        # 初始化列表为“Token”
        代币 = [       ]

        #
        而自我。当前字符：
            如果是自己的话。'\t'中的current_char ：
                自己。进步（）
            埃利夫自己。数字中的当前字符：
                代币。追加( self.make_number ( ) )                  
：
                代币。追加(       Token       ( TT_PLUS, pos_start= self.pos      )     )
                自己。进步（）
            埃利夫自己。当前字符== '-'：
                代币。追加(  令牌  ( TT_MINUS, pos_start= self.pos       )       )
                自己。进步（）
            埃利夫自己。当前字符== '*'：
                代币。追加(       Token       ( TT_MUL, pos_start= self.pos       )       )
                自己。进步（）
            埃利夫自己。当前字符== '/'：
                代币。追加(      Token      ( TT_DIV, pos_start= self.pos      )      )
                自己。进步（）

                代币。追加(令牌( TT_LPAREN, pos_start= self.pos      )      )
                自己。进步（）

                代币。追加(令牌( TT_RPAREN, pos_start= self.pos      )      )
                自己。进步（）
            另外：
                pos_start = 自我.位置。复制（）
                字符=自我。当前字符
                自己。进步（）
                return        [       ] , IllegalCharacterError       ( pos_start, self.pos , " '" + char + "'"      )

        代币。追加(     Token    ( TT_EOF, pos_start= self.pos   )  )
        返回令牌，无

    def  make_number ( self ) :
        num_str = ''
        点数 = 0
        pos_start = 自我.位置。复制（）

        while self.current_char and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            返回 Token ( TT_FLOAT, float ( num_str ) , pos_start, self.pos )
