import sheets
from mailchimp3 import MailChimp
import secrets

my_spreadsheet = "1N_kE1qu7FheLxK95Bi8Ex3wZvS2E7kbBwxZmk7w-kVk"
#my_spreadsheet = "1caOuonv31-xjMAsgKfDxJD5nE0v0oM97WxINC-T6I08"

users = sheets.get(my_spreadsheet, "D6:E")

chapter_users = [user for user in users if len(user) == 2 and user[1] == "NoC South"]


client = MailChimp(mc_api=secrets.key, mc_user=secrets.uname)

list_id = client.lists.all()["lists"][0]["id"]

print(len(chapter_users))
for user in []:#chapter_users:
    try:
        client.lists.members.create(list_id=list_id, data=
          {
            "status":"subscribed", 
            "email_address":user[0]
          }
        )
    except:
        print("user existed")
    
 
