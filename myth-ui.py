import PySimpleGUI as sg
import os
import myth2json



def init_ui():

    global layout
    sol_files_list = ['|| ALL FILES ||']

    file_path = os.path.dirname(os.path.abspath(__file__))
    dir_files = str(os.popen('ls').read()).split('\n')

    for item in dir_files:
        if '.sol' in item:
            sol_files_list.append(item.replace('.sol', ''))
    
    sg.theme('DarkGrey2')
    frames_size = (310, 260)

    input_frame = [[sg.Frame('File Assets', [
        [   
            sg.Text('Solidity File: ', size=(10, 1), font='arial 11 bold'), sg.Stretch(), 
            
            sg.Combo(
                values=sol_files_list, ## placeholder
                default_value=None,
                size=(23,6),
                font='arial 11',
                key='sol file',
                readonly=True
            ), sg.Push()
        ],

        [
            sg.VPush(),
            sg.FolderBrowse('..', font='arial 8 bold', pad=(1,0), button_color='#B3B3B3 on #284B5A', initial_folder=file_path),
            sg.Input(file_path, key='file directory', size=(35,1), pad=(0,0), font='arial 11', enable_events=True, border_width=0)
        ],

        [
            sg.VPush(),
            sg.FolderBrowse('..', font='arial 8 bold', pad=(1,0), button_color='#B3B3B3 on #284B5A'),
            sg.Input(default_text=f'{file_path}/analysis', key='analysis dump directory', size=(35,1), pad=(0,0), font='arial 11', enable_events=True, border_width=0, )
        ], 
        [
            sg.Button(
                'START ANALYSIS', 
                font='verdana 15 bold', 
                button_color='black on #ed4245', 
                size=(20,3), 
                key='start',
                mouseover_colors=('#141414', '#7a2223'),
                border_width=0
            ),
        ]
    ], size=frames_size, relief=sg.RELIEF_SUNKEN, pad=(0, 0), border_width=0)]]

    output_frame = [[sg.Frame('Output', [

        [sg.Multiline(
            size=(50, 17), 
            key='OUTPUT', 
            font = 'Consolas 9 bold',
            autoscroll=True, 
            disabled=True, 
            background_color='black', 
            text_color='white', 
            border_width=0, 
            sbar_background_color='#284B5A',
            sbar_trough_color='black',
            sbar_frame_color = 'black',
            sbar_relief = 'black',
            sbar_arrow_color = '#B3B3B3', 
            reroute_stdout=True
        )]
    ], size= (370, 260), pad=(0, 0), border_width=0)]]


    layout = [[
        sg.Column(input_frame, vertical_alignment = 't'),
        sg.Column(output_frame, pad=(0, 0))
    ]]



def main():

    init_ui()
    window = sg.Window('Mythril to Json', layout, resizable=False, background_color='#282923')
    
    while True:  # Event Loop
        event, values = window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'start':

            if values["sol file"] == '|| ALL FILES ||':
                myth2json.main()

            else:
                myth2json.main(values["sol file"])

    window.close()



if __name__ == "__main__":
    main()