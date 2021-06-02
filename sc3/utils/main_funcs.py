def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Unable to retrieve tweets
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            '관심 리스트에 추가되었습니다.',
            'success'
        ),
        (
            '관심 리스트에서 삭제되었습니다.',
            'success'
        ),
        (
            '입력된 값이 없습니다.',
            'warning'
        ),
        (
            '분석 완료 되었습니다.',
            'success'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }
