from pypresence import Presence
import time

def update_presence():
    RPC.update(
        state='Playing Solo',
        details='Competitive',
        start=1108663200,
        # end=1739815200,
        large_image='autism',
        large_text='UwU',
        small_image='frog',
        small_text='Frog - Level 19',
        party_id='429525273965363202',
        party_size=[1, 2],
        buttons=[
            {'label': 'GitHub', 'url': 'https://github.com/J4nis05'},
#            {'label': 'Website', 'url': 'https://www.J4nis05.ch'},
            {'label': 'YouTube', 'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}
        ]
    )


def main():
    try:
        time.sleep(15)
    except KeyboardInterrupt:
        confirm_exit = input('Confirm Exit [Y/n] ').capitalize()
        match confirm_exit:
            case 'Y' | '':
                exit()
            case 'N':
                return
            case _:
                print('Input not Recognized')
                return


app_id = '123456'
RPC = Presence(app_id)
print('Setting Application ID... ')

RPC.connect()
print('Connecting To Discord... ')

print('Setting Discord Rich Presence... ')
update_presence()
print('Discord Rich Presence Updated Successfully!')

while True:
    main()
