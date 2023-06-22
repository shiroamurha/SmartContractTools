import PySimpleGUI as sg



def init_ui():

    global layout
    #sg.Input(key='solc', size=(15, 2)
    sg.theme('DarkAmber')
    frames_size = (310, 260)

    input_frame = [[sg.Frame('File Assets', [
        [   
            sg.Text('Solidity File: ', size=(10, 1), font='arial 11 bold'), sg.Stretch(), 
            
            sg.Combo(
                values=['value' for _ in range(8)], ## placeholder
                default_value=None,
                size=(23,6),
                font='arial 11',
                key='sol file'
            ), sg.Push()
        ],

        [
            sg.VPush(),
            sg.FolderBrowse('..', font='arial 8 bold'),
            sg.Input('PLACEHOLDER', key='file directory', size=(35,1), font='arial 11', enable_events=True)
        ],

        [
            sg.VPush(),
            sg.FolderBrowse('..', font='arial 8 bold'),
            sg.Input('PLACEHOLDER', key='analysis dump directory', size=(35,1), font='arial 11', enable_events=True)
        ], 
        [sg.VPush()],
        [
            sg.VPush(),
            sg.Button('START ANALYSIS', font='verdana 15 bold', button_color='black on ', size=(20,3), key='start')
        ]
    ], size=frames_size, relief=sg.RELIEF_SUNKEN, pad=(0, 0))]]

    output_frame = [[sg.Frame('Output', [

        [sg.Multiline(
            size=(40, 15), 
            key='OUTPUT', 
            autoscroll=True, 
            disabled=True, 
            background_color='black', 
            text_color='white')]
    ], size=frames_size, pad=(0, 0))]]


    layout = [[
        sg.Column(input_frame, vertical_alignment = 't'),
        sg.Column(output_frame, pad=(0, 0))
    ]]



def main():

    init_ui()
    window = sg.Window('Mythril to Json', layout, resizable=False)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'start':
            window['OUTPUT'].update(
                f'{values["OUTPUT"]}\nsla oq coimeço aqui este arquivo da silva: {values["sol file"]}'
            )

    window.close()



if __name__ == "__main__":
    main()