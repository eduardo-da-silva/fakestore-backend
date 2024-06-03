from firebase_admin import initialize_app
from firebase_admin import messaging

app = initialize_app()

# registration_token = "es7Ic22E-eNZ5pdQewwlB4:APA91bHzXD8jutVwCyTuKa2Ay5k_pkSWNPDpDR_dAS1wfOWMJeT_BCDYT6zLP50K0T7Ml5wRVOmMwFGK-MnDfZP5hJd3JDLRLH1_jEHkCpqsjhXcbc34HDAGL0MxTM_e2MDqrSaMqMgk"
# registration_token = "cEf1yacm_4JQOezCmZ7ygx:APA91bG8y6fBR34yq8IAbW0tYAlaNVeUuYQ75BeX97kfZ-jlyhhKYGTzDIB-0ENbGMSRzpx6mNG3ksiVSPidCWleIQ6PTbOJHf7IpkqIGKRraZdAFJ05n-6zO8ScXrRP9znuO2MbdV0N"
# registration_token = "eU89jzyjH2REzYVcEhduQ3:APA91bEXWGBKpEv2mZPWr7gVAusfmw3pF7YgBhMcKBxqsmVwI-egSdjziqNwTHBqioKjALnxHSPUQScw8I2pvJhzNppswDoosEfHKoLaV5OUsfriw8WXPO_eLEkDv-MtJrA3F1d4oXZa"
# registration_token = "f264gc23l7DgF9feJztk_v:APA91bHH66OSYpcHYkH97tvef2-eZClhwBZBYLaWDAI0VNQmCyAnSDyTnDlBMKraTXYJSrxA5mneY9YPoulvKOS-5tjaklftc-2M_PGU7zCRJmA9Sg7naVUBhOd4Poq86CjjAWhzQkfa"
registration_token = "ey2eLoPTMVLzdx_jZu1y0V:APA91bEbMY4-gIhDRvb0u2rWiY1A89rCt449n0TcRi8PX0rE3MzlWQwQNvxEDdppYIULdK__v_ed8klnsee2YnBbmQrrkAkQHAjRT16eSbXoh2Zphk8ZgmhcOnHj5tPksbJf3jILAYFt"

message = messaging.Message(
    data={
        "title": "Mais uma mensagem do python",
        "body": "Aprenda Django...\n\nSaiba mais...",
    },
    token=registration_token,
)

response = messaging.send(message)
print("Successfully sent message:", response)
