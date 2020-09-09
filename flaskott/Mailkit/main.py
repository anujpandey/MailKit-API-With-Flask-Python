# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#import mailkit

from flaskott.Mailkit import mailkit


global campaign_mailkit_list
def mailkit_campaigns_list(client_id,client_MD5,ID_message):
    # Use a breakpoint in the code line below to debug your script.
    #print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    return mailkit.call_mailkit_campaigns_list(client_id,client_MD5,ID_message)


def create_mailkit_campaigns(client_id,client_MD5,name_of_campaign, subject_of_campaign,type_message):
        return mailkit.call_create_mailkit_campaigns(client_id,client_MD5,name_of_campaign, subject_of_campaign,type_message)
# Press the green button in the gutter to run the script.

def create_sendemailMail(client_id,client_MD5,campaign_ID,Send_to,subject,content):
        return mailkit.call_sendemailMail(client_id,client_MD5,campaign_ID,Send_to,subject,content)
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    demonstrate_mailkit_api(name)
