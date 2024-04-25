import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv, dotenv_values
import re
import flatten_json as fj
import pandas as pd 

#
# channel_id=''
load_dotenv()
api_token=os.getenv("API_TOKEN")
client=WebClient( api_token, "https://app.slack.com/api/")


def get_user_info(user_id):
    '''
    function to retrieve the user information , such as name surname based on id 
    '''
    try:
        # Call the users.info API method
        response = client.users_info(
            user=user_id,
        )

        user_info = response["user"]
        return user_info
    except SlackApiError as e:
        print(f"Error fetching user info: {e.response['error']}")

def get_list_of_members(channel_id):

    '''
    Function to get the list of members part of a channel , and their respective information
    '''

    try:
        list_of_members_ids=client.conversations_members(channel=channel_id)['members']
        print('list of members \n',list_of_members_ids)

        list_of_members={'id':'name'}

        for id in list_of_members_ids:
            member_name=get_user_info(id)['name']
            list_of_members.update({id:member_name})

        return list_of_members

    except SlackApiError as e:
        print(f"Error fetching user list: {e.response['error']}")

#def get_channel_history(client,channel_id):
    #




#def get_channel_members_list(channel_id):

if __name__=='__main__':
    #api token and channel 

    client = WebClient(api_token, "https://app.slack.com/api/")
    conversation_history = []
    #
    # response = client.conversations_history(channel=channel_id)
   
    membersList=get_list_of_members(channel_id)
    print(membersList)

    try:
        result = client.conversations_history(channel=channel_id)
        print('TYPE',type(result))
        conversation_history = result["messages"]

    except SlackApiError as e:
        print(f"Error: {e}")
    #print(conversation_history)
    u=get_user_info('U06RXTUM8DP')

    # for message in conversation_history:
    #     user_gifting_recg=message['user']

    #     if message['blocks'][0]

    message=conversation_history[0]
    test=message['blocks'][0]['elements'][0]['elements']
    print(test)
 
    for x in test:
        print('TESTING \n',x)
    
    # df=pd.DataFrame(columns=['Sender','Receiver','Recognition Type'])
    # print(df)
    # df.insert(column='Receiver',value='A')
    for i,message in enumerate(conversation_history) :
        if message.get('subtype') in ['channel_join', 'channel_leave']:
            continue
        
        #print('Sender: ',message.get('user'),'Message: ',message.get('text'))
        sender=message.get('user')
        line= message.get('text')
        flat=fj.flatten(message.get('blocks')[0])
        
        # print('Unflat VERSION \n',message)
        # print('FLAT VERSION \n',i,'\n',flat)

        print(message.get('blocks')[0]['elements'][0]['elements'])
    
        # if re.search("<@\w{11}>",line): #maybe add a check for # as well 
            
        # else:
        #     continue

        '''
        1st option :
            check text format by using regex and then if format is @name #Tag use the block to get the respective info
            cheks the text format if @name @name up to 5 tags then #tag we use again the block

            How to deal with the format that is not @name #tag and how to distinguish from other msgs 
            that might just be a description of why the recognition was given
            
            break the code into different functions with respective comments to clean the code and make it maintainable 

        '''
        #print(message['blocks'][0]['elements'][0]['elements'])
        #print(message.get('blocks'))
        

    #print(conversation_history)


    # for x,y in message['blocks'][0][2]:
    #     print(x,y)



   # print(u)