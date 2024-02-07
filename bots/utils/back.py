
async def send_back(call, message_text, reply_markup=None):
    await call.message.answer(message_text, reply_markup=reply_markup)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()


numbers = [
        '1', '3', '6',
        '7', '8', '10',
        '11', '13', '15',
        '16', '18'
    ]


number = [
        2, 4, 5,
        9, 12, 14,
        17, 19
    ]
