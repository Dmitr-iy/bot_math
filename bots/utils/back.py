
async def send_back(call, message_text, reply_markup=None):
    await call.message.answer(message_text, reply_markup=reply_markup)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
