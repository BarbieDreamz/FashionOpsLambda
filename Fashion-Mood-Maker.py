# Runtime: Python 3.8
#This code needs to be tested to see if it still works. This code is over a year old.
def lambda_handler(event, context):
  
    # In this lab, the lambda_handler "event" parameter has the following structure of name/value pairs:
    # {
    #     "emoji_type": number,
    #     "message": "string"
    # }

    emoji_type = event["emoji_type"]

    # Here the message value is extracted from the event Lambda parameter and passed to a variable called message.
    message = event["message"]
    #feeling =event["feeling"]
    #new_message = event["new_message"]
    
    # The variables are printed here, which means the variable values will be displayed in CloudWatch logs and the Execution Results panel.
    print(emoji_type)
    print(message)
    #print(feeling)
    #print(new_message)
    
    feeling=None
    #new_message = None
    
    # That is, if the value of emoji_type is equal to 0, we execute the statement inside its block
    if emoji_type == 0:
        # Only execute if id is equal to 1
        # The variable custom_message combines "Message for code 0:" string with the variable message
        feeling ="positive" #+ feeling
        #new_message = "positive:" + new_message

    elif emoji_type == 1:
        # The variable custom_message combines "Message for code 1:" string with the variable message
        feeling ="neutral" #+ feeling
        #new_message = "neutral" + new_message

    else:
        # The variable custom_message combines "Message for all other codes:" string with the variable message
        feeling ="negative" #+ feeling
        #new_message = "negative" + new_message

    response = {
      # In this name-value pair, the literal value "message" will store the value of the variable custom_message.
      #  "message": message,
        # In this name-value pair, the literal value "id" will store the value of the variable id.
        "feeling":feeling,
#        "new_message": new_message,
        "message":message,
    }
    
    # The execution of the lambda function is finished.
    return response
