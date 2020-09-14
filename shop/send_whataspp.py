from twilio.rest import Client


def SendWhatsapp(body):
    account_sid = 'AC621671b8db42539275d67bb1c7ae3d55'
    auth_token = '510a574786d023e44a2c5252786393e1'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+14439372266',
                        to='+573014723047'
                    )
