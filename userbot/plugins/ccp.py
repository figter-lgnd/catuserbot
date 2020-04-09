"""
Time In Profile Pic.....
Command: `.cpp`

:::::Credit Time::::::
1) Coded By: @s_n_a_p_s
2) Ported By: @r4v4n4 (Legend)
3) End Game Help By: @spechide
NOTE: NO.4 IS A VIRUS WHICH HAD COME HERE ACCIDENTALLY
4) Custom / Modified Plugin for some magical effects by this Legendary Guy @PhycoNinja13b 


#curse: who ever edits this credit section will goto hell

⚠️DISCLAIMER⚠️

USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/d20e550429ee2b5e555fc.jpg",
                         "https://telegra.ph/file/9cb141ddbba7a513209a0.jpg",
                         "https://telegra.ph/file/c3f08f75d03120e35ecd6.jpg",
                         "https://telegra.ph/file/ef30e9b495124d101843f.jpg",
                         "https://telegra.ph/file/e16b0f8dddfa06a579f12.jpg",
                         "https://telegra.ph/file/b90f2c39a29e18fac5d92.jpg",
                         "https://telegra.ph/file/335ea6f198926edec947f.jpg",
                         "https://telegra.ph/file/0ce2db182ea36f1961902.jpg",
                         "https://telegra.ph/file/a84205649eeeb96eadaaa.jpg",
                         "https://telegra.ph/file/114f8f24cd288faa6d8f9.jpg",
                         "https://telegra.ph/file/c1ee0aa020c0088f604b7.jpg",
                         "https://telegra.ph/file/f682e827a8ff1b036b4fd.jpg",
                         "https://telegra.ph/file/09576593cdf0670fcdd92.jpg",
                         "https://telegra.ph/file/ed752bfbbb115d4245639.jpg",
                         "https://telegra.ph/file/ad7eed66805bdeb43c326.jpg",
                         "https://telegra.ph/file/63cb6abc5468d522e53d8.jpg",
                         "https://telegra.ph/file/eeeedabfb99ebf2a02bfe.jpg",
                         "https://telegra.ph/file/9d48ed526e847b098866e.jpg",
                         "https://telegra.ph/file/2b5a971583241cde98223.jpg",
                         "https://telegra.ph/file/3bd924a5bdb43feba85a6.jpg",
                         "https://telegra.ph/file/cef910a11389e2196dea9.jpg",
                         "https://telegra.ph/file/fdb28ac326bae5d72d991.jpg",
                         "https://telegra.ph/file/310688bd4a8577bd5c3f2.jpg",
                         "https://telegra.ph/file/4973fe8da3ed8492d2dc8.jpg",
                         "https://telegra.ph/file/c2c0963c1fa2281f8b5dc.jpg",
                         "https://telegra.ph/file/a67fb0bafe5e3cf34f78e.jpg",
                         "https://telegra.ph/file/358647de948a0ae12c5c8.jpg",
                         "https://telegra.ph/file/acc4167a69ca4e0daca08.jpg",
                         "https://telegra.ph/file/d4de3301cec4ba5d2066c.jpg",
                         "https://telegra.ph/file/0235b31770a10aae0aab2.jpg",
                         "https://telegra.ph/file/1c099ab0385d1fbc595dd.jpg",
                         "https://telegra.ph/file/6f6bffdb3790c5e7e45ca.jpg",
                         "https://telegra.ph/file/0a8ce654acbb308850830.jpg",
                         "https://telegra.ph/file/175cb39d58b91ec1a1088.jpg",
                         "https://telegra.ph/file/37ef5df87eef4ca403ea7.jpg",
                         "https://telegra.ph/file/2ffd17740e90a32f9227d.jpg",
                         "https://telegra.ph/file/df3aad4e16d9362a3f600.jpg",
                         "https://telegra.ph/file/5d84085a146b6fcc07c17.jpg",
                         "https://telegra.ph/file/4bff8cd433e3e23ae15f5.jpg",
                         "https://telegra.ph/file/320fec079acc240dcb2f3.jpg",
                         "https://telegra.ph/file/39283e7e99f63eddd4580.jpg",
                         "https://telegra.ph/file/f9d5b552612ec3dbbda57.jpg",
                         "https://telegra.ph/file/5690c40d89e131f4b551a.jpg",
                         "https://telegra.ph/file/5690c40d89e131f4b551a.jpg",
                         "https://telegra.ph/file/9b1aa727f9d8497a367c3.jpg",
                         "https://telegra.ph/file/1469d44a2233800e40516.jpg",
                         "https://telegra.ph/file/1469d44a2233800e40516.jpg",
                         "https://telegra.ph/file/1469d44a2233800e40516.jpg",
                         "https://telegra.ph/file/25df7e589dfcdee0b9bdc.jpg",
                         "https://telegra.ph/file/94e2f87014a9cb3cc3615.jpg"
                        ]
@borg.on(admin_cmd(pattern="ampp ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./ravana/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("Bulati Hai \n Magar Jane Ka Nai ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((200, 250), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(900)
        except:
            return
