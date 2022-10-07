import moviepy.editor 

def askFileName():
    while(True):
        try:
            mp4_file = input('File name (sample.mp4): ')

            if (mp4_file[len(mp4_file)-4:len(mp4_file)]!= '.mp4'):
                print('Error: '+'"'+mp4_file+'"'+' is not a valid name!')
                continue

            mp3_file = input('New file name: (sample.mp3): ')

            if (mp3_file[len(mp3_file)-4:len(mp3_file)]!= '.mp3'):
                print('Error: '+'"'+mp4_file+'"'+' is not a valid name!')
                continue

            videoclip = moviepy.editor.VideoFileClip(mp4_file)

            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)

            audioclip.close()
            videoclip.close()
            print('Completed!')
        except:
            print('Error: no such file!')
        finally:
            again = input('\nWould you like try again? [Y/n] ')
            print('')
            if(again == 'y' or again == 'Y'):
                continue
            else:
                break

askFileName()
