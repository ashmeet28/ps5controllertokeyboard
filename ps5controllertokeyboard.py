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

    # print(event)
    # continue

    if event.type == 3 and event.code == 17 and event.value == -1:
        ui.write(ecodes.EV_KEY, ecodes.KEY_W, 1)
        ui.syn()
        is_key_w_down = True

    if event.type == 3 and event.code == 17 and event.value == 1:
        ui.write(ecodes.EV_KEY, ecodes.KEY_S, 1)
        ui.syn()
        is_key_s_down = True
    
    if event.type == 3 and event.code == 17 and event.value == 0:
        if is_key_w_down:
            ui.write(ecodes.EV_KEY, ecodes.KEY_W, 0)
            ui.syn()
            is_key_w_down = False

        if is_key_s_down:
            ui.write(ecodes.EV_KEY, ecodes.KEY_S, 0)
            ui.syn()
            is_key_s_down = False

    if event.type == 3 and event.code == 16 and event.value == -1:
        ui.write(ecodes.EV_KEY, ecodes.KEY_A, 1)
        ui.syn()
        is_key_a_down = True

    if event.type == 3 and event.code == 16 and event.value == 1:
        ui.write(ecodes.EV_KEY, ecodes.KEY_D, 1)
        ui.syn()
        is_key_d_down = True
    
    if event.type == 3 and event.code == 16 and event.value == 0:
        if is_key_a_down:
            ui.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
            ui.syn()
            is_key_a_down = False

        if is_key_d_down:
            ui.write(ecodes.EV_KEY, ecodes.KEY_D, 0)
            ui.syn()
            is_key_d_down = False
    
    if event.type == 1 and event.code == 307:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_K, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_K, 0)
            ui.syn()

    if event.type == 1 and event.code == 304:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_J, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_J, 0)
            ui.syn()
    
    if event.type == 1 and event.code == 305:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_L, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_L, 0)
            ui.syn()
    
    if event.type == 1 and event.code == 308:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_H, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_H, 0)
            ui.syn()
    
    if event.type == 1 and event.code == 310:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_Y, 0)
            ui.syn()
    
    if event.type == 1 and event.code == 311:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_O, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_O, 0)
            ui.syn()

    if event.type == 1 and event.code == 314:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_U, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_U, 0)
            ui.syn()

    if event.type == 1 and event.code == 315:
        if event.value == 1:
            ui.write(ecodes.EV_KEY, ecodes.KEY_I, 1)
            ui.syn()
        if event.value == 0:
            ui.write(ecodes.EV_KEY, ecodes.KEY_I, 0)
            ui.syn()


ps5_controller.ungrab()
ui.close()
