from evdev import InputDevice, UInput, ecodes, list_devices

ps5_controller = None

for device_path in list_devices():
    if InputDevice(device_path).name == 'DualSense Wireless Controller':
        ps5_controller = InputDevice(device_path)
        break


ps5_controller.grab()
ui = UInput()

is_key_w_down = False
is_key_s_down = False
is_key_a_down = False
is_key_d_down = False

for event in ps5_controller.read_loop():
    if event.type == 1 and event.code == 318:
        break
    if event.type == 1 and event.code == 317:
        break

    if event.type == 3 and event.code == 17 and value == -1:
        ui.write(e.EV_KEY, e.KEY_W, 1)
        ui.syn()
        is_key_w_down = True

    if event.type == 3 and event.code == 17 and value == 1:
        ui.write(e.EV_KEY, e.KEY_S, 1)
        ui.syn()
        is_key_s_down = True
    
    if event.type == 3 and event.code == 17 and value == 0:
        if is_key_w_down:
            ui.write(e.EV_KEY, e.KEY_W, 0)
            ui.syn()
            is_key_w_down = False

        if is_key_s_down:
            ui.write(e.EV_KEY, e.KEY_S, 0)
            ui.syn()
            is_key_s_down = False

    if event.type == 3 and event.code == 16 and value == -1:
        ui.write(e.EV_KEY, e.KEY_A, 1)
        ui.syn()
        is_key_a_down = True

    if event.type == 3 and event.code == 16 and value == 1:
        ui.write(e.EV_KEY, e.KEY_D, 1)
        ui.syn()
        is_key_d_down = True
    
    if event.type == 3 and event.code == 16 and value == 0:
        if is_key_a_down:
            ui.write(e.EV_KEY, e.KEY_A, 0)
            ui.syn()
            is_key_a_down = False

        if is_key_d_down:
            ui.write(e.EV_KEY, e.KEY_D, 0)
            ui.syn()
            is_key_d_down = False
    

ps5_controller.ungrab()
ui.close()
