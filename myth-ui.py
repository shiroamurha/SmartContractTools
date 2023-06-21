import PySimpleGUI as sg



def init_ui():

    global layout
    #sg.Input(key='solc', size=(15, 2)
    sg.theme('DarkAmber')

    input_frame = [
        [
            sg.Frame('', [
                [   
                    sg.Text('Solidity File: ', size=(15, 1)), 
                    
                    sg.Combo(
                        values=['value' for _ in range(8)], ## placeholder
                        default_value=None,
                        size=(15,6)
                    )            
                ],
                [
                    sg.FolderBrowse('...', font='bold'), sg.Input(key='FOLDER', enable_events=True)
                ],
                [sg.Button('SUBMIT', font='verdana 15 bold', button_color='black on ')]
            ])
        ]
    ]


    layout = [
        
        input_frame
    ]



def main():

    init_ui()
    window = sg.Window('Mythril to Json', layout, resizable=False)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Show':
            window['-OUTPUT-'].update(values['solc'])

    window.close()



if __name__ == "__main__":
    main()