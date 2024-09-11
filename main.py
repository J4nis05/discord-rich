import pypresence
from pypresence import Presence
import time


def load_env(file_path):
    env_dict = {}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            value = value.strip('\'"')
            env_dict[key.strip()] = value

    return env_dict


def set_value(value, value_type):
    if value is None or 0 or '' and value_type is not bool:
        return None
    elif value is None or 0 or '' and value_type is bool:
        return True

    match value_type:
        case 'int':
            return int(value)
        case 'str':
            return str(value)
        case 'bool':
            return bool(value)
        case _:
            print("Unknown value type")
            return value


def set_party_size(party_min, party_max):
    return [set_value(party_min, 'int'), set_value(party_max, 'int')]


def set_buttons(b1_label, b1_url, b2_label, b2_url):
    # Check Weather one or both buttons contain an empty element
    if b1_label is None or 0 or '' or b1_url is None or 0 or '':
        if b2_label is None or 0 or '' or b2_url is None or 0 or '':
            # Buttons 1 & 2 Contain Empty Elements
            return None
        else:
            # Button 1 Contains empty Elements, Return Stuff from Button 2
            element = [{'label': b2_label, 'url': b2_url}]
    else:
        if b2_label is None or 0 or '' or b2_url is None or 0 or '':
            # Button 1 Has Stuff, but Button 2 is Empty, Return Button 1
            element = [{'label': b1_label, 'url': b1_url}]
        else:
            # Return Both Buttons
            element = [{'label': b1_label, 'url': b1_url}, {'label': b2_label, 'url': b2_url}]

    return element


def update_presence():
    RPC.update(
        state=set_value(env['drp_state'], 'str'),
        details=set_value(env['drp_details'], 'str'),
        start=set_value(env['drp_start'], 'int'),
        end=set_value(env['drp_end'], 'int'),
        large_image=set_value(env['drp_large_img'], 'str'),
        large_text=set_value(env['drp_large_txt'], 'str'),
        small_image=set_value(env['drp_small_img'], 'str'),
        small_text=set_value(env['drp_small_txt'], 'str'),
        party_id=set_value(env['drp_party_id'], 'str'),
        party_size=set_party_size(env['drp_party_size'], env['drp_party_max']),
        #join=set_value(env['drp_join_hash'], 'str'),
        #spectate=set_value(env['drp_spectate_hash'], 'str'),
        #match=set_value(env['drp_match_hash'], 'str'),
        buttons=set_buttons(env['drp_button1_label'], env['drp_button1_url'],
                            env['drp_button2_label'], env['drp_button2_url']),
        instance=set_value(env['drp_instance'], 'bool')
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


env = load_env('.env')

RPC = Presence(env['app_id'])
print('Setting Application ID ... ')
RPC.connect()
print('Connecting To Discord ... ')
print('Setting Discord Rich Presence ... ')
update_presence()
print('Discord Rich Presence Updated Successfully!')


while True:
    main()


