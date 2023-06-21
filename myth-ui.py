import PySimpleGUI as sg



def init_ui():

    global layout
    #sg.Input(key='solc', size=(15, 2)
    sg.theme('DarkAmber')

    input_frame = [
        [
            sg.Frame('File assets', [
                [   
                    sg.Text('Solidity File: ', size=(10, 1), font='arial 11 bold'), sg.Stretch(),
                    
                    sg.Combo(
                        values=['value' for _ in range(8)], ## placeholder
                        default_value=None,
                        size=(17,6),
                        font='arial 11'
                    ), 
                    
                ],
                [
                    sg.FolderBrowse('..', font='arial 9 bold', size=(1,0)), sg.Stretch(), sg.Input('PLACEHOLDER', key='FOLDER', enable_events=True, size=(28,3))
                ],
                [sg.Button('SUBMIT', font='verdana 15 bold', button_color='black on ')]
            ])
        ]
    ]


    layout = [
        [sg.Column(input_frame)]
        
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