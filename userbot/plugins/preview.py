"""
Reply to a message with .preview to toggle the webpage preview of a message
"""
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.messages import EditMessageRequest

from userbot.plugins.kbass_core import self_reply_cmd


@self_reply_cmd(borg, pattern=r"preview")
async def on_edit_preview(event, target):
    try:
        await borg(EditMessageRequest(
            peer=await event.get_input_chat(),
            id=target.id,
            no_webpage=bool(target.media),
            message=target.message,
            entities=target.entities
        ))
    except MessageNotModifiedError:
        # There was no preview to modify
        pass
